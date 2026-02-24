from django.db import models

class Resource(models.Model):
    RESOURCE_TYPE = [
        ('code', 'Code'),
        ('problem', 'Problem Set'),
        ('pdf', 'PDF'),
        ('latex', 'LaTeX'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='resources/')
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

