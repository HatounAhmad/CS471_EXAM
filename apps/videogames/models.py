from django.db import models

class Developer(models.Model):
    name=models.CharField(max_length=150,null=False)

class Games(models.Model):
    title=models.CharField(max_length=200,null=False)
    developer=models.ForeignKey(Developer,on_delete=models.CASCADE)
