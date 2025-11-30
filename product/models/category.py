from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name