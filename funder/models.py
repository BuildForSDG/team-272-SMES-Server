from django.db import models

from user.models import CustomUser
# Create your models here.

# funder model


class Funder(CustomUser):
    organization_name = models.CharField(max_length=120)
    sector_of_operation = models.CharField(max_length=120)
    type_of_organization =
    name_of_contact_person = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    contact_number1 = models.CharField(max_length=120)
    contact_numder2 = models.CharField(max_length=120)
    email_address = models.CharField(max_length=120)
    website = models.CharField(max_length=120)
    type_of_financing =
    primary_funding_agency1 = models.CharField(max_length=120)
    primary_funding_agency2 = models.CharField(max_length=120)
    primary_funding_agency3 = models.CharField(max_length=120)
    terms_and_conditions = models.TextField(max_length=380)
    purpose_for_financing = models.CharField(max_length=120)
    geographical_preference = models.CharField(max_length=120)
    funding_ceiling = models.IntegerField()
    fund_startups_or_ongoing =
    eligibility_criteria_of_SME = models.TextField(max_length=380)
    deadline_of_application = models.DateTimeField()

    def __str__(self):
        """
        Returns name of the business when called.
        """
        return self.organization_name
