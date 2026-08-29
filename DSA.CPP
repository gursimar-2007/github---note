// hey 
#include<bits/stdc++.h>
using namespace std;
int getcircumfrence(float a,float b){
    float c;
    c=3.14*a*b;
    cout<<c;
    return c;
}
int main(){
    int a,b;

    cout<<"enter your number";
    cin>>a;
    cout<<"enter your second number";
    cin>>b;
    getcircumfrence(a,b);
    return 0;


}