from collections import defaultdict, Counter

# d = {"a": 1}
# print(d["a"])
# print(d.get("a"))
# print(d.get("b"))
# print(d)

# d = defaultdict(lambda: 2)
# d["a"] = 3
# print(d["b"])
# print(d)

d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)

counter = defaultdict(int)
mylist = ["a", "a", "b", "b", "a", "c"]
for item in mylist:
    counter[item] += 1

print(counter)

counter = Counter(mylist)
print(counter.values())

from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])

person1 = Person("Alice", 28, "Berlin")
person2 = Person("Bob", 32, "New York")

print(person1.name)
print(person1._asdict())

### Itertools

# permutations
from itertools import chain, combinations, cycle, count, islice

a = [1,2,3]
b = [4,5,6]
c = list(chain(a, b))
print(c)

print(list(combinations(c, 4)))

# counter = cycle(a)
# for _ in range(100):
#     print(next(counter))

counter = count(80, 2)

# for val in counter:
#     print(val)
#     if val > 100:
#         break

limited_counter = islice(counter, 94, 100)
for val in limited_counter:
    print(val)

### Functions

from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(4))

# Unveränderbare default values

class MathOperations:
    def __init__(self):
        self.add = partial(self.operation, operation_type="add")
        self.subtract = partial(self.operation, operation_type="subtract")

    def operation(self, operation_type, x, y):
        if operation_type == "add":
            return x + y
        elif operation_type == "subtract":
            return x - y

math_operations = MathOperations()

result_add = math_operations.add(5, 3)
print(result_add)

result_subtract = math_operations.subtract(5, 3)
print(result_subtract)



