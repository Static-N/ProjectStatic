from django.db import models
# from multiselectfield import MultiSelectField

# Create your models here.

class genere(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class Catgry(models.Model):
    name = models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.name

class mainInfo(models.Model):
    name = models.CharField(max_length=200,null=True)
    catgrys = models.ManyToManyField(Catgry,blank=True)
    post_img = models.URLField(null=True)
    hero_img = models.URLField(null=True)
    des = models.TextField(null=True)
    imdb = models.URLField(null=True)
    rotTom = models.URLField(null=True)
    generes = models.ManyToManyField(genere)
    def  __str__(self):
        return self.name

class Reviews(models.Model):
    rev_name = models.CharField(max_length=200,null=True)
    name = models.ForeignKey(mainInfo, on_delete=models.SET_NULL, null=True,blank=True)
    review = models.TextField()
    def __str__(self):
        return self.rev_name