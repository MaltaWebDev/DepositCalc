import json
from datetime import datetime, timedelta

# Set the minimum and maximum deposit limits
min_deposit = 10.00
max_deposit = 50000.00

# Set the minimum self-imposed deposit limit
min_limit = 10.00

# Read the deposit history from the JSON file
with open('dep_30d.json', 'r') as json_file:
    deposit_history = json.load(json_file)

# Prompt the user to input the weekly deposit limit
weekly_input = float(input("Enter the weekly deposit limit: "))

# if the weekly limit is 0, set it to the maximum deposit
if weekly_input == 0:
    weekly_limit = max_deposit
else:
    weekly_limit = weekly_input

print(weekly_limit)

# throw exception if the weekly limit is set but less than the minimum deposit or greater than the max
try:
    if weekly_limit > 0 and weekly_limit < min_limit:
        raise ValueError
    if weekly_limit > max_deposit:
        raise ValueError
except ValueError:
    print("The weekly limit must be between 10 and 500")
    exit()

print(f"The weekly limit is: {weekly_limit}")

def calc_next_three_weekly(weekly_limit, deposit_history):
    # Calculate the remaining limit
    remaining_limit = weekly_limit - sum([deposit['amount'] for deposit in deposit_history])
    # Calculate the next three available deposits
    next_three_deposits = []
    for i in range(3):
        # Calculate the next available deposit time and date
        next_deposit_time_and_date = datetime.now() + timedelta(days=i)
        # Add the next available deposit to the list
        next_three_deposits.append({'time_and_date': next_deposit_time_and_date.strftime('%Y-%m-%d %H:%M:%S'), 'amount': remaining_limit})
    # Print the remaining limit
    print(f"Remaining limit: {remaining_limit:.2f}")

    print(next_three_deposits)

    # Print the next three deposits 
    dep1 = next_three_deposits[0]['amount']
    dep1f2 = "{:.2f}".format(dep1)
    print(f"Next deposit is: {dep1f2} at {next_three_deposits[0]['time_and_date']}")

    dep2 = next_three_deposits[1]['amount']
    dep2f2 = "{:.2f}".format(dep2)
    print(f"Then: {dep2f2} at {next_three_deposits[1]['time_and_date']}")

    dep3 = next_three_deposits[2]['amount']
    dep3f2 = "{:.2f}".format(dep3)
    print(f"Then: {dep3f2} at {next_three_deposits[2]['time_and_date']}")

calc_next_three_weekly(weekly_limit, deposit_history)

# print(deposit_history)

# add up all the deposits in the deposit history
total_deposits = sum([deposit['amount'] for deposit in deposit_history])
print(f"Total deposits: {round(total_deposits, 2)}")