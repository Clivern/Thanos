#include <iostream>

int main()
{
    int h = 5;
    h += 5;
    h++;
    ++h;
    std::cout << "h => " << h++ << "\n"; // h => 12
    std::cout << "h => " << ++h << "\n"; // h => 14

    int x = 4;

    if(x == 4){
        std::cout << "x == 4\n";
    }else if(x > 4){
        std::cout << "x > 4\n";
    }else if (x < 4){
        std::cout << "x < 4\n";
    }else if (x != 4){
        std::cout << "x != 4\n";
    }

    bool z = true;
    bool y = false;

    if(z && y){
        std::cout << "z and y are true\n";
    }else if(z || y){
        std::cout << "z or y are true\n";
    }

    bool k = true;
    k &= true;
    k == true ? std::cout << "k is true\n" : std::cout << "k is false\n";

    bool o = false;
    o |= false;
    o == true ? std::cout << "o is true\n" : std::cout << "o is false\n";

    int q = 2;
    if(q > 4)
        std::cout << "success";
        // below statement is outside the if condition
        std::cout << "Not inside the if condition";

    for(int r=0; r <= 5; r++){
        std::cout << "r = " << r << "\n";
    }

    for(int l=0; l <= 10; l++){
        if(l == 4){
            continue;
        }
        if(l == 9){
            break;
        }
        std::cout << "l = " << l << "\n";
    }

    bool u = true;
    int i = 0;
    while(u){
        i += 1;
        std::cout << "i = " << i << "\n";
        if(i == 10){
            u = false;
        }
    }

    int a, b, c;
    std::cout << "Enter 3 Number\n";
    std::cin >> a >> b >> c;
    if(a > b)
    {
        if( a > c)
        {
            std::cout << "a is greatest\n";
        }
        else
        {
            std::cout << "c is greatest\n";
        }
    }
    else
    {
        if( b > c)
        {
            std::cout << "b is greatest\n";
        }
        else
        {
            std::cout << "c is greatest\n";
        }
    }
}
