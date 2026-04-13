#include "splashkit.h"
#include "utilities.h"

int read_integer_range(string prompt, int low, int high)
{
    int input = read_integer(prompt);
    while (input < low || input > high)
    {
        write_line("Please enter a value between " + to_string(low) + " and " + to_string(high));
        input = read_integer(prompt);
    }
    return input;
}

int calculate_score(int goals, int behinds)
{
    return goals * 6 + behinds;
}

void draw_heading_line(int width)
{
    write("+");

    for (int i = 0; i < width - 2; i++)
    {
        write("-");
    }

    write_line("+");
}

void draw_title(string title, int width)
{
    int spaces = width - 3 - length_of(title);

    draw_heading_line(width);
    write("| " + title);

    for (int i = 0; i < spaces; i++)
    {
        write(" ");
    }

    write_line("|");
    draw_heading_line(width);
}

void print_details(string team_name, int goals, int behinds)
{
    write_line(team_name + ":");
    write_line("   " + to_string(goals) + " Goals");
    write_line("   " + to_string(behinds) + " Behinds");
    write_line("   " + to_string(calculate_score(goals, behinds)));
}

void print_menu()
{
    draw_title("Main Menu", 26);
    write_line("1: Update goals");
    write_line("2: Update behinds");
    write_line("3: Print details");
    write_line("4: Quit");
    draw_heading_line(26);
}

bool read_boolean(string prompt)
{
    string input = read_string(prompt);

    while (input != "y" && input != "n")
    {
        write_line("Please enter y or n");
        input = read_string(prompt);
    }
    return input == "y";
}

int main()
{
    draw_title("Score Calculator", 26);
    write_line("Welcome to the AFL score calculator");

    string team_name = read_string("Enter team name: ");
    int goals = read_integer("Enter goals: ");
    int behinds = read_integer("Enter behinds: ");

    write_line("Current Score: " + to_string(calculate_score(goals, behinds)));

    bool finished = false;

    while (!finished)
    {
        print_menu();
        int option = read_integer_range("Enter Option: ", 1, 4);

        if (option == 1)
        {
            write_line("Current goals: " + to_string(goals));
            goals = read_integer("Enter new goals: ");
            write_line("Current Score: " + to_string(calculate_score(goals, behinds)));
        }

        else if (option == 2)
        {
            write_line("Current behinds: " + to_string(behinds));
            behinds = read_integer("Enter new behinds: ");
            write_line("Current Score: " + to_string(calculate_score(goals, behinds)));
        }

        else if (option == 3)
        {
            print_details(team_name, goals, behinds);
        }

        else if (option == 4)
        {
            bool quit = read_boolean("Are you sure you want to quit? [y/n]: ");

            if (quit)
            {
                write_line("Bye!");
                finished = true;
            }
        }
    }
    return 0;
}