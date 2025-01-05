# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2  

    def perimeter(self):
        return 2 * 3.14159 * self.radius

  
c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())
# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
class Person:
    def __init__(self, name, country, year_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth

    def age(self, current_year):
        return current_year - self.year_of_birth

  
p = Person("John Doe", "USA", 1990)
print("Age:", p.age(2025))
# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

  
calc = Calculator()
print("Add:", calc.add(10, 5))
print("Subtract:", calc.subtract(10, 5))
print("Multiply:", calc.multiply(10, 5))
print("Divide:", calc.divide(10, 5))
# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return 3 * self.base

  
s = Square(4)
print("Square Area:", s.area())
print("Square Perimeter:", s.perimeter())
# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)
        
        return self._search(root.right, key)

  
bst = BinarySearchTree()
bst.insert(10)
bst.insert(20)
bst.insert(5)
print(bst.search(10)) 
# 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

  
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop()) 
# 7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

  
ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(1)
ll.display()
ll.delete(2)
ll.display()  
# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

  
cart = ShoppingCart()
cart.add_item("Apple", 1.0)
cart.add_item("Banana", 0.5)
print("Total Price:", cart.total_price()) 
cart.remove_item("Apple")
print("Total Price:", cart.total_price())  
# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def display(self):
        print(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

  
stack = Stack()
stack.push(1)
stack.push(2)
stack.display()
print(stack.pop())
stack.display()  
# 10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

  
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue()) 
queue.enqueue(3)
print(queue.dequeue()) 
print(queue.dequeue())
# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, name, balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, name, balance)
        else:
            print("Account already exists")

    def remove_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print("Account does not exist")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account does not exist")

  
bank = Bank()
bank.add_account(101, "John Doe", 500)
account = bank.get_account(101)
print("Balance:", account.get_balance())
account.deposit(200)
print("Balance:", account.get_balance())