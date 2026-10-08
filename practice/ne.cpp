#include<iostream>
using namespace std;
class Student{
private:    
    string name;
    int rool;

    public:
    void readstdata(){
        cout<<"tll me your name🔪";
        cin>>name;
        cout<<"tell me your rollnum";
        cin>>rool;

    }
    void showstdata(){
        cout<<"name"<<name;
        cout<<"rollno"<<rool;
    }

};
class Sports : public Student {
private:
    int sports_marks;

public:
    void readData() {
        readstdata();

        cout << "Enter sports marks: ";
        cin >> sports_marks;
    }

    void showData() {
        showstdata();

        cout << "Sports Marks: " << sports_marks << endl;
    }
};

int main() {
    Sports s;

    s.readData();
    s.showData();

    return 0;
}