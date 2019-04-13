from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

##UserProfileManager inherits from models.Manager
##So it inherits it's methods
##So super().get_queryset() is calling the method get_queryset from the models.Manager class and
##then we are customizing the output.

##The reason for making is a class is incase we have to do this operation lots of times it would be
##tiresome to have to include it everytime and write UserProfile.objects.filter(city = 'London') everytime so
##just associate the UserProfileManager with a filter (London in this case)
##in the UserProfile class by writing London = UserProfileManager()




class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(city='London')




##Each model is one structure on one table on the database
##userprofile is a name that we made up but the elements of this class inherit from models.Model
##So basically we are telling django that we are creating a class which is a django model and
##will be one table in our database
##class UserImage(User):
##    image = models.ImageField(upload_to= 'profile_image', blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100,default='',null=True)
    city = models.CharField(max_length=100,default='', null=True)
    website = models.URLField(default='', null=True)
    phone = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to= 'profile_image', blank=True)

    london = UserProfileManager()
    objects = models.Manager()
##def below changes the string from UserObject to username in admin

    def __str__(self):
        return "%s" %(self.user)

#this code works i just dont have the visual representation in django admin of userprofiles, but they are created when a user is added(checkd in shell)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


















