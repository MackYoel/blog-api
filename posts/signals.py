from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from . import models


@receiver(pre_save, sender=models.Post)
def set_post_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
