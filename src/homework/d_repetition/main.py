import repetition

def main():
    while(1):
        print("Homework 3 Menu")
        print("1-Factorial")
        print("2-Sum odd numbers")
        print("3-Exit")
        num = int(input("Select one: "))
        if(num == 1):
            n = int(input("Enter a number greater than 0, but less than 10: "))
            if(num > 0 and num < 10):
                answ = repetition.get_factorial(n)
                print("Answer = ", answ)
        if(num == 2):
            n = int(input("Enter a number greater than 0, but less than 100: "))
            if(num > 0 and num < 100):
                answ = repetition.sum_odd_numbers(n)
                print("Answer = ", answ)
        if(num == 3):
            exit = input("Do you want to continue? y/n: ")
            if exit == "y":
                break

main()