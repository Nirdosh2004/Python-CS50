# x = int(input("what's x? "))

# if x % 2 == 0:
#           print("X is even")
# else:
#         print("x is odd")

def is_Even(n):
        return  n%2 == 0

def main():
          x = int(input("What's x? "))
          print("Even ") if is_Even(x) == True else print("Odd")
          
main()
