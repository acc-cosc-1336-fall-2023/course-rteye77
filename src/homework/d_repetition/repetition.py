def get_factorial(num):
    answ = 1
    for i in range(1, num+1):
        answ = answ * i
    return answ

def sum_odd_numbers(num):
    i = 1
    total = 0
    if(num <= 1):
        return 1
    while(i <= num):
        if int(i) % 2 == 1:
            total += i
        i = i + 1
    return total