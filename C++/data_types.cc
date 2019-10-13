#include <iostream>

using namespace std;

int main()
{
    // Built-in Datatypes
    char char_chr = 'A';
    float float_chr = 3.89;
    double double_chr = 6e-9;
    bool bool_chr = true;

    int int_chr = 367;
    long int int_l_chr = 34667777777666;
    short int int_s_chr = 34233;
    signed int int_si_chr = -341;
    unsigned int int_usi_chr = 324;

    // User-defined or Abstract Datatypes

   cout << "Size of char : " << sizeof(char) << endl;
   cout << "Size of int : " << sizeof(int) << endl;
   cout << "Size of short int : " << sizeof(short int) << endl;
   cout << "Size of long int : " << sizeof(long int) << endl;
   cout << "Size of float : " << sizeof(float) << endl;
   cout << "Size of double : " << sizeof(double) << endl;
   cout << "Size of wchar_t : " << sizeof(wchar_t) << endl;

   return 0;
}
