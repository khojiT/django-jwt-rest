import sys
sys.path.append("..")
from django.db import models
from django.contrib.auth.models import AbstractUser
from extensions.utils import jalali_converter
LEVEL_CH = (
    ('0', 'beginner'),
    ('1', 'junior'),
    ('2', 'mid'),
    ('3','senior'),
)
class mainUser(AbstractUser):
    age =models.IntegerField(verbose_name='Age',null=True,blank=True)
    salary = models.IntegerField(verbose_name= 'Salary')
    level = models.CharField(max_length=1,choices=LEVEL_CH,default='0',verbose_name='سطح')
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['level','salary']
    class Meta:
        verbose_name = 'فرد'
        verbose_name_plural = 'افراد'
    def __str__(self):
        return self.username
    def jpublish(self):
        return jalali_converter(self.date_joined)
    jpublish.short_description = 'زمان ورود'