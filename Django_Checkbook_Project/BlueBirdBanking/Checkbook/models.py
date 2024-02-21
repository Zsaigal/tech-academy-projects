from django.db import models


# Define the Account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)  # Field to store the first name of the account holder
    last_name = models.CharField(max_length=50)  # Field to store the last name of the account holder
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)  # Field to store the initial deposit amount

    Accounts = models.Manager()  # Manager to handle Account objects

    # String representation of the Account object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Define choices for Transaction types
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# Define the Transaction model
class Transaction(models.Model):
    date = models.DateField()  # Field to store the date of the transaction
    type = models.CharField(max_length=10,
                            choices=TransactionTypes)  # Field to store the type of transaction (Deposit or Withdrawal)
    amount = models.DecimalField(max_digits=15, decimal_places=2)  # Field to store the amount of the transaction
    description = models.CharField(max_length=100)  # Field to store the description of the transaction
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE)  # ForeignKey relationship with Account model, each
    # transaction belongs to an account

    Transactions = models.Manager()  # Manager to handle Transaction objects
