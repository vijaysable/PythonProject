from django.db import models
from django.utils import timezone

class Products(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(Users, related_name='author2', default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name