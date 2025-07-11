from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    file = models.FileField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} - {self.name}'



class ProductOffer(models.Model):
    product = models.ForeignKey(Product, related_name='product_offers', on_delete=models.CASCADE)
    file = models.FileField(upload_to='offers/')

    def __str__(self):
        return f'offer: {str(self.product.name)}'