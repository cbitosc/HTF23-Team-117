from django.db import models

# Create your models here.

class cred_model(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    contact=models.IntegerField()
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table='login_cred'

class emotion(models.Model):
    day=models.IntegerField()
    emotion=models.CharField(max_length=20)
    score=models.IntegerField()
    time=models.CharField(max_length=20)

    
    class Meta:
        db_table='emotion'