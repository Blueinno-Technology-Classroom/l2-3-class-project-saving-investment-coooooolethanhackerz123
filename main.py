##################################################
'''
Q1: 
'''

# TODO: Write your code here
current_balance = 0
interest_rate= 0.065
interest = 0
deposit = 100
new_balance = 1000

for i in range(25):
    current_balance = new_balance
    interest = interest_rate * new_balance 
    new_balance = current_balance + interest
    print(f'{i+1:02}:current_balance:{current_balance:.2f}, interest:{interest},deposit:{deposit}, new_balance:{new_balance:.2f}')
    if i > 0:
        new_balance += deposit
##################################################
'''
Q2:
'''

# TODO: Write your code here

##################################################
'''
Q3:
'''

# TODO: Write your code here

##################################################
'''
Q4:
'''

# TODO: Write your code here

##################################################
'''
Q5:
'''

# TODO: Write your code here

##################################################
'''
Q6:
'''

# TODO: Write your code here

##################################################
