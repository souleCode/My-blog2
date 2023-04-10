from django.db import models
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


# def get_upload_path(instance, filename):
#     return 'profile_pics/{0}/{1}'.format(instance.user.username, filename)

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_img = models.ImageField(upload_to=get_upload_path, blank=True, null=True)


#la fonction qui cree un chemin relatif
def get_upload_path(instance, filename):
    return 'profile_pics/{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

#les signaux pour creer une photo de profile une fois utilisateur creer
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#signaux pour enregistrer une photo.
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
