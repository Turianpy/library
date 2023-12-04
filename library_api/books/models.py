from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    year = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created_at',)
