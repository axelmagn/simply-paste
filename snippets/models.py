from django.db import models
from snippets.langs import ACE_LANGUAGES
from shortuuidfield import ShortUUIDField

LANGUAGE_CHOICES = ACE_LANGUAGES

# Create your models here.
class Snippet(models.Model):
    """
    Snippet of code or text pasted by user

    """
    # uuid
    uuid = ShortUUIDField(primary_key=True, unique=True, db_index=True)
    # content
    content = models.TextField()
    # language
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='text',
                                max_length=100)
    # created
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('created',)
