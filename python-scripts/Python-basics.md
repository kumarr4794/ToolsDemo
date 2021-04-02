# Python 

## Data Types

- Strings - string(str) , print(''/"") both are same.
- Integer - Whole no, print(1)
- Float - decimal places. print(2.3)  


# String Concatenation :  "+"
 Adding string and number.

print("20 days " + str(50) + " minutes")

Other way to write: using "f" format in statement instead of typecast str(int)

print(f"20 days {50} minutes")


# Variables

Used to store values, we dont have to specify data type before a variable.

Naming convention: If more than 2 words used "_"
eg: hello_world = something.

If a variable stores string -> a = "hello"
We can't use Reserved in naming the variables.

# Functions : Lets say we want to re-use some code block

**def** > to define a funtion name.
Ex :def days_to_units():
Indentation is required for functions. We have to invoke/call the function in order to execute code inside it.

# Passing Parameters to functions.

days_to_units(35.4)

# Variable scopes 

- global = A Variable is global if defined outside the function.
- local  = A Variables is local if defined inside the function.


# User Input program
input()
# return values from function
 use return in func , keyword to return something from function
# type() - returns datatype of variable.


# Conditionals , if/else
Example using Validation of user Input.

"=" - assign values, 
"==" - condition check.

# Try Catch 
  try: 
    if:
    elseif:
  except ValueError:


# While loops
 Runs until the statement/condition is true, if false exits the loop.


# Lists and For Loops 

    List operations : 
    CREATE : mylist = ["1", "2", "3"] -> index same as array 0,1,2
    REMOVE: mylist[0]
    ADD : mylist.append("4")

    -----------------------------
    Listname = ["1", "2", "3"]
    For = for <listElement> in <Listname>:
        Some condition here

 convert elements into list -> split() returns a list of values.
   USUAGE: var.split(",")

# Comments 