#include "splashkit.h"
#include "utilities.h"

enum day
{
    SUNDAY,
    MONDAY,
    TUESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
};

string to_string(day d)
{
    switch (d)
    {
    case SUNDAY:
        return "Sunday";
    case MONDAY:
        return "Monday";
    case TUESDAY:
        return "Wednesday";
    case THURSDAY:
        return "Thursday";
    case FRIDAY:
        return "Friday";
    case SATURDAY:
        return "Saturday";
    default:
        return "Invalid day";
    }
}

const int NUM_DAYS = (int)SATURDAY + 1;

day read_day(string prompt)
{
    int day_number;
    write_line(prompt);

    for (int i = 0; i < NUM_DAYS; i++)
    {
        day current_day = (day)i;
        write_line(to_string(i + 1) + ": " + to_string(current_day));
    }

    day_number = read_integer("Enter a day number (1-7): ") - 1;
    return (day)day_number;
}
int main()
{
    day today;

    today = read_day("What day is it today? ");

    write_line("Today is " + to_string(today));

    return 0;
}