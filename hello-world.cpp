#include "splashkit.h"

const int HOUR = 60;
int main()
{
    string user_input;
    double age;
    write_line("Hello World");
    write_line(" - by Andrew");
    write_line(7+2);

    write("How old are you?");
    user_input = read_line();
    age = to_double(user_input);
}