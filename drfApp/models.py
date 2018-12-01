from django.db import models



class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title   = models.CharField(max_length=50)
    content = models.TextField()
    name    = models.ForeignKey(Category, on_delete= models.CASCADE)
    date    = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
