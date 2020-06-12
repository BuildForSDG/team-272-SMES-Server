from django.db import models

from user.models import CustomUser
from model_utils import Choices
# Create your models here.

# funder model


class Funder(CustomUser):

    # choices for choice fields
    ORGTYPES = Choices(
        ('Goverment', ('Goverment organization')),
        ('Non-Goverment', ('Non-Goverment organization')),
        ('private', ('private organization')),
        ('international', ('international organization')),
    )

    FINTYPES = Choices(
        ('Credit', ('Credit financing')),
        ('Grant', ('Grant financing')),
        ('In Kind', ('In Kind financing')),
        ('Research', ('Researc financing')),
    )

    FUNDCHOICE = Choices(
        ('Startup Projects', ('Startup projects')),
        ('Ongoing Projects', ('Ongoing projects')),
        ('all', ('all projects types')),
    )

    organization_name = models.CharField(max_length=120)
    sector_of_operation = models.CharField(max_length=120)
    type_of_organization = models.CharField(
        max_length=120,
        choices=ORGTYPES,
        default=ORGTYPES.private,
    )
    name_of_contact_person = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    contact_number1 = models.CharField(max_length=120)
    contact_numder2 = models.CharField(max_length=120)
    email_address = models.CharField(max_length=120)
    website = models.CharField(max_length=120)
    type_of_financing = models.CharField(
        max_length=120,
        choices=FINTYPES,
        default=FINTYPES.Grant,
    )
    primary_funding_agency1 = models.CharField(max_length=120)
    primary_funding_agency2 = models.CharField(max_length=120)
    primary_funding_agency3 = models.CharField(max_length=120)
    terms_and_conditions = models.TextField(max_length=380)
    purpose_for_financing = models.CharField(max_length=120)
    geographical_preference = models.CharField(max_length=120)
    funding_ceiling = models.IntegerField()
    fund_startups_or_ongoing = models.CharField(
        max_length=120,
        choices=FUNDCHOICE,
        default=FUNDCHOICE.all,
    )
    eligibility_criteria_of_SME = models.TextField(max_length=380)
    deadline_of_application = models.DateTimeField()

    def __str__(self):
        """
        Returns name of the business when called.
        """
        return self.organization_name
