from django.db import models

from user.models import CustomUser
# Create your models here.

#funder model

class Funder(CustomUser):
    name_of_business = models.CharField(max_length=120)
    name_of_contact_person = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    financial_records = models.FileField(
        upload_to='docs/Funders/financial_records')

    def __str__(self):
        return self.name_of_business