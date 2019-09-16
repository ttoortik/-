sum = 0;
def sumfinder (num):
    divsum = 0
    for div in range(1,num):
        if num % div == 0:
            divsum+=div
    return divsum

for num in range(1,9999):
    if sumfinder(num)!=num and sumfinder(sumfinder(num)) == num:
        sum+=num
print(sum)




