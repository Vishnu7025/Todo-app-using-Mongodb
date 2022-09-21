from djongo import models

# Create your models here.
class Todo(models.Model):
    def __str__(self) -> str:
        return self.headline
    headline = models.CharField(max_length=225)
