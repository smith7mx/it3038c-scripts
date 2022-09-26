#Take a number input and calculate how many prime numbers come between it and 0
print('Enter a number to find how many prime numbers come between it and 0')
getNum=int(input())
count=int(0)

for num in range(0, getNum+1):
    if num>1:
        for i in range(2,num):
            if (num %i) == 0:
                break
        else:
            count=count+1
print('There are ' + str(count) + ' prime numbers')