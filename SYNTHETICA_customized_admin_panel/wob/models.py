from django.db import models

class employee(models.Model) :
    name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to='pics')
    link = models.BooleanField(default=True)
    age = models.IntegerField()
    def __str__(self):
        return self.name
class product(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500)
    image = models.ImageField(upload_to='img')
    comment = models.IntegerField()
    def __str__(self):
        return self.title
    ch = ( ('AI','AI'),
           ('pro','pro'),
           ('high','high'),
           ('new','new'),
           ('old','old')
    )
    ty = models.CharField(max_length=50,choices=ch,default='AI')
    feature = models.BooleanField(default=False)

