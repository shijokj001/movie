from django.db import models
from django.utils.translation import gettext_lazy as _


class Movie(models.Model):
    """docstring for Movie."""

    MOVIE_GENRE = (
        ('action', _('Action')),
        ('adventure', _('Adventure')),
        ('comedy', _('Comedy')),
        ('drama', _('Drama')),
        ('horror', _('Horror')),
    )

    name = models.CharField(max_length=200)
    genre = models.CharField(choices=MOVIE_GENRE, max_length=10, blank=True)
    studio = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    cast = models.CharField(max_length=255)
    collection = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    release_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """Docstring for str."""
        return self.name


