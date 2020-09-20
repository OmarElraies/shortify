from django.db import models

from model_utils.models import TimeStampedModel

from .utils import url_shortener


class UrlData(TimeStampedModel):
    long_url = models.CharField('Url',max_length=256)
    shortened_url = models.CharField('Shortened Url',max_length=6)

    def save(self, *args, **kwargs):
        self.shortened_url=url_shortener()
        super(UrlData, self).save(*args, **kwargs)
