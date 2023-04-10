from django.shortcuts import render,get_object_or_404
from .models import Post ,Comment,Category
from . forms import CommentForm, SearchPost
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.contrib.postgres.search import SearchVector
# Create your views here.

def post_list(request,category=None):
    posts = Post.published.all() # On remplace Post."objects" par "published"(car on veut utilser un manager)
    categories = Category.objects.all()
    if category:
        category = get_object_or_404(Category, slug=category)
        posts = posts.filter(category=category)
    
    paginator=Paginator(posts,2)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1) 
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)
        
    contexte={
        'posts': posts,
        'page': page,
        'categories': categories,
        'category': category,
    }           
   
    return render(request, 'blog/post/post_list.html',contexte)

def post_detail(request,year: int,month: int,day: int,slug :str): # on ajoute les parameters de get_absolute_url
    # try:
    #     post = Post.objects.get(slug=slug)
        
    # except Post.DoesNotExist:
    #     raise("this post not found")
    post = get_object_or_404(Post, slug=slug, status='published',publish__year=year,publish__month=month,publish__day=day) # on passe publish__pour recuperer les args=[] de get_object_or_404
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)    
            new_comment.post = post
            new_comment.save()
            comment_form = CommentForm() # retourner le formulaire vide uen fois que le commentaire est enregistrer.
        else:
            comment_form = CommentForm()
                    
    contexte={
        'post':post,
        'comments':comments,
        'new_comment':new_comment,
        'comment_form':comment_form,
    }
    return render(request,'blog/post/detail.html',contexte)


#vue generique pour remplacer post_list().
# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     paginate_by= 2
#     template_name= 'blog/post/post_list.html'
#     context_object_name= 'posts'



def post_search(request):
    query = None
    results = []
    search_form = SearchPost()
    if request.method == 'GET':
        search_form = SearchPost(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            results= Post.published.annotate(
            search= SearchVector("title", "body"),
                ).filter(search=query)
    return render(request,'blog/post/search.html',
                  {'query':query,
                   'search_form':search_form,
                   'results': results,
                   })       
        
    



