# Python Variables, Objects, and Memory Management

## 1. What is a variable in Python?

A Python variable is a **name bound to an object**. It is not a box that permanently contains a value.

```python
x = 10
```

Conceptually, the name `x` refers to the integer object `10`. Python objects have an identity, a type, and a value:

```python
x = 10
print(id(x))   # identity for this object during its lifetime
print(type(x)) # <class 'int'>
print(x)       # value: 10
```

`id()` returns an identity value that is unique and constant for an object's lifetime. Its exact meaning is implementation-dependent; in CPython it is commonly related to the object's memory address.

## 2. Are Python values objects?

In Python, values such as numbers, strings, lists, functions, and classes are objects. For example:

```python
number = 10
name = "sakshi"
marks = 85.5
numbers = [10, 20, 30]
```

Each name is bound to an object. The objects have identities and types, and their values are accessible through those names.

## 3. Built-in data type categories

- Numeric: `int`, `float`, `complex`
- Boolean: `bool`
- Text: `str`
- Sequence: `list`, `tuple`, `range`
- Set: `set`, `frozenset`
- Mapping: `dict`
- Binary: `bytes`, `bytearray`, `memoryview`
- Special: `NoneType` (the type of `None`)

## 4. Numeric types

```python
age = 25            # int
count = -10         # int
price = 99.0        # float
percentage = 88.75  # float
z = 3 + 4j          # complex
```

## 5. Boolean values

Python's Boolean values are `True` and `False` (capitalized). `bool()` converts a value to its truth value:

```python
is_active = True
is_logged_in = False

print(bool(0))       # False
print(bool(""))      # False
print(bool("hello")) # True
```

## 6. Strings

A string (`str`) is an immutable sequence of characters. Indexing starts at zero:

```python
name = "Aishu"
print(name[0])  # A
print(name[1])  # i
```

Strings are immutable: an individual character cannot be replaced in place. An expression can instead create a new string and bind a name to it.

## 7. Lists

```python
numbers = [10, 20, 30]
data = [10, "python", 25.5, True]
```

Lists are ordered, mutable, allow duplicate values, and can contain values of different types.

## 8. Tuples

```python
point = (10, 20)
```

Tuples are ordered and immutable, and they can contain duplicate values. A tuple cannot have its elements replaced, though an element that refers to a mutable object can itself be mutated.

## 9. Sets

```python
numbers = {10, 10, 20, 30}
print(numbers)  # {10, 20, 30}; display order is not guaranteed
```

Sets contain unique, hashable elements. A `set` is mutable, but it is not used for positional indexing. Use `set()` to create an empty set; `{}` creates an empty dictionary.

## 10. Dictionaries

Dictionaries store key-value pairs:

```python
student = {
    "id": 101,
    "name": "Aishu",
    "marks": 85.5,
}
```

Keys are unique and must be hashable. Dictionaries preserve insertion order in modern Python.

## 11. `None`

`None` represents the absence of a value. It is different from `0`, `False`, `""`, and `[]`:

```python
result = None
if result is None:
    print("No result yet")
```

Use `is None` to check for `None`.

## 12. Mutable and immutable objects

An immutable object's value cannot be changed after it is created. Common immutable types include `int`, `float`, `bool`, `str`, `tuple`, and `frozenset`.

Mutable objects can be changed in place. Common mutable types include `list`, `set`, `dict`, and `bytearray`.

## 13. Rebinding a name is not changing an immutable object

```python
x = 10
x = 20
```

The name `x` first refers to the integer object `10`, then is rebound to the integer object `20`. The integer `10` was not modified.

## 14. Multiple names can refer to one object

```python
a = 10
b = a
```

Both names refer to the same integer object conceptually. Rebinding `a` does not rebind `b`:

```python
a = 20
print(a)  # 20
print(b)  # 10
```

## 15. Mutating a shared mutable object

```python
a = [10, 20]
b = a
b.append(30)
print(a)  # [10, 20, 30]
```

Both names refer to the same list. `append()` mutates that list, so the change is visible through either name.

## 16. `==` versus `is`

- `==` checks whether two objects compare equal in value.
- `is` checks whether two names refer to the exact same object.

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True: equal contents
print(a is b)  # False: distinct list objects
```

Use `is` for identity checks such as `value is None`; use `==` for value comparisons.

## 17. Where does Python use memory?

Python uses memory for objects created by a program, including integers, strings, lists, dictionaries, and functions. Python manages object allocation through its runtime and allocator; the exact details depend on the Python implementation. In CPython, Python's allocator obtains memory from the underlying process and operating system as needed.

## 18. Reference counting in CPython

CPython primarily uses reference counting to track references to objects:

```python
a = [1, 2, 3]
b = a
del b
```

Initially, both `a` and `b` refer to the list. Deleting `b` removes that reference; `a` still refers to the list. (The exact reference count can include internal references as well.)

## 19. Garbage collection

Python manages memory automatically; normally, you do not manually free an object's memory. An object can be reclaimed when it is no longer reachable. In CPython, reference counting handles many objects promptly, while the cyclic garbage collector can handle unreachable reference cycles.

## 20. Reference counting and cyclic garbage collection

Reference counting alone cannot reclaim an isolated cycle, because objects in the cycle keep references to one another:

```python
a = []
a.append(a)
```

The list refers to itself. Python's cyclic garbage collector can detect and reclaim unreachable cycles. The `gc` module provides interfaces for inspecting and controlling cyclic garbage collection.

## 21. What does `del` do?

`del` removes a name binding; it does not necessarily destroy the object immediately:

```python
numbers = [1, 2, 3]
other = numbers
del numbers
print(other)  # [1, 2, 3]
```

The list remains reachable through `other`.

## 22. When can an object be reclaimed?

```python
numbers = [1, 2, 3]
other = numbers
del numbers
del other
```

After both names are deleted, this list has no references from these names and may be eligible for reclamation if nothing else refers to it. The timing of reclamation, and whether memory is returned to the operating system, depends on the implementation and allocator.

## 23. The big picture

```text
name -> object (identity, type, value)
                 |
                 v
          managed memory
                 |
       object becomes unreachable
                 |
       memory may be reclaimed
```

Names refer to objects. Python's runtime manages those objects and their memory; garbage collection is part of that memory-management system, not a direct action performed by each variable.

## 24. If Python has garbage collection, why doesn't `del numbers` necessarily destroy the object immediately?

Because `del numbers` removes the name `numbers`, not every reference to the object. If another name or part of the program still refers to it, the object remains reachable. When an object becomes unreachable, it is eligible for reclamation. CPython often reclaims ordinary objects promptly through reference counting, but cycles may require cyclic garbage collection, and Python does not guarantee when memory will be returned to the operating system.