from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.


class Entry(models.Model):
    """Model representing an entry."""
    your_first_name = models.CharField(max_length=100)
    your_last_name = models.CharField(max_length=100)
    date_of_birth_of_child = models.DateField(null=True, blank=True)
    contact_information = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['your_last_name', 'your_first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular entry instance."""
        return reverse('entry-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.your_last_name}, {self.your_first_name}'
