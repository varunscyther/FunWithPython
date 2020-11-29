"""
Some bank wants to implement a customer account management system that supports the following operations:

Deposit the client's account.
Withdraw money from the account.
Request account balance.
Make a money transfer between customer accounts.
To charge interest to all clients.
You need to implement such a system. Bank clients are identified by their names (unique string that does not contain spaces). Initially, the bank does not have any clients. As soon as a client makes a deposit, withdrawal or transfer of money, he gets a zero balance account. All further operations are carried out with this account only. The amount in the account can be either positive or negative, and is always an integer number.

Input format: The input contains a sequence of operations. The list of possible operations:

DEPOSIT name sum − deposit amount sum to name's account. If the client does not have an account, the account is created.
WITHDRAW name sum − withdraw amount sum from name's account. If the client does not have an account, the account is created.
BALANCE name − find out the balance of the client name.
TRANSFER name1 name2 sum − transfer amount sum from name1's account to name2's account. If any of the clients does not have an account, an account is created for them.
INCOME p − charge p% of the account's amount for all clients with open accounts. Interest is charged only to clients with a positive account balance, if the client has a negative balance, his balance does not change. After interest is accrued, the amount in the account remains integer, i.e. only an integer number of monetary units is accrued. The fractional part of the accrued interest is discarded.
The input ends with an empty line.

Output format: For each BALANCE request, the program must print the account balance of that customer. If the client with the requested name does not have a bank account, print ERROR

Possible tests :
Input data:
DEPOSIT Ivanov 100
INCOME 5
BALANCE Ivanov
TRANSFER Ivanov Petrov 50
WITHDRAW Petrov 100
BALANCE Petrov
BALANCE Sidorov


Program output:
105
-50
ERROR

-------------------------
Input data:
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 100
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 150
BALANCE Petrov
DEPOSIT Ivanov 10
DEPOSIT Petrov 15
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Ivanov 46
BALANCE Ivanov
BALANCE Petrov
DEPOSIT Petrov 14
BALANCE Ivanov
BALANCE Petrov


Program output:
ERROR
ERROR
100
ERROR
150
110
165
156
165
156
179
------------------------
Input data:
BALANCE a
BALANCE b
DEPOSIT a 100
BALANCE a
BALANCE b
WITHDRAW a 20
BALANCE a
BALANCE b
WITHDRAW b 78
BALANCE a
BALANCE b
WITHDRAW a 784
BALANCE a
BALANCE b
DEPOSIT b 849
BALANCE a
BALANCE b


Program output:
ERROR
ERROR
100
ERROR
80
ERROR
80
-78
-704
-78
-704
771
"""


def deposit() :
    existing_balance = account.get(raw_input[1])
    if existing_balance is not None :
        new_bal = existing_balance + int(raw_input[2])
        account[raw_input[1]] = new_bal
    else :
        account.setdefault(raw_input[1], int(raw_input[2]))


def withdraw() :
    existing_balance = account.get(raw_input[1])
    if existing_balance is not None :
        new_bal = existing_balance - int(raw_input[2])
        account[raw_input[1]] = new_bal
    else :
        account.setdefault(raw_input[1], 0 - int(raw_input[2]))


def balance() :
    if account.get(raw_input[1]) is None:
        print("ERROR")
    else:
        print(account.get(raw_input[1]))



def transfer() :
    existing_balance_sender = account.get(raw_input[1])
    if existing_balance_sender is not None :
        new_bal = existing_balance_sender - int(raw_input[3])
        account[raw_input[1]] = new_bal
    else :
        account.setdefault(raw_input[1], 0 - int(raw_input[3]))

    existing_balance_receiver = account.get(raw_input[2])
    if existing_balance_receiver is not None :
        new_bal = existing_balance_receiver + int(raw_input[3])
        account[raw_input[2]] = new_bal
    else :
        account.setdefault(raw_input[2], int(raw_input[3]))


def charge_interest() :
    for account_holder_name, bal in account.items() :
        if bal > 0 :
            bal += int(bal * int(raw_input[1]) / 100)
            account[account_holder_name] = bal


def invoke_transaction(x) :
    global raw_input
    raw_input = []
    raw_input = x.split()
    transaction_type = raw_input[0]
    if transaction_type == "BALANCE" :
        balance()
    elif transaction_type == "DEPOSIT" :
        deposit()
    elif transaction_type == "WITHDRAW" :
        withdraw()
    elif transaction_type == "INCOME" :
        charge_interest()
    elif transaction_type == "TRANSFER" :
        transfer()
    else :
        print("Unauthorized operation : " + transaction_type)


def collect_data() :
    global formatted_data, account
    account = {}
    user_data = []
    while True :
        line = input()
        if line :
            user_data.append(line)
        else :
            break
    formatted_data = "\n".join(user_data).split("\n")
    for x in formatted_data :
        invoke_transaction(x)


collect_data()
