from django.test import TestCase

from .models import SME
# from .serializers import SMESerializer, SMECreateUserSerializer

class SMESerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        SME.objects.create_user(username='Test_user', name_of_contact_person='Test_contact', name_of_business='Test_business', phone=+25612345667, email='testemail@test.com', password='test12345678')

    def test_user_name(self):
        sme = SME.objects.get(id=1)
        expected_object_name = f'{sme.username}'
        self.assertEquals(expected_object_name, 'Test_user')