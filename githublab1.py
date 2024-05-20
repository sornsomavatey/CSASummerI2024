# Prompt user to enter the minutes (e.g., 1 billion), and displays the number of years and days for the minutes. 
# Sample run:
# Enter the number of minutes:  1000000000
# 1000000000 minutes is approximately 1902 years and 214 days
minute = eval(input("Enter the minutes: "))
total_days = minute // (60*24)
years = total_days // 365
remaining_days = total_days % 365
print(f"{minute} minutes is approximately {years} years and {remaining_days} days")

