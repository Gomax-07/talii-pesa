import uuid  # Required for rent instances

from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


# Create your models here.
class Caretaker(models.Model):
    """Model representing a House caretaker."""
    name = models.CharField(max_length=200, help_text='Enter your House Caretaker (e.g. Macharia John)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class House(models.Model):
    """Model representing a House)."""
    house_name = models.CharField(max_length=200)

    # Foreign Key used because House can only have one tenant, but tenant can have multiple houses
    # Tenant as a string rather than object because it hasn't been declared yet in the file
    tenant = models.ForeignKey('Tenant', on_delete=models.SET_NULL, null=True)

    summary = models.CharField(max_length=250, help_text='Enter a brief description of the house location')
    # ManyToManyField used because caretaker can maintain many  Houses.  Houses can cover many caretakers.
    # Caretaker class has already been defined so we can specify the object above.
    caretaker = models.ManyToManyField(Caretaker, help_text='Select a caretaker for this House')

    def __str__(self):
        """String for representing the Model object."""
        return self.house_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this house."""
        return reverse('house-detail', args=[str(self.id)])

    def display_caretaker(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(caretaker.name for caretaker in self.caretaker.all()[:3])

    display_caretaker.short_description = 'Caretaker'


class Rent(models.Model):
    """Model representing a specific house instance and rent)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular rent across whole rentcase(s)')
    house = models.ForeignKey('House', on_delete=models.RESTRICT, null=True)
    amount = models.IntegerField()
    payment_date = models.DateField(null=True, blank=True)

    RENT_STATUS = (
        ('p', 'Pending'),
        ('r', 'Underpaid'),
        ('G', 'Paid'),
        ('o', 'Overpaid'),
    )

    status = models.CharField(
        max_length=1,
        choices=RENT_STATUS,
        blank=True,
        default='p',
        help_text='Rent_payment',
    )

    class Meta:
        ordering = ['payment_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.house.house_name})'


class Tenant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_entry = models.DateField('Entry', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('tenant-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        ordering = ['last_name']
