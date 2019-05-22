from django.db import models

# Create your models here.
class Music(models.Model):
    review = models.TextField(default="none")
    game = models.TextField(default="none")
    time = models.TextField(default="none")
    aview = models.TextField()
    month = models.TextField()
    #voted_up= models.TextField(default="none")
    #last_modify_date = models.DateTimeField(auto_now=True)
    #created = models.DateTimeField(auto_now_add=True)
    
#class fucker(models.Model):
    #review = models.TextField(default="none")
    #game = models.TextField(default="none")
    #time = models.TextField(default="none")
    class Meta:
        managed = True
        #db_table = "test"
        db_table = "music"
       

