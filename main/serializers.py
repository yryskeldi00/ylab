from decimal import Decimal

from rest_framework import serializers, status
from rest_framework.response import Response

from main.models import BankAccount


class BankAccountCreateSerializer(serializers.ModelSerializer):
    """
    BankAccount Create Serializer
    """

    class Meta:
        model = BankAccount
        fields = ('title', 'is_overdraft')


class BankAccountRetrieveSerializer(serializers.ModelSerializer):
    """
    BankAccount Retrieve Serializer
    """

    class Meta:
        model = BankAccount
        fields = ('money',)


class BankAccountUpdateSerializer(serializers.ModelSerializer):
    """
    BankAccount Update   Serializer
    """
    recipient = serializers.PrimaryKeyRelatedField(
        many=False, queryset=BankAccount.objects.all(), required=True,
        write_only=True,
    )

    class Meta:
        model = BankAccount
        fields = ('money', 'recipient',)

    def update(self, instance, validated_data):
        recipient = validated_data['recipient']
        money = validated_data['money']
        donor = instance
        return self.account_operation(donor, recipient, money)

    @staticmethod
    def account_operation(donor, recipient, money):
        donor_money = donor.money - money
        if recipient == donor:
            raise serializers.ValidationError(
                detail={'message': 'Вы не можете перевести деньги самому себе!'}
            )
        elif money <= 0:
            raise serializers.ValidationError(
                detail={'message': f'Неправильные данные! {money}'},
            )
        elif not donor.is_overdraft and donor_money < 0:
            raise serializers.ValidationError(
                {'message': f'У вас недостаточно средств для данной операции! {(donor_money)}'}
            )
        recipient.money += money
        recipient.save(update_fields=['money'])
        return recipient
