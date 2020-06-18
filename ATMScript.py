'''
Andrew Vue
SNHU
IT140 20EW3
ATM Script
'''


import sys

#account balance
account_balance = float(500.25)


#<--------functions go here-------------------->
#printbalance function
def balance():
  global account_balance
  print("Your current balance: \n" + str(account_balance))
  return account_balance #This updates the balance for the other transactions

#deposit function
def deposit (amount):
  global account_balance
  account_balance += float(amount)
  print("Deposit was $%.2f, current balance is $%.2f" %(amount, account_balance))
  return balance()#This updates the balance from deposits

#withdraw function
def withdraw(amount):
  global account_balance
  if float(amount) > account_balance:
    print("$" + str('%.2f' % float(amount)) + "is greater than your account balance of $" + str(account_balance))
  else:
    account_balance -= float(amount)
    print("Withdrawal amount was $" + str('%.2f' % float(amount)) + ", current balance is $" + str('%.2f' % float(account_balance)))
  return balance()#This updates the balance from deposits

#This creates a quit function to exit the interaction
def quit():
    quit
    print("Thank you for banking with us today.")


##Not sure what to call this function
user_choice = input("What would you like to do?\n" "Type 'B' for Balance, 'D' for deposit, 'W' for withdrawal, 'Q' to quit.\n")

##User Input goes here, use if/else conditional statement to call function based on user input
#Created a while loop so that the user can do more than 1 transaction
while user_choice != 'Q':
  user_choice = input("What would you like to do?\n")

  if user_choice == 'D':
    deposit_amount = float(input("How much would you like to deposit?\n"))
    deposit(deposit_amount)
  elif user_choice == 'W':
    withdrawal_amount = float(input("How much would you like to withdraw?\n"))
    withdraw(withdrawal_amount)
  elif user_choice == 'B':
    balance()
  elif user_choice == 'Q':
    quit()


'''
options = {
  'B': balance,
  'b': balance,
  'W': withdraw,
  'w': withdraw,
  'D': deposit,
  'd': deposit,
  'Q': quit,
  'q': quit,
}

options[user_choice]()

if userchoice == D:
    deposit_amount = input("How much would you like to deposit today?")
    print("Deposit was" +str(deposit_amount) +"," + (account_balance + deposit_amount)

if userchoice == B:
    account_balance = 500.25
    print("Your current balance: \n" + str(account_balance))

if userchoice == W:
    withdraw()
'''
