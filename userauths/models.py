from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField 
from django.db.models.signals import post_save
# Create your models here.
#one_time_password=otp

GENDER ={
    ('Female','Female'),
    ('Male','Male')
}
IDENTITY={
    ('National Identification Number','National Identification Number'),
    ('Driver Licence','Driver Licence'),
    ('International Passport','International Passport')
}

def user_director_path(instance,filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s"%(instance.user.id , filename)
    return "user_{0}/{1}".format(instance.user.id,filename)


# def user_director_path(instance,filename):
#     return "user_{0}/{1}".format(instance.user.id , filename)

class User(AbstractUser):
    full_name = models.CharField(max_length=300 , blank=True,null=True)
    username = models.CharField(max_length=200,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,choices=GENDER,default="Male")
    otp = models.CharField(max_length=100,null=True,blank=True)

    REQUIRED_FIELDS =['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username
    

class Profile(models.Model):
    pid = ShortUUIDField(length=1,max_length=30,alphabet="0123456789",prefix="PROFIL")
    image = models.FileField(upload_to=user_director_path,null=True,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300 , blank=True,null=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    gender = models.CharField(max_length=100,choices=GENDER,default="Male")
    
    country = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)

    identity_type = models.CharField(max_length=150,choices=IDENTITY,null=True,blank=True)
    identity_image = models.FileField(upload_to=user_director_path,null=True,blank=True)

    facebook = models.URLField(null=True,blank=True)
    twitter = models.URLField(null=True,blank=True)

    wallet =models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)
    verified = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.full_name:
            return f"{self.full_name}"
        else:
            return f'{self.user.username}'
        
# signal sur le modele pour la creation d'un profile
def create_user_profile(sender, instance , created , **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)  