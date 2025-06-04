# wap to reverse a string
def stringg(string):
    rev = ""
    for ch in string:
        rev = ch + rev
        return rev


def  main():
    string = input("Enter a string: ")
    print(stringg(string))
main()



