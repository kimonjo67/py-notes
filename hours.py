# Employees houry pay rate function
# PseudoCode
# Input total hours
# Conditional statement if the hours are more than 80
# Print error message and restart program
# Conditional statement if hours are over 40 hours
# Input basic pay rate
# Input overtime rate
# Compute how many hours are overtime ==> hours - 40 and save in variable called overTime_hours
# Compute basic hours = hours - overtime and save in normal-hours variable
# Compute ovetime pay = overtime-rates * overtime hours
# Print overtime pay + normal pay to get total pay
# print total pay for hours under 40 hours.

def employeePay():
    hours = int(input("Please Enter total hours worked: "))
    if hours > 80:
        print("Invalid input, Please enter Hours between 0 - 80")
    elif hours > 40:
        normal_rates = float(input("Enter your basic hourly rate: "))
        normal_pay = normal_rates * hours
        overTime_hours = hours - 40
        overTime_rates = float(input("Enter Overtime rates: "))
        overTime_pay = overTime_rates * overTime_hours
        normal_pay = normal_rates * (hours - overTime_hours)
        total_pay = normal_pay + overTime_pay
        print("First 40 hours at ", normal_rates, "per hour "," And the next 40 hours at: ", overTime_rates,"per hour", "Total Pay is: ", total_pay)

    elif hours <= 40:
        normal_rates = float(input("Enter your hourly rate: "))
        normal_pay = normal_rates * hours
        print(hours, " Hours at",normal_rates, " per hour "," Total Pay: ", normal_pay)
employeePay()