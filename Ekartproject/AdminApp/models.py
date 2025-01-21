from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
    
class Products(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    description=models.TextField(max_length=100)
    rating=models.PositiveIntegerField(null=True,blank=True)
    image=models.ImageField(upload_to="images")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name