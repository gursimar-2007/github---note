n=5
for i in range(0,n,1):
    for j in range(0,n-i-1,1):
        print(" ")
    for k in range(0,2*i-1,1):
        print("* ")
    print(f"\n")