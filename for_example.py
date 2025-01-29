#sum of the first 10 numbers
sum=0
for num in range(1,3): #last one is excluded, so it goes from 1 to 10, loops from 1 to 2
    sum = sum+num
print(sum)

#print multiplication example
for i in range (1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

#re write using while
sum= 0
num = 0 #need to define it in while loop
while num < 100:
    num = num + 1
    sum += num #this is equal to sum+num
print(sum)