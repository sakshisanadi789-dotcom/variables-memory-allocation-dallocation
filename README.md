# Variables, Memory Allocation, and Deallocation

## 1) What are the uses of variables in Python?

Variables in Python are names that refer to values stored in memory. They are used to:

- store data temporarily or permanently
- keep track of program state
- pass values into functions
- perform calculations using stored values
- reuse values without rewriting them

Example:

```python
x = 10
y = x + 5
name = "Alice"
print(y, name)
```

In this code:
- `x` is a variable name
- `10` is the value stored in memory
- `x` points to that memory location

## How memory associates with variables

Python variables do not usually store the value directly in the variable itself. Instead, the variable stores a reference to an object in memory.

```python
a = [1, 2, 3]
b = a
```

Here, both `a` and `b` refer to the same list object in memory.

If we change one:

```python
b.append(4)
print(a)   # [1, 2, 3, 4]
print(b)   # [1, 2, 3, 4]
```

This shows that both names point to the same underlying object.

## Validity / lifetime / expiry of variables

A variable’s lifetime depends on its scope:

- local variable: exists while the function or block runs
- global variable: exists for the module/program lifetime
- object: lasts as long as at least one reference points to it

Example:

```python
def demo():
    x = 5
    return x

print(demo())
```

`x` is created inside `demo()`, and it is destroyed when the function ends.

When we delete a variable:

```python
x = 10
del x
```

The name `x` is removed. The object may still exist if another name references it.

Python frees memory automatically when an object has no references left. This is done mainly through:

- reference counting
- garbage collection for cyclic references

```python
x = []
y = x
del x
# the list still exists because y points to it
```

When no references remain, Python reclaims the memory.

---

## 2) How memory allocation works in Node.js for variables

Node.js uses the V8 JavaScript engine. V8 manages memory automatically.

There are two important memory areas:

- stack: stores primitive values and execution context
- heap: stores objects, arrays, functions, and larger structures

Example:

```js
let num = 42;
let user = { name: "Asha" };
```

- `num` is a primitive value
- `user` is an object stored in the heap
- the variable stores a reference to that heap object

### Scope and lifetime in JavaScript

```js
function demo() {
  let x = 10;
  if (true) {
    let y = 20;
  }
  // y is gone here
}
```

`let` and `const` are block-scoped. Variables are released when their scope ends.

### Garbage collection in Node.js

Node.js/V8 uses automatic garbage collection. If an object is no longer reachable, the engine frees it.

```js
let obj = { name: "test" };
obj = null;
```

Now the original object becomes unreachable and can be collected.

V8 uses generational garbage collection, so short-lived objects are collected quickly, while long-lived objects are handled efficiently.

---

## 3) How memory allocation and deallocation work in Python for variables

### Allocation

When you assign a value, Python creates the object and binds the variable to it:

```python
x = 100
name = "Alice"
items = [1, 2, 3]
```

Python allocates memory for the object, then binds the variable to that object.

### Deallocation

Python does not require manual memory deletion like C/C++.

It frees memory automatically when:

- a variable is deleted with `del`
- the variable goes out of scope
- the object has no references left
- the garbage collector finds cyclic references

Example:

```python
x = [1, 2, 3]
del x
```

The name is removed. If no other references exist, the list becomes eligible for garbage collection.

### Cycles

```python
a = []
b = []
a.append(b)
b.append(a)
```

This creates a cycle. Python detects such cycles and reclaims them periodically using garbage collection.

---

## Quick comparison

| Topic | Python | Node.js (JavaScript) |
| --- | --- | --- |
| Variable type | Reference to Python object | Value managed by V8 |
| Memory model | Heap + object references | Stack + heap |
| Cleanup | Reference counting + GC | Garbage collection |
| Scope | function/module block-based | function/block-based |
| Manual deallocation | `del` reduces references | no manual memory delete in normal JS |

## Final idea

Variables are names used to access memory-backed values. In Python, they are references to objects; in Node.js, they are values managed by the V8 engine. In both cases, memory is automatically managed so that developers do not have to manually free memory in the usual way.

This is why Python and JavaScript are easier to work with than lower-level languages such as C and C++.
