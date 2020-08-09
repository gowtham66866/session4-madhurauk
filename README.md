## Session 4 - Numeric Types II
Description of the classes and methods in session4.py and test_session4.py

### Qualean
Qualean class is inspired by Boolean+Quantum concepts. We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place

### __and__
This method implements the logical and gate for the user defined Qualean objects

### __or__
This method implements the logical and gate for the user defined Qualean objects

### __repr__
This method returns the representation of the Qualean object and the value it contains in a nicely formatted string.

### __str__
This method returns the str object of value of the Qualean object mentioned.

### __add__
This method overrides the basic implementation of addition + operator for the Qualean class. 

### __mul__
This method overrides the basic implementation of multiplication * operator for the Qualean class.

### __eq__
This method overrides the equality checking == for the user defined Qualean objects.

### get_number
This is the getter function to return the internal number stored by a Qualean object 

### __float__
This method returns the float conversion of the Qualean object.

### __ge___
This method overrides the greater than or equal to checking >= for the user defined Qualean objects.

### __gt__
This method overrides the greater than checking > for the user defined Qualean objects.

### __le__
This method overrides the lesser than or equal to checking <= for the user defined Qualean objects.

### __lt__
This method overrides the lesser than checking < for the user defined Qualean objects.

### __invertsign__
This method returns the opposite sign of value of the calling Qualean object.

### __bool__
This dunder method returns the bool value for the Qualean object.

### __sqrt__
This method implements the mathematical Square root operation on the Qualean object.  

## test_session4.py
It consists of all the test cases for the Qualean class 

### test_indentations
Test case to check the indentation of the session4.py file.

### test_and_when_q2_not_defined
Test case to check q1 and q2 returns False when q2 is not defined as well and q1 is False

### test_and_functionality
Test case to check the logical and operation of the two Qualean objects.

### test_or_when_q2_not_defined
Test case to check q1 or q2 returns True when q2 is not defined as well and q1 is not false

### test_or_functionality
Test case to check the logical or operation of the two Qualean objects.

### test_repr
Test case to check the object representation (__repr__) of the Qualean object.

### test_str
Test case to check the string representation (__str__) of the Qualean object.

### test_add_mul
Test case to check q + q + q ... 100 times = 100 * q

### test_ge
Test case to check the greater than or equal to (__ge__) comparison of the two Qualean objects.

### test_all_functions_exist
Test case to check that code contains all the required functions

### test_readme_exists
Test case to check if the README.md file exists or not in the repo.

### test_readme_contents
Test case to check the contents of the README.md file and also checks if the file consists of atleast 500 words.

### test_readme_proper_description
Test case to cross check if the README.md file contains proper description of modules.

### test_readme_file_for_formatting
Test case to check the proper formatting of the README.md file.