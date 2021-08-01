from django.db import models
from django.contrib.auth.models import AbstractUser
LEVEL_CH = (
    ('0', 'beginner'),
    ('1', 'junior'),
    ('2', 'mid'),
    ('3','senior'),
)
class mainUser(AbstractUser):
    age =models.IntegerField(verbose_name='Age',null=True,blank=True)
    salary = models.IntegerField(verbose_name= 'Salary')
    level = models.CharField(max_length=1,default='0',verbose_name='Level')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['level','salary']

    def __str__(self):
        return self.username
