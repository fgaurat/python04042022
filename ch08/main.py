import sys
import traceback
from typing import final

def divi(a,b):
    c = a/b
    return c


def call_divi(a,b):
    result = 0
    try:
        print("-- call_divi --")
        result = divi(a,b)
    except Exception as e:
        print(e)
        raise e
    finally:
        print("dans finally de call_divi")
        print("-- write to file --")
    return result

def main():
    try:
        # b=int(input("Quelle est la valeur de b ? : "))
        a=2
        b=0
        c=call_divi(a,b)
        print(c)
    except ValueError as e:
        print("ValueError!",e)
        traceback.print_exc()
    except TypeError as e:
        print("TypeError!",e)
        traceback.print_exc()
        sys.exit(10)
    except Exception as e:
        print(type(e))
        print("erreur !")
        print(e)
        traceback.print_exc()
    else:
        print("else")
    finally:
        print("finally")


    print("après")

if __name__ == '__main__':
    main()