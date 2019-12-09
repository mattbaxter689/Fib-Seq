#create a function that will calculate the fibonacci sequence

'''
- Add check that asks the user at the end if they want to see more fibonacci numbers
'''

def fib_seq(n):
    if n <= 1:
        return n
    else:
        return (fib_seq(n-1) + fib_seq(n-2))
        

#create function that makes sure the user enters a positive number
def user_num():
    while True:
        x = input("How many Fibonacci numbers would you like to see?: ")
        
        if not x.isdigit():
            print("Please ensure to enter a positive integer")
            continue
        else:
            x = int(x)
            break

    return x

def main():
    while True:

        n = user_num()
        for i in range(n):
            print(fib_seq(i))
        
        see_again = input("Would you like to see more Fibonacci numbers? Enter 'y' or 'n': ")

        if see_again.lower()[0] == 'y':
            continue

        else:
            break

if __name__ == "__main__":
    main()
        
