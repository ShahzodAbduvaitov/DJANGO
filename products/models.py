from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продукта'


class ProductModel(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.FloatField()
    product_des = models.TextField()
    product_image = models.ImageField(upload_to='products')
    product_amount = models.IntegerField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Наши продукты'
        verbose_name_plural = 'Наши продукты'
