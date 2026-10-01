#include<iostream>
using namespace std;
int main(){
    int a;
    int b;
    cout<<"enter your number 1";
    cin>>a;
    cout<<"enter your number 2";
    cin>>b;
    int i;
    bool is_prime=true;
    for(i=a;i<=b;i++){
        if(i<=1){
            continue;
        }
        for(int j=2;j*j<=i;j++){
            
            if (i%j==0){
                is_prime=false;
                break;
            }
        }
        // cout<<i;
        if(is_prime){
            cout<<i<<"";
        }
    }
// cout<<endl;
int usm;
i==usm;
// cout<<usm;



    return 0;
}