#include <iostream>

/*
return-type function-name(parameter1, parameter2, ...)
{
    // function-body
}
*/

// you can also declare the function but optional
// Function declaration, is done to tell the compiler about the existence of the function.
// Function's return type, its name & parameter list is mentioned.
// Function body is written in its definition.
int sum (int x, int y);

int sum(int x, int y){
    return x + y;
}

void call_by_value(int x){
    x = x + 6;
}

void call_by_reference(int *x){
    *x = *x + 6;
}

int main()
{
    std::cout << "3 + 2 = " << sum(3, 2) << "\n"; // 3 + 2 = 5

    int z = 0;
    call_by_value(z); // will add 6 to a local variable but z still zero
    std::cout << "z = " << z << "\n"; // z = 0
    call_by_reference(&z); // will add 6 and affect z
    std::cout << "z = " << z << "\n"; // z = 6

    return 0;
}
