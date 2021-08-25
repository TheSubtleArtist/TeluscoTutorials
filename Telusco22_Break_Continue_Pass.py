#Break

x = int(input ("How many Candies do you want"))
av = 5
i = 1

while i<= x:
    if i>av: #Checks to see if candy is available
        print("Only " + str(av) + " candies are available. You have exhausted the supply of available candy")
        break #exits the loop
    print("Candy")
    i+=1 #Shortcut for i=i+1 to increment
print("Bye")

#Print all numbers in a range, skpping those divisible by a particular value

y = int(input("Enter a number between 1 and 9"))
z = int(input("Enter a maximum value"))

print ("These are all the of the numbers between 1 and " + str(z) + " which are not divisible by " + str(y) +".")
for i in range (1,z):
    if i%y == 0:
        continue  #skips remaining statements, but does not exit the loop
    print(i)
print("The End")

#

z = int(input("Enter a maximum value"))
print ("These are all the not odd numbers between 1 and " + str(z) + ".")
for i in range(1,z):
    if(i%2!=0): #notice there is only on equal sign for the comparison, because the ! is the second.
        pass #Indicates there is no actual code because, so the machine should simply continue
    else:
        print(i)
print("The End, Bye.")
