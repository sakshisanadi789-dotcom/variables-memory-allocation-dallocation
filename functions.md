# Python Functions

## 1. Why do we use functions?

Without a function, the same instructions may need to be repeated:

```python
print("Welcome, Sakshi")
print("Welcome, Sanika")
print("Welcome, Akshata")
```

A function lets us write the logic once and reuse it:

```python
def welcome(name):
    print("Welcome,", name)


welcome("Sakshi")
welcome("Sanika")
welcome("Akshata")
```

Functions help with:

- code reuse and less repetition
- organization and readability
- maintenance
- testing individual pieces of a program

## 2. What is a function?

A function is a reusable block of code that performs a task. It can accept input, perform work, and optionally return a result.

```python
def add(a, b):
    return a + b


result = add(2, 3)
print(result)  # 5
```

## 3. Defining versus calling a function

Defining a function describes what it will do. It does not run the body:

```python
def greet():
    print("Hello")
```

Calling the function runs its body:

```python
greet()  # Hello
```

## 4. Functions without parameters

A function does not need parameters if it does not need input from its caller:

```python
def welcome():
    print("Welcome to Nighan2 Labs!")


welcome()
```

## 5. Functions with parameters

Parameters are names listed in the function definition. Arguments are the values passed when the function is called:

```python
def welcome(name):
    print("Welcome,", name)


welcome("Sakshi")
```

Here, `name` is a parameter and `"Sakshi"` is an argument.

## 6. Functions with multiple parameters

```python
def add(a, b):
    print(a + b)


add(10, 20)  # 30
```

The function has two parameters, `a` and `b`, and the call supplies two arguments.

## 7. `print()` versus `return`

`print()` displays information. `return` sends a result back to the caller so the program can store or use it:

```python
def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


add_and_print(10, 20)  # Displays 30
result = add_and_return(10, 20)
print(result)           # Displays 30
```

Use `return` when the calling code needs to work with the result.

## 8. What happens after `return`?

`return` immediately exits the current function. Statements after it in that function are not executed:

```python
def test():
    return 10
    print("This will not run")


print(test())  # 10
```

## 9. Returning multiple values

Python can return several values. They are packed into a tuple and can be unpacked by the caller:

```python
def calculate(a, b):
    return a + b, a - b, a * b


sum_result, difference, product = calculate(10, 5)
print(sum_result)  # 15
print(difference)  # 5
print(product)     # 50
```

## 10. Default parameters

A default parameter value is used when the caller leaves out that argument:

```python
def greet(name="Sakshi"):
    print("Hello,", name)


greet()          # Hello, Sakshi
greet("Sanika")  # Hello, Sanika
```

Defaults are useful when a parameter has a sensible common value. Avoid mutable objects such as lists as defaults; they are shared between calls.

## 11. Positional arguments

Positional arguments are matched to parameters by their order:

```python
def student(name, age):
    print(name, age)


student("Sakshi", 21)
```

Here, `"Sakshi"` is assigned to `name` and `21` to `age`.

## 12. Keyword arguments

Keyword arguments identify parameters by name, so their order can vary:

```python
student(age=21, name="Sakshi")
```

This call uses the `student` function defined in the previous section.

## 13. Combining positional and keyword arguments

You can use positional arguments first, followed by keyword arguments:

```python
def student(name, age, course):
    print(name, age, course)


student("Sakshi", 21, course="BCA")
student(name="Sakshi", age=21, course="BCA")
```

Both calls are valid. This is invalid because a positional argument follows a keyword argument:

```python
# student(name="Sakshi", 21, course="BCA")
```

## 14. `*args`

Use `*args` when a function should accept a variable number of positional arguments. Inside the function, `args` is a tuple:

```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(add(10, 20))           # 30
print(add(10, 20, 30))       # 60
print(add(1, 2, 3, 4, 5))    # 15
```

The name `args` is a convention; the `*` is what collects extra positional arguments.

## 15. `**kwargs`

Use `**kwargs` to accept a variable number of keyword arguments. Inside the function, `kwargs` is a dictionary:

```python
def show_student(**details):
    print(details)


show_student(name="Sakshi", age=21, course="BCA")
# {'name': 'Sakshi', 'age': 21, 'course': 'BCA'}
```

The name `kwargs` is a convention; the `**` collects extra keyword arguments.

## 16. Combining parameters, `*args`, and `**kwargs`

A function can combine regular parameters, extra positional arguments, and extra keyword arguments:

```python
def example(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("extra positional:", args)
    print("extra keyword:", kwargs)


example(1, 2, 3, 4, course="BCA")
```

In this call, `a` is `1`, `b` is `2`, `args` is `(3, 4)`, and `kwargs` is `{"course": "BCA"}`.

## 17. Local and global variables

A variable created inside a function is local to that function:

```python
def show_local():
    message = "I am local"
    print(message)


show_local()
```

A function can read a variable defined at module level (global scope):

```python
message = "I am global"


def show_global():
    print(message)


show_global()
```

## 18. The `global` keyword

To assign to a module-level variable from inside a function, declare it `global`:

```python
count = 0


def increment():
    global count
    count += 1


increment()
print(count)  # 1
```

Avoid global state when possible. Passing values as parameters and returning results usually makes functions easier to reuse and test.

## 19. Local scope and `NameError`

A local variable cannot normally be accessed outside the function where it is defined:

```python
def test():
    value = 10


test()
print(value)  # Raises NameError: value is not defined here
```

The name `value` is local to `test()`.

## 20. Functions can call other functions

Functions can be combined to organize a program into smaller steps:

```python
def add(a, b):
    return a + b


def display_result():
    result = add(10, 20)
    print(result)


display_result()  # 30
```

A larger program might follow a flow like:

```text
main() -> validate() -> calculate() -> save() -> display()
```