n1=int(input("please enter the number"))
n2=int(input("please enter the number"))
n3=int(input("please enter the number"))
n4=int(input("please enter the number"))
n5=int(input("please enter the number"))
n6=int(input("please enter the number"))
n7=int(input("please enter the number"))
n8=int(input("please enter the number"))
n9=int(input("please enter the number"))
det={
    1:{"frow":n1,"srow":n2,"trow":n3},
    2:{"frow":n4,"srow":n5,"trow":n6},
    3:{"frow":n7,"srow":n8,"trow":n9}
}
print("your matrix is this thingy")
for k,v in det.items():
    print(f"{v["frow"]} {v["srow"]} {v["trow"]}")
print("YOUR DETERMINANT IS")
print(f"{(n1*((n5*n9)-(n8*n6))) - (n2*((n4*n9)-(n7*n6))) +(n3*((n4*n8)-(n7*n5)))}")

