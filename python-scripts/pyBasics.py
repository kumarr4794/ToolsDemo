# Author : Ravi Kumar

print("Hello-World!")

# Min in a day : Simple Math calculation.
print(20 * 24 * 60)

#String concat using str() and +
print("20 days " + str(50) + " minutes")

#String concat using f/format.
print(f"20 days {50} minutes")


# Variables
calculation_to_secs = 100 +  1
seconds = "seconds"
print(f"{calculation_to_secs} {seconds}")

'''
#Functions 
def days_to_units():
    print(f"{calculation_to_secs} {seconds}")
    print('From Function')

# Invoking functions
days_to_units()    


# Passing Parameters to functions.

def days_to_units(no_of_days):
    print(f"{calculation_to_secs} {no_of_days} {seconds}")
    print('From Function')

# Invoking functions
days_to_units(35)
days_to_units(35.4)


#Variables Scopes

def scope(no_of_days):
    return print(f"{calculation_to_secs}")
    print(no_of_days)

# To solve above scope problem create and use same variable in this func, too.
# no_of_days
scope(1)

# UserInput  / argparse , Always treated as string not number.
user_input = input("Hey User pleas input something here:\n")
print (user_input)
# return values from function

'''
# Conditionals if/else


def days_to_units(no_of_days):
    if no_of_days > 0:
        calculation_to_secs = 24
        return f"{no_of_days} days are {calculation_to_secs * no_of_days}"
    elif no_of_days == 0:
        return "0 is not accepted."
    else:
        return "Negative input"
   
user_input = input("Hey User pleas input something here:\n")

def validate_and_execute():
    if user_input.isdigit():  
        user_input_number = int(user_input) 
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print('Input is not valid number.') 

#try: 
#    except ValueError:   
    
# Try and catch / Error handling.
