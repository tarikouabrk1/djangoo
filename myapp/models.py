from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Article(models.Model):
    name=models.CharField(max_length=100)
    prix=models.DecimalField(max_digits=7,decimal_places=2)
    slug=models.SlugField(unique=True)
    date_de_publication=models.DateTimeField(auto_now_add=True)
    reduction=models.FloatField(
        default=0,
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name