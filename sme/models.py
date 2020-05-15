from django.db import models

from user.models import CustomUser


# Create your models here.

#SME model

class SME(CustomUser):
    name_of_business = models.CharField(max_length=120)
    name_of_contact_person = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    financial_records = models.FileField(
        upload_to='docs/SMEs/financial_records')
