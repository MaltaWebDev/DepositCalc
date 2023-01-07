import json
import random
from datetime import datetime, timedelta

# Set the minimum and maximum deposit amounts
min_deposit = 10.00
max_deposit = 500

# Generate the deposit history
deposit_history = []
for i in range(20):
    # Generate a random deposit amount
    amount = round(random.uniform(min_deposit, max_deposit), 2)
    # Calculate a random time and date within the last 30 days
    time_and_date = datetime.now() - timedelta(days=random.randint(0, 29))
    # Add the deposit to the deposit history
    deposit_history.append({'time_and_date': time_and_date.strftime('%Y-%m-%d %H:%M:%S'), 'amount': amount})

# Convert the deposit history to JSON
deposit_history_json = json.dumps(deposit_history)

# Print the JSON data
print(deposit_history_json)

# Output the JSON data to a file
with open('./dep_30d.json', 'w') as json_file:
    json_file.write(deposit_history_json)