# hard code the maximum deposit as per pmts
max_deposit = 50000.00
# minimum deposit is almost always 10.00
min_deposit = 10.00

def get_limit_input(prompt):
    while True:
        # convert input to float and throw exception if not a number
        try:
            daily_input = float(input(prompt))
        except ValueError:
            print("Please enter a number")
            continue
        # no negative numbers either
        if daily_input < 0:
            print(f"Please enter a positive number, minimum {min_deposit}")
        # no point setting a limit less than the minimum deposit
        elif daily_input > 0 and daily_input < min_deposit:
            print(f"The minimum is {min_deposit}")
        # valid input
        elif daily_input >= min_deposit and daily_input <= max_deposit:
            return daily_input
        # setting a limit is not mandatory
        elif daily_input == 0 or daily_input == "":
            return None

# prompt for user input
daily_limit = get_limit_input("Enter the daily deposit limit: ")
weekly_limit = get_limit_input("Enter the weekly deposit limit: ")
monthly_limit = get_limit_input("Enter the monthly deposit limit: ")

print(daily_limit, weekly_limit, monthly_limit)