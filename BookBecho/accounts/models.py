from django.db import models
from django.contrib.auth.models import User
from time import timezone
from django.core.validators import RegexValidator

class UserInfoModel(models.Model):
    user = models.OneToOneField(User,related_name='profiles',on_delete=models.DO_NOTHING)
    profile_pic = models.ImageField(upload_to='profile',default='/profiles/1.png',blank=True)
    describe = models.TextField(max_length=256,blank=True)
    bday = models.DateField()
    def __str__(self):
        return self.user.username

class UserInfo(models.Model):
    user = models.OneToOneField(User,related_name='phone',on_delete=models.DO_NOTHING)
    phone_number = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    def __str__(self):
        return self.phone_number
