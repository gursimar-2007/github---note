def main():
    calculation(1,"+",2)
def calculation(n1,op,n2):
    match op:
        case"+":print("Sum =",sum(n1,n2))
        case"-":sub(n1,n2)
        case"/":
            out = div(n1,n2)
            if out == -1:
                print("f") 

        case"*":mul(n1,n2)
def sum(n1,n2):
    return n1+n2
def mul(n1,n2):
    return n1*n2
def sub(n1,n2):
    return n1-n2
def div(n1,n2):
    if n2==0:
        print("blah blah blah")
        return -1
    return n1/n2
if __name__ == "__main__":
    main()