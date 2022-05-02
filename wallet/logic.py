from .models import Account

#Creating Business Logic Here

#Create X amount to users one of the account.
def deposit_x_ammount_to_one_account(user_id,account_id,ammount):
    try:
        user_wallet = Account.objects.get(user_id=user_id)
        user_wallet.balance += ammount
        user_wallet.save()
        return True
    except:
        return False

# Debit X amount from users one of the account.
def debit_x_ammount_from_one_account(user_id,account_id,ammount):
    try:
        user_wallet = Account.objects.get(user_id=user_id)
        user_wallet.balance -= ammount
        user_wallet.save()
        return True
    except:
        return False

#Transfer money from one account to another account for a single user.
def transfer_x_ammount_from_one_account_to_another_account(user_id,from_account_id,to_account_id,ammount):
    try:
        debit_x_ammount_from_one_account(user_id,from_account_id,ammount)
        deposit_x_ammount_to_one_account(user_id,to_account_id,ammount)
        return True
    except:
        return False

# Transfer money from one account of user to another account of another user.
def transfer_x_ammount_from_one_account_to_another_account_of_another_user(user_id,from_account_id,to_user_id,to_account_id,ammount):
    try:
        debit_x_ammount_from_one_account(user_id,from_account_id,ammount)
        deposit_x_ammount_to_one_account(to_user_id,to_account_id,ammount)
        return True
    except:
        return False

#Get balance for a user.
def get_balance_for_a_user(user_id):
    try:
        user_wallet = Account.objects.get(user_id=user_id)
        return user_wallet.balance
    except:
        return False

#  Get balance for an account of a user.
def get_balance_for_an_account_of_a_user(user_id,account_id):
    try:
        user_wallet = Account.objects.get(user_id=user_id)
        return user_wallet.balance
    except:
        return False