# Password checker

from curses.ascii import islower


print('This program tests a string to validate if it would be a good password\n')

# Request password candidate from the user

pass_to_test = input('Please provide a password to be tested: ')

# Check for password conditions:
# no new-line allowed
# no white-space allowed
# no tabs allowed
# minimum 1 small letter
# minimum 1 large letter
# minimum 1 special character
# minimum 8 characters

error_list = ""
num_chars = 0
num_upper = 0
num_lower = 0
num_spec = 0

for c in pass_to_test:
    num_chars += 1
    if c == "\n" or c == "\r":
        error_list = error_list + "Your password should be just one line\n"
    elif c == " ":
        error_list = error_list + "Please remove white space from position " + str(num_chars) + "\n"
    elif c == "\t":
        error_list = error_list + "Please remove tabulation from position " + str(num_chars) + "\n"
    elif c.isupper():
        num_upper += 1
    elif c.islower():
        num_lower += 1
    elif c in "!@#$%^&*()-_=+:;\\[]\{\}\"'?/>.<,":
        num_spec += 1

if num_chars < 8:
    error_list = error_list + "Your password should be at least 8 characters \n"

if num_upper == 0:
    error_list = error_list + "Your password should contain at least one capital letter \n"

if num_lower == 0:
    error_list = error_list + "Your password should contain at least one lower-case letter \n"

if num_spec == 0:
    error_list = error_list + "Your password should contain at least one special character \n"

if error_list == "":
    print("Congratulations! The password", pass_to_test, "is strong.")
else:
    print(error_list)

