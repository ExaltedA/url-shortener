from hashlib import sha1

from django.db import models


# Create your models here.
class Url(models.Model):
    full_url = models.URLField(unique=True)
    url_hash = models.CharField(unique=True, blank=True, max_length=10)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def clicked(self):
        self.clicks += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = sha1(self.full_url.encode()).hexdigest()[:6]

        return super().save(*args, **kwargs)

    def __str__(self): return f'full_url: {self.full_url}'
