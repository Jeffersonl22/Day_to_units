def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{number_of_days} days are {number_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        # We want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number!")
        else:
            print("You entered a negative number, no conversion for you!")
    except ValueError:
        print("Your input is not a valid number!")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and conversion unit separate by :\n"
                       "(You can also tap exit for end the program)\n")
    if user_input == "exit":
        print("Thanks for using this program!")
        break
    else:
        days_and_unit = user_input.split(":")
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_execute()
