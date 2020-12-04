from django.db import models

# Create your models here.

class Upload(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    pdf = models.FileField(upload_to='post_pdfs')

    def __str__(self):
        return self.title