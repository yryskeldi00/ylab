from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main.models import BankAccount


class BankAccountTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        """Load initial data for the TestCase."""
        bank_account_1 = BankAccount.objects.create(title='user1', is_overdraft=True)
        bank_account_1.save()
        bank_account_2 = BankAccount.objects.create(title='user2', is_overdraft=False)
        bank_account_2.save()

    def test_bank_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('v1:create_bank_account')
        data = {'title': 'DabApps', 'is_overdraft': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_bank_account_retrieve(self):
        bank_account_id = BankAccount.objects.first().id
        url = reverse('v1:retrieve_bank_account', kwargs={'pk': bank_account_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bank_account_update(self):
        bank_account_is_overdraft = BankAccount.objects.get(id=1).id
        bank_account_id = BankAccount.objects.get(id=2).id
        url = reverse('v1:update_bank_account', kwargs={'pk': bank_account_is_overdraft})
        data = {'recipient': bank_account_id, 'money': 100}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bank_account_update_invalid_value(self):
        bank_account_is_overdraft = BankAccount.objects.get(id=1).id
        bank_account_id = BankAccount.objects.get(id=2).id
        url = reverse('v1:update_bank_account', kwargs={'pk': bank_account_id})
        data = {'recipient': bank_account_is_overdraft, 'money': 100}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
