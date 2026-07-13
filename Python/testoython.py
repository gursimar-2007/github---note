def prime_numbers():
    n=int(input("enter a number"))
    for i in range(2,n-1):
        if n%i==0:
            print("not a prime number")
            break
        # isprimenumber=1
        else:
            print("a prime number")
            break
def fact(n):
    if n>0:
        if n == 0 or n == 1:
            return 1
        return n * fact(n - 1)
def putha():
    n=input()
    print(n[::-1])
    list=[1,2,3,4,5]
    sum=0
    for i in range(len(list)):
        if(list[i]%2==0):
            sum=sum+list[i]
            print(sum)
def pallendrome():            
    n=input()
    reverse_el=n[::-1]
    if(reverse_el==n):
        print("pali")
    else:    
        print("no pali")
print(fact(4))
pallendrome()
putha()
prime_numbers()
