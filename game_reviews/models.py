from django.db import models
from django.contrib.auth import get_user_model

class GameReview(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    game = models.CharField(max_length=64)
    system = models.CharField(max_length=64)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name