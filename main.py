name_of_units = "hours"
calculate_to_hours = 24


def days_to_units(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days are {number_of_days * calculate_to_hours} {name_of_units}"
    elif number_of_days == 0:
        return "You entered a 0, please enter a valid positive number!"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("Your input is not a valid number!")


user_input = input("Hey user, enter a number of days and I will convert to hours!\n")
validate_and_execute()

