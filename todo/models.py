from django.db import models


# Create your models here.
class Item(models.Model):
    """ creates item model with 2 fields: name and done """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """
        override the string method just to change how our items are displayed
        """
        return self.name
