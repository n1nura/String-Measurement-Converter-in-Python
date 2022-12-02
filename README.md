<h1>String and Unit Measurement Converter in Python</h1>

### Introduction
<br>
For this assessment it was required to design and produce software that met certain functionality requirements (addressed in the 'Module Descriptions' section) using basic concepts of Software Engineering.
The production code for this software was implemented using Python and allows the user to multiple String and Measurement conversions.

All functionalities from Category 1:
>a. Converting a given string to upper case or lower case.<br>
b. Identify whether numeric values are in a given string.<br>
c. Identify whether a given string is a valid number or not.<br>
d. Remove any numeric values in a given string and then convert the string to upper
case or lower Case.

and the following functionality from Category 2:
>a. Converting a number which represents a length given in meters to feet and vice
versa and centimeter to inches and vice versa.

were implemented.

This report covers the descriptions of each module in the software, assumptions made when designing the modules, a guide on how to use the production code, a checklist of Modularity guidelines that was to be followed in developing the production code and the results of reviewing the production code against the checklist.

Several test designs for both Black-Box testing and White-box testing that were used to test the production code are also included. Furthermore, there is a record of each test run for each module along with the test cases written for each one.

There is a small description on how to run the test code and the results of the tests with a small discussion for each result.

Finally, there is a discussion about the use of Version Control during this project as well as a discussion on Ethics and a discussion about this work itself.


<div style="page-break-after: always;"></div>

### Module Descriptions


| Name                       | Description                                                                                                          | Behaviour                                                                                                                                                                                                                                            | Input Method          | Output Method         |
|----------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|-----------------------|
| Convert Case               | Converts a given string to upper case or lower case                                                                  | Takes user input. Asks the user if upper case or lower case is needed. Converts the given string using in-built python function. Outputs converted function and asks user if storage in a file is necessary. If the user selects yes, store in file. | Keyboard Input / File | Console Output / File |
| Identify Numeric Values    | Identifies whether numeric values are in a given string                                                              | Takes user input. Identifies any numeric values in a given string. Confirms if or not numeric values found                                                                                                                                           | Keyboard Input / File | Console Output        |
| Check Valid Number         | Identifies whether a number in a given string is valid or not within a range of -1000 to 1000                        | Takes user input. Checks validity of number against pre-defined conditions. Outputs "Valid"/"Invalid" depending on the outcome.                                                                                                                      | Keyboard Input / File | Console Output        |
| Remove Number Convert Case | Identifies and removes numeric values in a given string and also converts the remaining string into upper/lower case | Uses functionality from previous modules to take user input, remove numeric values and convert the case. Then outputs converted string based on user requirement.                                                                                    | Keyboard / File       | Console Output / File |
| Convert Measuring Unit     | Converts meters to feet and vice versa, and centimeters to inches and vice versa.                                    | Takes user input, and converts to required unit via unit conversion formulae. Outputs value to console and also saves in file                                                                                                                        | Keyboard Input / File | Console Output / File |
| Input Handler              | Handles user input for other modules                                                                                 | Asks user if input will be manual or from file. If from user takes console input. If from file, reads from file                                                                                                                                      | Keyboard              |                       |
| Output Handler             | Handles user output from other modules                                                                               | Outputs values returned from functions onto text file.                                                                                                                                                                                               |                       | File                  |

Each functionality required was considered as a separate module for ease of implementation and testing. Along with modules for handling user input and saving an output to a file.
It was assumed that identifying the existence of numeric values in a string and checking if a given number was valid would not provide an output that was important to save to a file.
For checking the validity of a number a range between -1000 and 1000 was considered.

<div style="page-break-after: always;"></div>

### Modularity

<br>

#### Production Code Guide

Once the production code begins execution the user will be shown the following:

