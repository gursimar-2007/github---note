import tests
import check
def main():
    
    test_positive()
def test_positive():
    assert check.sum(10,10)==20
    assert check.sum(10,20)==30
    assert check.sum(10,0)==10
def test_negative():
    assert check.sub(10,10)==0
    assert check.sub(20,10)==10
    assert check.sub(10,0)==10
def test_multiply():
    assert check.mul(10,10)==100   
    assert check.mul(20,10)==200
    assert check.mul(20,0)==0
def test_divide():
    assert check.div(10,10)==1
    assert check.div(20,10)==2
    assert check.div(20,0)==0


if __name__ == "__main__":
    main()