from django.test import TestCase

from .models import Funder
from .serializers import FunderSerializer, FunderCreateUserSerializer

class FunderSerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Funder.objects.create_user(username='Test_funder', name_of_contact_person='Test_funder_contact', name_of_business='Test_funder_business', phone=+25612345667, email='testfunderemail@test.com', password='test12345678')

    def test_user_name(self):
        funder = Funder.objects.get(id=1)
        expected_object_name = f'{funder.username}'
        self.assertEquals(expected_object_name, 'Test_funder')
    
