

x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
name = input("Please tell me your name.")
def greet():
    print("Hello, " + name)

def add_sub(x, y):
    c = x+y
    d = x-y
    return c,d


greet()
sum, diff = add_sub(x, y)
print(sum, diff)

