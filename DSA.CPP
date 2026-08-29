// hey 
#include<bits/stdc++.h>
using namespace std;
double getcircumfrence(double radii){
    double c;
    c=2*3.14159265359*radii;
    cout<<c;
    return c;
}
int main(){
    double r;

    cout<<"enter your radii";
    cin>>r;
    getcircumfrence(r);
    return 0;


}