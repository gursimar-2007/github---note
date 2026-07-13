import calculations
def main():
    testing_code()
def testing_code():3
    # if calculations.square(2)!=4:
    #     print("4 is er of 2")
    # if calculations.square(0)!=0:
    #     print("0 is not equal to 0")
    # if calculations.square(3)!=0:
    #     print("9 is not equal to 2")
    # if calculations.square(-2)!=4:
    #     print("4 is not equal to 2")
    # try:
        assert calculations.square(2)==4
        assert calculations.square(3)==9
        assert calculations.square(-2)==2
        assert calculations.square(0)==0
        assert calculations.square(-3)==9
    # except AssertionError:
    #     print("Error in output of code")
def test_positive():
     assert calculations.square(3)==9
     assert calculations.square(1)==1
     assert calculations.square(2)==4
def test_negative():
     assert calculations.square(-1)==1
     assert calculations.square(-2)==4
     assert calculations.square(-3)==9

if __name__=="__main__":
    main()