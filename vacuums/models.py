from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL pattern

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=20, help_text="Enter a vacuum type (ex. cordless, robot etc.)")
    image = models.FilePathField(path="/img", default='default.png')

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('brand-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=20, help_text="Enter the model name")
    description = models.CharField(max_length=200, help_text="Product name/description appeared on website")
    # Foreign Key used because  Model can only have one Brand, but Brands can have multiple Models
    # Brand as a string rather than object because it hasn't been declared yet in file.
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because type can contain many models. Brands can cover many types.
    # Type class has already been defined so we can specify the object above.
    type = models.ManyToManyField(Type, help_text='Select a vacuum type for this model')
    inventory_no = 'InventoryNumber'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this model"""
        return reverse('model-detail', args=[str(self.id)])




class InventoryNumber(models.Model):
    number = models.CharField(max_length=4, help_text=("Enter the 4-digit inventory number"))
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    date_received = models.DateField('Received', null=True, blank=True)

    def __str__(self):
        return self.number

class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


    # class ModelStatus(models.Model):
    #
    #     model = models.ForeignKey('Model', on_delete=models.RESTRICT, null=True)
    #
    #     CR = (
    #         ('C', 'Completed'),
    #         ('T', 'Testing In Progress'),
    #         ('NS', 'Not Started'),
    #     )
    #
    #     CR_STATUS = models.CharField(
    #         max_length=2,
    #         choices=CR,
    #         blank=True,
    #         default='NS',
    #         help_text='CR test status'
    #
    #     )
    #
    #     CR_due_date = models.DateField(null=True, blank=True)
