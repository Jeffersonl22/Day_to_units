name_of_units = "hours"
calculate_to_hours = 24


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculate_to_hours} {name_of_units}"


def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number!")


user_input = input("Hey user, enter a number of days and I will convert to hours!\n")
validate_and_execute()
