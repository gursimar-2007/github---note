# import sys
# import name
# if len(sys.argv)==2:
#     name.hello()
import sys
import check
def main():
    n1=int(sys.argv[1])
    op=sys.argv[2]
    n2=int(sys.argv[3])
    check.calculation(n1,op,n2)
if __name__ == "__main__":
    main()
