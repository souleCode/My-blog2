from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published') #retourne seulement les articles de status published

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    STATUS_CHOISES = (('published','Published'), # on va ajouter un Model.Manager
                      ('draft','Draft'))
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES, default='published',max_length=10)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posted')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    objects = models.Manager()
    published = PublishedManager() #costumers manager,default manager
    def __str__(self) :
        return self.title
    #urls personnalises avec reverse
    def get_absolute_url(self):
       return reverse('post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug]) #on passe tout ce qu'on avoir dans notre urls dans le parametre args=[]
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    body = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.title #on recupere post dans la table Post et on recupere son titre
    
        
   


    