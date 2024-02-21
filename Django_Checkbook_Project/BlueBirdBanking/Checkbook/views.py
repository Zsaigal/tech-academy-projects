from django.shortcuts import render, redirect, get_object_or_404  # Import necessary functions
from .forms import AccountForm, TransactionForm  # Import form classes
from .models import Account, Transaction  # Import models


# Define the view for the home page
def home(request):
    # Create a TransactionForm instance with POST data if available
    form = TransactionForm(data=request.POST or None)

    # Check if the request method is POST
    if request.method == 'POST':
        # If it's a POST request, extract the 'account' field from the form data
        pk = request.POST['account']
        # Redirect to the 'balance' view with the extracted 'pk'
        return balance(request, pk)

    # If it's not a POST request, render the home page template with the form
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


# Define the view for creating a new account
def create_account(request):
    # Create an AccountForm instance with POST data if available
    form = AccountForm(request.POST or None)

    # Check if the request method is POST
    if request.method == 'POST':
        # If it's a POST request and the form is valid, save the form and redirect to the home page
        if form.is_valid():
            form.save()
            return redirect('index')

    # If it's not a POST request or the form is not valid, render the account creation template with the form
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)


# Define the view for displaying account balance
def balance(request, pk):
    # Retrieve the account object with the given pk from the database or return a 404 error if not found
    account = get_object_or_404(Account, pk=pk)

    # Retrieve all transactions related to the account
    transactions = Transaction.Transactions.filter(account=account)

    # Initialize current total balance with the initial deposit of the account
    current_total = account.initial_deposit

    # Create a dictionary to store transaction details and their corresponding balances
    table_contents = {}

    # Iterate through each transaction
    for t in transactions:
        # Update the current total balance based on the transaction type and amount
        if t.type == 'Deposit':
            current_total += t.amount
        else:
            current_total -= t.amount
        # Update the table_contents dictionary with the transaction and its corresponding balance
        table_contents[t] = current_total

    # Prepare data to be passed to the template for rendering
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}

    # Render the balance sheet template with the data
    return render(request, 'checkbook/BalanceSheet.html', content)


# Define the view for adding a transaction
def transaction(request):
    # Create a TransactionForm instance with POST data if available
    form = TransactionForm(request.POST or None)

    # Check if the request method is POST
    if request.method == 'POST':
        # If it's a POST request and the form is valid, save the form and redirect to the balance view
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)

    # If it's not a POST request or the form is not valid, render the transaction addition template with the form
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
