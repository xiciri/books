from django.db import models

# CRUD - create - read - update - delete


class Books(models.Model):
    title = models.CharField(max_length=250)
    # slug = models.SlugField(unique=True,null=True,blank=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    price = models.PositiveBigIntegerField()
    published = models.DateField()

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    def __str__(self):
        return self.category_name
    
class Author(models.Model):
    author_name = models.CharField(max_length=250)
    def __str__(self):
        return self.author_name