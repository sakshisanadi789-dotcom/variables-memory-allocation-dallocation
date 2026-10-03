# Python Operators and Function Logic (1 to 10)

This file explains the basic logic of Python operators and functions step by step.

## 1. Arithmetic operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo / remainder | `10 % 3` | `1` |

These operators help us calculate values quickly in Python.

## 2. Remainder operator `%`

The `%` operator gives the remainder left after division.

Example:

- `10 % 3 = 1`
- because `10 = 3 * 3 + 1`

This operator is very useful to check divisibility.

If the remainder is `0`, then the number is divisible by the other number.

Example:

- `12 % 3 == 0` means 12 is divisible by 3.
- `13 % 3 == 1` means 13 is not divisible by 3.

## 3. Comparison operators like `>=`

Comparison operators are used to compare two values.

Examples:

- `>` means greater than
- `<` means less than
- `>=` means greater than or equal to
- `<=` means less than or equal to
- `==` means equal to

Example:

```python
marks >= 75
```

This condition is true when the marks are 75 or greater.

## 4. Decision-making with `if`

The `if` statement checks whether a condition is true or false.

```python
if marks >= 75:
    print("Distinction")
```

If the condition is true, the code inside the block runs. Otherwise, Python skips it.

This is called decision-making in programming.

## 5. Function concept

A function is a reusable block of code that performs a specific task.

Example:

```python
def check_number(number):
    print(number)
```

This function takes a value called `number`, and then works with it.

Functions help us write code once and use it many times.

## 6. Function: `check_number(number)`

```python
def check_number(number):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

    print("Divisible by 3:", number % 3 == 0)
    print("Divisible by 5:", number % 5 == 0)
```

### Logic explained

- `number % 2 == 0` checks whether the number is even.
- If it is even, Python prints: `number is even`.
- Otherwise, it prints: `number is odd`.
- `number % 3 == 0` checks if the number is divisible by 3.
- `number % 5 == 0` checks if the number is divisible by 5.

This function uses the remainder operator `%` to check divisibility.

## 7. Function: `check_marks(marks)`

```python
def check_marks(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"
```

### Logic explained

- If `marks >= 75`, the function returns `"Distinction"`.
- Else if `marks >= 35`, the function returns `"Pass"`.
- Otherwise, it returns `"Fail"`.

This function uses comparison operators and `if` statements to make a decision.

## 8. Why `return` is used

The `return` keyword sends a value back from the function to the place where it was called.

Example:

```python
return "Pass"
```

This means the function gives the value `"Pass"` back to the program.

Without `return`, the function would only print a result and not send it back.

## 9. Functions and user input

The program reads values from the user using `input()`.

```python
number = int(input("Enter an integer to check: "))
check_number(number)

marks = int(input("Enter the student's marks: "))
print(check_marks(marks))
```

### Logic explained

- `input()` reads text from the user.
- `int(...)` converts it into an integer.
- `check_number(number)` calls the function to check the number.
- `check_marks(marks)` decides the grade result.
- `print(...)` shows the result on the screen.

This shows how functions and user input work together in Python.

## 10. Full program flow summary

The complete program does the following:

1. Takes a number from the user.
2. Calls `check_number(number)`.
3. Checks whether the number is even or odd.
4. Checks if it is divisible by 3 and 5.
5. Takes marks from the user.
6. Calls `check_marks(marks)`.
7. Compares marks using `>=`.
8. Prints `Distinction`, `Pass`, or `Fail`.

This is a simple example of how Python combines:

- arithmetic operators
- remainder operator `%`
- comparison operators like `>=`
- decision-making with `if`
- functions and user input

## Final conclusion

This file teaches the basic building blocks of Python programming.

It shows how operators help us calculate and compare values, while functions help us organize logic. Together, they allow us to build meaningful and useful programs.

