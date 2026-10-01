#include<iostream>
using namespace std;
int main(){
    int a;
    int b;
    cout<<"enter your number 1";
    cin>>a;
    cout<<"enter your number 2";
    cin>>b;
    int totalodd=0;
    int totaleven=0;
    for(int i=a;i<=b;i++){
        if(i%2==0){
            totaleven++;
        }
        else{
            totalodd++;
        }
    }
    cout<<totaleven<<endl;
    cout<<totalodd<<endl;

    return 0;
}