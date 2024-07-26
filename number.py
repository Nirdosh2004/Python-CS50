def main():
        x = getInt()
        print(f"X is {x}")


def getInt():
          while True:
                    try:
                              x = int(input("What's x? "))
                    except ValueError:
                               print("X is not an integer")
                    else:
                            return x
main()

