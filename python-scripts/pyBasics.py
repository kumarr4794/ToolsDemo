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
'''

# Passing Parameters to functions.

def days_to_units(no_of_days):
    print(f"{calculation_to_secs} {no_of_days} {seconds}")
    print('From Function')

# Invoking functions
days_to_units(35)
days_to_units(35.4)