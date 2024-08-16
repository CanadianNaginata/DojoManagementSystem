from django.db import models
from django.contrib.auth.models import User


class LoggableModel(models.Model):
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name="+")
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                  related_name="+")

    class Meta:
        abstract = True

# Create your models here.


class Dojo(LoggableModel):
    abbr = models.CharField(max_length=10)
    active = models.BooleanField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20)   # TODO: Make it a selection
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    probation = models.IntegerField()  # TODO: make selection
    approval_date = models.DateField(blank=True, null=True)
    contact_email = models.CharField(max_length=254)
    website = models.CharField(max_length=2048)
    notes = models.TextField()
