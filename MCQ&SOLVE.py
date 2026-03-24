# Q1
x = [1,2,3]
print(x * 2)   # Answer: [1,2,3,1,2,3]

# Q2
print(bool(""))   # Answer: False

# Q3
print("list")   # Answer: list

# Q4
print(10 == 10.0)   # Answer: True

# Q5
a = [1,2,3]
b = a
b.append(4)
print(a)   # Answer: [1,2,3,4]

# Q6
def func(x=[]):
    x.append(1)
    return x
print(func())   # Answer: [1]
print(func())   # Answer: [1,1]

# Q7
for i in range(5):
    if i == 3:
        break
    print(i)   # Answer: 0,1,2

# Q8
try:
    print(10/0)
except:
    print("Error")   # Answer: Error
finally:
    print("Done")    # Answer: Done

# Q9: 
s = "Hello World"
vowels = "aeiouAEIOU"
v_count = sum(1 for ch in s if ch in vowels)
c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print("Vowels:", v_count, "Consonants:", c_count)

# Q10: 
with open("sample.txt","r") as f:
    text = f.read()
lines = text.splitlines()
words = text.split()
chars = len(text)
print("Lines:", len(lines), "Words:", len(words), "Characters:", chars)

# Q11:
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
    def check_balance(self):
        return self.balance

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(300)
print(acc.check_balance())   # Answer: 700

# Q12: 
nums = [4,2,5,2,1,4]
unique = list(set(nums))
for i in range(len(unique)):
    for j in range(i+1, len(unique)):
        if unique[i] > unique[j]:
            unique[i], unique[j] = unique[j], unique[i]
print(unique)   # Answer: [1,2,4,5]

# Q13:
nums = [1,2,3,4,5,6]
result = list(map(lambda x: x**2, filter(lambda x: x%2==0, nums)))
print(result)   # Answer: [4,16,36]

# Q16:
def login():
    uname = "user1"
    pwd = "pass1"
    with open("users.txt") as f:
        for line in f:
            u,p = line.strip().split(",")
            if u == uname and p == pwd:
                print("Login successful")
                return
    print("Invalid credentials")
login()

# Q17: 
class InvalidAgeError(Exception):
    pass
age = 15
if age < 18:
    raise InvalidAgeError("Age must be 18 or above")
else:
    print("Valid age")

# Q18: 
import tkinter as tk
def show_name():
    lbl.config(text="Entered: " + entry.get())
root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="Submit", command=show_name)
btn.pack()
lbl = tk.Label(root)
lbl.pack()
root.mainloop()

# Q19:
import sqlite3
con = sqlite3.connect("student.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Student(id INTEGER PRIMARY KEY, name TEXT, age INT)")
cur.executemany("INSERT INTO Student(name, age) VALUES (?,?)",
                [("Alice",20),("Bob",21),("Charlie",22)])
con.commit()
for row in cur.execute("SELECT * FROM Student"):
    print(row)
con.close()

# Q20: 
import sqlite3
con = sqlite3.connect("sms.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Student(id INTEGER PRIMARY KEY, name TEXT, age INT)")
def add_student(name, age):
    cur.execute("INSERT INTO Student(name, age) VALUES (?,?)", (name, age))
    con.commit()
def view_students():
    for row in cur.execute("SELECT * FROM Student"):
        print(row)
def delete_student(id):
    cur.execute("DELETE FROM Student WHERE id=?", (id,))
    con.commit()
add_student("Ravi", 20)
add_student("Meena", 21)
view_students()
delete_student(1)
view_students()