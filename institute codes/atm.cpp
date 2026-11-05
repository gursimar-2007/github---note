#include <iostream>
using namespace std;
int main()
{
    int pin;
    int check_bal;
    int depo_mon;
    int withdraw;
    char exit;
    char op;
    int balance;
    balance = 100000;

    cout << "welcome to the atml" << endl
         << "please enter your pin";
    cin >> pin;
    if (pin == 12345)
    {
        cout << "correct pin";
        do
        {

            cout << "ENTER YOUR OPERATION"<<endl;
            cin >> op;
            if (op == '1')
            {
                cout << "your current balance is" << balance << endl;
            }
            else if (op == '2')
            {
                cout << "please enter amount to deposit money" << endl;
                cin >> depo_mon;
                balance += depo_mon;
                cout << "your current balance is" << balance << endl;
            }
            else if (op == '3')
            {
                cout << "please enter amount to withdraw" << endl;
                cin >> withdraw;
                if (withdraw > balance)
                {
                    cout << "you are slave" << endl;
                }
                else
                {

                    balance -= withdraw;
                    cout << "Your balance is now" << balance << endl;
                }
            }
            else if (op == '4')
            {
                cout << "THANKYOU FOR USING ATMSS" << endl;
                break;
            }
        } while (1);
    }
    else if(pin!=12345){
        cout<<"enter correct pin"<<endl;
    }

    return 0;
}