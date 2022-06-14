name_of_units = "hours"
calculate_to_hours = 24


def days_to_units(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculate_to_hours} {name_of_units}"
    elif number_of_days == 0:
        return "You entered a 0, please enter a valid positive number!"
    else:
        return "You entered a negative value, so no conversion for you"


user_input = input("Hey user, enter a number of days and I will convert to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)
