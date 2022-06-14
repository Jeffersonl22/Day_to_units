name_of_units = "hours"
calculate_to_hours = 24


def days_to_units(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculate_to_hours} {name_of_units}"


def validate_and_execute():
    try:
        user_input_number = int(number_of_days_element)

        # We want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days as a comma separated list and I will convert to hours! \n ("
                       "or enter exit for stop the program)\n")
    list_of_days = user_input.split(", ")
    for number_of_days_element in set(list_of_days):
        validate_and_execute()
