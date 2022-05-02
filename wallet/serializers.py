from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'user', 'balance')

        def save(self):
            account = Account.objects.create(
                user = self.validated_data['user'],
                balance = self.validated_data['balance']
            )
            return account