from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        reveal_type(self.id)  # example reveal of all fields in a model
        reveal_type(self.author)
        reveal_type(self.text)
        reveal_type(self.is_published)
        reveal_type(self.created_at)
        return '<BlogPost {0}>'.format(self.id)
