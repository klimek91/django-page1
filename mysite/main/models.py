from django.db import models

# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=100)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField("data published")

    def __str__(self):
        return self.tutorial_title