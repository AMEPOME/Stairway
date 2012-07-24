from django.db import models
from django.contrib import admin

class Students(models.Model):
    ID_number = models.IntegerField(max_length=8)
    name = models.CharField(max_length=30)
    Program_of_study = models.CharField(max_length=30)
    e-mail = models.EmailField()
    institution=models.CharField(max_length=30)
    contact_number=models.IntegerField(max_length=12)
    def __unicode__(self):
       return self.name
admin.site.register(Students)
admin.site.register(ehostel)

