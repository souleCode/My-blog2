from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegistrationForm, ProfileForm

from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
# Create your views here.


#photo de profile



@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def my_view(request):
    profile = request.user.profile
    context = {'profile_img': profile.profile_img.url}
    return render(request, 'base.html', context)

# la vue de connexion  
def login_view(request):
    context={}
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, 'Votre compte a été créé avec succès!')
                return redirect("post_list")
                
            else:
                # messages.error(request, "Nm d'utilisateur ou mot de passe invalide!")
                return render(request,'registration/login.html')   
        else:
            return render(request,'registration/login.html')   
      
    else:
        return redirect('post_list')    
    
    

# la vue de deconnexion  
def logout_view(request):
    logout(request)
    return redirect('login_view')

def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login_view')
        else:
            return render(request, 'registration/register.html',{'user_form':user_form,})
    else:
        user_form= RegistrationForm()
        return render(request, 'registration/register.html',{'user_form':user_form,})    
            
        