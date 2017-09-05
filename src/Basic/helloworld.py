# Number
num1 = 10
num2 = 20
num1 += 5
num2 += 5
sum = num1 + num2
print("Total = " + str(sum))

# Array
list = []
list.append("JB")
list.append("Lily")
list.append("Leia")
list.append("Hachi")
#list.remove("Hachi")
#list.reverse()
list.sort()
for value in list:
    print("Name : " + value)


last = list.pop()
print("Last : " + last)