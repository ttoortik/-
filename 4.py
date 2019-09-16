max = 0;
for first in range(100,999):
    for second in range(100,999):
        if str(first*second) == str(first*second)[::-1] and max<first*second:
            max = first*second
print(max)