![screenshot of production code's start](.\screenshots\prodcodestart.PNG)

The user must type "1" and Press Enter for String Conversions or type "2" and Press Enter for Measurement Conversions.
If the user opts for String Conversions they will be shown the options below.

![screenshot of string conversion choices](.\screenshots\StringConversionOptions.png)

As before the user must type a value between "1-4" and press Enter.

Once they select an operation. They would be presented the option to input values/data manually or to take data from a predetermined file.

![screenshot of sample operation](.\screenshots\InputChoice.png)

Once the user determines and enters an input, the operation will be carried out. With the output of each operation either being a console output or saved to a file. (This is described in detail under Module Descriptions.)

*InputFile.txt must be edited by the user before importing values from the file if a specific value is required to be used*

<br>

#### Checklist
Reduce Degree of Coupling
- Calls (Function calling another function, uses parameters and return values. Lower the number of parameters)
- Use of Global Variables (Increases complexity. Remove Global Variables.)
- Control Flags (Using Boolean parameters. Must be removed.)

Increase Cohesiveness
- Increase the extent to which each module by does single well-defined task.
- Sequential Tasks (Add unnecessary complexity to a function with unrelated tasks within it. Split into individual functions)
- Consider relatedness of tasks (Do they use the same data, are executed parallely)
- Consider if distinct parts of function use different data.(Different concepts)

Reduce Redundancy
- Code should not be doing what other code already does.
- Reuse code
- Add common code to its own function

<br>

#### Code Review Results

Functions are called by other functions such as RemoveNum, FindNum calling InputHandler. However, there is a very amount of parameters being used.
There are no global variables. Values are returned from functions which use local variables for their tasks.
There are no boolean parameters being passed for functions. These factors reduce the coupling within the production code.

Each function (InputHandler, OutputHandler, RemoveNum, ConvertCase, etc.) has a specific task to accomplish. Concepts such as converting a string to uppercase for instance is an entirely separate function from identifying numbers in a string.
While there is some relativity among the functions as they all take some sort of user input and perform an operation on the data.

The InputHandler is called multiple times by multiple functions. This serves to reduce redundancy in code as multiple copies of code to take input is unnecessary duplication.
While this does increase the coupling slightly it cannot be avoided. If more modules and functions were to be added, it would be better to
Having a separate function to handle input also increase cohesiveness.

RemoveNum calls ConvertCase instead of duplicating the code, also to reduce redundancy.

<div style="page-break-after: always;"></div>

### Test Designs
<br>

#### Black-Box Testing

Submodule: Convert Case<br>
Method: Equivalence Partitioning<br>
Imports: n(string)

| Category                                      | Test Data                 | Expected Result                                       |
|-----------------------------------------------|---------------------------|-------------------------------------------------------|
| n only has letters                            | Kanakaratne               | kanakaratne / KANAKARATNE                             |
| n has letters and numbers                     | aBc9488                   | abc9488 / ABC9488                                     |
| n only has numbers                            | 9488                      | Error                                                 |
 | n only has special characters (!,?,etc)       | !                         | Error                                                 |
 | n has letters and special characters          | Ninura B.D.S. Kanakaratne | ninura b.d.s. kanakaratne / NINURA B.D.S. KANAKARATNE |
| n has letters, numbers and special characters | 2001: A Space Odyssey     | 2001: a space odyssey /  2001: A SPACE ODYSSEY        |

<br>

Submodule: FindNum<br>
Method: Equivalence Partitioning<br>
Imports: n(string)

| Category                                      | Test Data                 | Expected Result |
|-----------------------------------------------|---------------------------|-----------------|
| n only has letters                            | Kanakaratne               | False           |
| n has letters and numbers                     | aBc9488                   | True            |
| n only has numbers                            | 9488                      | True            |
| n only has special characters (!,?,etc)       | !                         | False           |
| n has letters and special characters          | Ninura B.D.S. Kanakaratne | False           |
| n has letters, numbers and special characters | 2001: A Space Odyssey     | True            |

<br>

Submodule: CheckValidNum<br>
Method: Boundary Value Analysis and Equivalence Partitioning<br>
Imports: n(string)

| Category                                      | Test Data                 | Expected Result                 |
|-----------------------------------------------|---------------------------|---------------------------------|
| n only has letters                            | Kanakaratne               | False                           |
| n has letters and numbers                     | aBc9488                   | False                           |
| n only has numbers                            | 400, 9488                 | True, False (Invalid Partition) |
| n only has special characters (!,?,etc)       | !                         | False                           |
| n has letters and special characters          | Ninura B.D.S. Kanakaratne | False                           |
| n has letters, numbers and special characters | 2001: A Space Odyssey     | False                           |

Boundary Value Analysis

| Invalid Test Cases | Valid Test Cases   | Invalid Test Cases |
|--------------------|--------------------|--------------------|
| -1001, -1000.1     | -1000, 50.84, 1000 | 1000.1, 1001       |

<br>

Submodule: RemoveNum<br>
Method: Equivalence Partitioning<br>
Imports: n(string)

| Category                                      | Test Data                 | Expected Result                                       |
|-----------------------------------------------|---------------------------|-------------------------------------------------------|
| n only has letters                            | Kanakaratne               | kanakaratne / KANAKARATNE                             |
| n has letters and numbers                     | aBc9488                   | abc / ABC                                             |
| n only has numbers                            | 9488                      | Error                                                 |
| n only has special characters (!,?,etc)       | !                         | Error                                                 |
| n has letters and special characters          | Ninura B.D.S. Kanakaratne | ninura b.d.s. kanakaratne / NINURA B.D.S. KANAKARATNE |
| n has letters, numbers and special characters | 2001: A Space Odyssey     | : a space odyssey /  : A SPACE ODYSSEY                |

<br>

Submodule: ConvertMeasureUnit<br>
Method: Equivalence Partitioning<br>
Imports: n(string)

| Category                                      | Test Data                 | Expected Result                              |
|-----------------------------------------------|---------------------------|----------------------------------------------|
| n only has letters                            | Kanakaratne               | Error                                        |
| n has letters and numbers                     | aBc9488                   | Error                                        |
| n only has numbers                            | 9488                      | 31130.128 / 2891.801 (Depends on conversion) |
| n only has special characters (!,?,etc)       | !                         | Error                                        |
| n has letters and special characters          | Ninura B.D.S. Kanakaratne | Error                                        |
| n has letters, numbers and special characters | 2001: A Space Odyssey     | Error                                        |

<br>

#### White-Box Testing

Module: CheckValidNum

| Path                                         | Test Case     | Expected Result          |
|----------------------------------------------|---------------|--------------------------|
| Enter 'while' loop and goto 'if'             | input: 9488   | output: "Valid Number"   |
| Enter 'while' loop skip 'if' and goto 'else' | input: Ab9488 | output: "Invalid Number" |
| Skip 'while' loop                            | input: -1500  | output: "Invalid Value"  |  
<br>

Module: FindNum

| Path                    | Test Case              | Expected Result                                    |
|-------------------------|------------------------|----------------------------------------------------|
| Enter 'if'              | input: Kanakaratne9488 | Output: "String contains numerical values"         |
| Skip 'if', Enter 'else' | input: Kanakaratne     | Output: "String does not contain numerical values" |

<div style="page-break-after: always;"></div>

### Test Implementation

| Module name             | BB test design(EP) | BB test design (BVA) | WB test design | EP test code(run) | BVA test code(run) | White-Box testing(run) |
|-------------------------|--------------------|----------------------|----------------|-------------------|--------------------|------------------------|
| Convert Case            | done               | not done             | not done       | done              | not done           | not done               |
| Identify Numeric Values | done               | not done             | done           | done              | not done           | not done               |
| Check Valid Number      | done               | done                 | done           | done              | done               | not done               |
| Remove Number           | done               | not done             | not done       | done              | done               | not done               |
| Convert Measuring Unit  | done               | not done             | not done       | done              | not done           | not done               |

#### Test Code Guide

Each module was given a Test version so that the test cases could be implemented. Since unittest was not used when testing these modules, each test case category was written manually.


![screenshot of production code's start](.\screenshots\TestConvertMeasureCode.PNG)

Changing the parameters being passed by the functions we can test if the desired output is received via the terminal.
If there are no assertion errors raised by the test code or any errors from the production code we assume that it has passed testing.

![screenshot of production code's start](.\screenshots\TestConvertMeasureResults.PNG)

<br>

#### Testing Review

This method of testing is not optimal and for each error the code will stop execution.

Testing revealed errors in modules such as "FindNum" where the range of values was incorrectly implemented and was fixed. After running the test again the issue was resolved.
There is also an error in "ConvertCase", if a special character is passed (!,.?) it will still complete execution. This was not fixed.

<div style="page-break-after: always;"></div>

