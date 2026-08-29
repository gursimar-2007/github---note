// hey 
// #include<bits/stdc++.h>
// using namespace std;
// float getcircumfrence(float radii){
    //     float c;
    //     c=2*3.14159265359*radii;
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
#include<bits/stdc++.h>
using namespace std;
bool is_vowel(char ch){
    if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u'||ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U'){
        cout<<"your character is a vowel";
    }else {
        cout<<"your character is not a vowel";
    }  

}
int main(){
    char ch;
    cout<<"enter your character";
    cin>>ch;
    is_vowel(ch);
    return 0;
}
