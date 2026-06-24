#include<iostream>
using namespace std;
//====================== INPUT OF STUDENT DATA =========================
class students_data{
    public:
    int roll_no;
    char name[20];

    public:
    void read(){
        cout<<"Enter student roll no";
        cin>>roll_no;
        cout<<"Enter student name";
        cin>>name;
    }
};

class maths: public students_data{
    public:
    int maths_marks;

    public:
    void maths_data(){
        cout<<"Enter maths marks";
        cin>>maths_marks;
    }
    void show_data(){
        cout<<"Your data is>>>>>"<<endl;
        cout<<"Student name is "<<name<<"\nRoll number is "<<roll_no<<"\nMarks obtained is: "<<maths_marks; 
    }
    
};
int main(){
    class maths ob;
    ob.read();
    ob.maths_data();
    ob.show_data();
    return 0;
}