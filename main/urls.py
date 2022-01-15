from django.urls import path

from main.views import (
    BankAccountUpdateAPIView, BankAccountCreateAPIView, BankAccountRetrieveAPIViewAPIView,
)

urlpatterns = [
    path('create-bank_account/', BankAccountCreateAPIView.as_view(), name='create_bank_account'),
    path('retrieve-bank_account/<int:pk>', BankAccountRetrieveAPIViewAPIView.as_view(), name='retrieve_bank_account'),
    path('update-bank_account/<int:pk>', BankAccountUpdateAPIView.as_view(), name='update_bank_account'),
]
