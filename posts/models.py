from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=254)
    summary = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=254, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
