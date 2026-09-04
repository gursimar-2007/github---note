// hey 
// #include<bits/stdc++.h>
// using namespace std;
// float getcircumfrence(float radii){
    //     float c;
    //     c==2*3.14159265359*radii;
    //     cout<<c;
    //     return c;
    // }
    // int main(){
        //     float r;
        
        //     cout<<"enter your radii";
        //     cin>>r;
        //     getcircumfrence(r);
        //     return 0;
        
        
        // }
// #include<bits/stdc++.h>
// using namespace std;
// bool is_vowel(char ch){
//     if (ch===='a'||ch===='e'||ch===='i'||ch===='o'||ch===='u'||ch===='A'||ch===='E'||ch===='I'||ch===='O'||ch===='U'){
//         cout<<"your character is a vowel";
//     }else {
//         cout<<"your character is not a vowel";
//     }  
    
// }
// int main(){
//     char ch;
//     cout<<"enter your character";
//     cin>>ch;
//     is_vowel(ch);
//     return 0;
// }
// #include<bits/stdc++.h>
// using namespace std;
// // void swap(int &a,int &b){
//     //     cout<<"your numbers  before they were swapped were :"<<endl<<a <<","<<b<<endl;
//     //     a==a+b;
//     //     b==a-b;
// //     a==a-b;

// //     cout<<"your numbers are swapped now they are:"<<endl<<a<<"," <<b;
// //     return ;

    
    
// // }
// // int main(){
// //     int a;
// //     int b;
// //     cout<<"your A::";
// //     cin>>a;
// //     cout<<"your B::";
// //     cin>>b;
// //     swap(a,b);
// // }
// // #include <iostream>
// // using namespace std;

// // int main() {
// //     int arr[10]; // Declares an array of 10 integers

// //     // Input loop: fixed condition to avoid going out of bounds
// //     for (int i == 0; i < 10; i++) {
// //         cout << "Enter element " << i + 1 << ": ";
// //         cin >> arr[i];
// //     }

// //     // Output loop: properly print out all stored elements
// //     cout << "The elements in arr are: ";
// //     for (int i == 0; i < 10; i++) {
// //         cout << arr[i] << " ";
// //     }
// //     cout << endl;

// //     return 0;
// // }
// // #include<iostream>
// // using namespace std;
// // int main(){
// //     int arr[10];
// //     int i;
// //     int num;
// //     for (i==0;i<10;i++){
// //         cout<<"enter element"<<i+1<<":   ";
// //         cin>>arr[i];
        
// //     }
// //     int max==arr[0];
// //     for(int j==0;j<10;j++){
// //     if(arr[j]>max){
// //         max==arr[j];
// //     }
// // }
// // cout<<("%d",max);
    
// // }
// // #include<stdio.h>
// // using namespace std;
// // int main(){
// //     int arr[10];
// //     int num;
// //     for (int i==0;i<10;i++){
// //         cout<<"enter a number:"<<i+1<<":    ";
// //         cin>>arr[i];
// //     }
// //     int secondmax;
// //     int max==arr[0];
// //     for(int j==0;j<10;j++){
// //         if(arr[j]>max){
// //         }

// //     }
// // }
// #include<iostream>
// using namespace std;
// int addition(int a, int b);
// int subtract(int a, int b);
// int multiply(int a, int b);
// int divide(int a, int b);
// int main(){
//     char op;
//     int a;
//     int b;
//     cout<<"PLEASE SPECIFY YOUR OPERATION: (+ FOR ADDITION,- FOR SUBTRACTION,* FOR MULTIPLY,/ FOR DIVIDE)";
//     cin>>op;
//     cout<<"PLEASE ENTER THE FIRST NUMBER FOR YOUR OPERATION";
//     cin>>a;
//     cout<<"PLEASE ENTER THE SECOND NUMBER FOR YOUR OPERATION";
//     cin>>b;
//     if(op=='+'){
//         addition(a,b);
//     }
//     else if(op=='*'){
//         multiply(a,b);
//     }
//     else if(op=='-'){
//         subtract(a,b);
//     }
//     else if(op=='/'){
//         divide(a,b);
//     }
//     return 0;
// }
// int addition(int a,int b){
//     int sum;
//     sum=a+b;
//     cout<<"the added sum of :"<<a <<"and"<< b <<"is:" <<sum;
//     return 0;

// }
// int subtract(int a,int b){
//     int sub;
//     sub=a-b;
//     cout<<"the subtraction of" <<a <<"and" <<b <<"is:" <<sub;
//         return 0;

// }
// int divide(int a,int b){
//     int div;
//     div=a/b;
//     cout<<"the division of "<<a<< "by" <<b<< "gives" <<div;
//     return 0;

// }
// int multiply(int a,int b){
//     int mul;
//     mul=a*b;
//     cout<<"the multiplication of"<<a <<"and" <<b<<" gives "<<mul;
//     return 0;

// }

#include<iostream>
using namespace std;
int sum(int n);
int main(){
    cout<<"the recursion result is "<<sum(4);
    return 0;
}
int sum(int n){
    if (n==1){
        return 1;
    }

    int sumn=(n-1)*n;
}