def main():
          number = getNum()
          meow(number)

def getNum():
        while True:
                n = int(input("Enter n : "))
                if n > 0:
                       break
                return n

def meow(n):
        for _ in range(n):
                print("meow")

main()