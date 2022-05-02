"""
Auther : Onjomba Felix
Github Link : github.com/developer-felix
Country : Kenya
Year of Experience : 3 years
Working Place : Freelancer
Email : onjombafelix1@gmail.com
"""

import uuid

from django.db import models

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'account'
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
