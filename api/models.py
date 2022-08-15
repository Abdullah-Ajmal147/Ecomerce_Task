from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from user_services.models import User


class Category(models.Model):
  name = models.CharField(_('category name'), max_length=30, blank=True)

  def __str__(self):
    return self.name


class Brand(models.Model):
  name = models.CharField(_('brand name'), max_length=30, blank=True)

  def __str__(self):
    return self.name


class Country(models.Model):
  name = models.CharField(_('country name'), max_length=30, blank=True)

  def __str__(self):
    return self.name


class State(models.Model):
  name = models.CharField(_('state name'), max_length=30, blank=True)

  def __str__(self):
    return self.name


class City(models.Model):
  name = models.CharField(_('city name'), max_length=30, blank=True)

  def __str__(self):
    return self.name


class Products(models.Model):
  user = models.ForeignKey(to=User, null=False, blank=False, on_delete=models.CASCADE)
  title = models.CharField(_('product title'), max_length=30, blank=True)
  category = models.ForeignKey(to=Category, null=False, blank=False, on_delete=models.CASCADE)
  brand = models.ForeignKey(to=Brand, null=False, blank=False, on_delete=models.CASCADE)
  country = models.ForeignKey(to=Country, null=False, blank=False, on_delete=models.CASCADE)
  state = models.ForeignKey(to=State, null=False, blank=False, on_delete=models.CASCADE)
  city = models.ForeignKey(to=City, null=False, blank=False, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
