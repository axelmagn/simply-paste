from django.db import models
from pygments.lexers import get_all_lexers

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

# Create your models here.
class Snippet(models.Model):
    """
    Snippet of code or text pasted by user

    """
    # TODO: slug
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
