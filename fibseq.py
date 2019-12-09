#create a function that will calculate the fibonacci sequence

def fib_seq(n):
    if n <= 1:
        return n
    else:
        return (fib_seq(n-1) + fib_seq(n-2))
        

#create function that makes sure the user enters a positive number
def user_num():
    while True:
        x = int(input("How many Fibonacci numbers would you like to see?: "))
        
        if x < 0:
            print("Please ensure to enter a positive integer")
            continue
        else:
            break

    return x

def main():
    n = user_num()
    for i in range(n):
        print(fib_seq(i))

if __name__ == "__main__":
    main()
        
