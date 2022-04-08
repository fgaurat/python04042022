# import fibo


# fibo.fib(10)
# print(fibo.fib2(10))
# import fibo
import sys
import fibo as fiboo
from fibo import fib as fibb, fib2 as fibb2


def fib(n):
    print("fib", n)


def main():

    fibb(10)
    print(fibb2(10))

    print("main", __name__)
    print("sys.argv", sys.argv)
    
    if len(sys.argv)>1:
        the_value = int(sys.argv[1])
        print(fibb2(the_value))
    else:
        print("erreur !")

if __name__ == "__main__":
    main()
