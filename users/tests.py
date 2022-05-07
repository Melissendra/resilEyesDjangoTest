from django.test import TestCase
from .models import User


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Test the user's creation """
        test_create_user = User.objects.create(
            firstname='Jean',
            lastname='Marchand',
            email='test@test.fr',
            phone_number='01 02 03 04 05',
            birthday_date='1980-05-29'
        )
        test_create_user.save()

    def test_user_data(self):
        user = User.objects.get(id=1)
        firstname = f'{user.firstname}'
        lastname = f'{user.lastname}'
        email = f'{user.email}'
        phone_number = f'{user.phone_number}'
        birthday_date = f'{user.birthday_date}'
        self.assertEqual(firstname, 'Jean')
        self.assertEqual(lastname, 'Marchand')
        self.assertEqual(email, 'test@test.fr')
        self.assertEqual(phone_number, '01 02 03 04 05')
        self.assertEqual(birthday_date, '1980-05-29')

