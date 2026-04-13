#include "splashkit.h"

int main()
{
    string line;
    int choice;
    string song_name;
    open_audio();
    do
    {
        write_line("Welcome to my simple music player");
        write_line();
        write_line("1: Load song");
        write_line("2: Play song");
        write_line("3: Stop song");
        write_line("4: Quit");
        write("Option: ");
        line = read_line();

        while (!is_integer(line))
        {
            write_line("Please enter a whole number");
            write("Enter your choice: ");
            line = read_line();
        }

        choice = convert_to_integer(line);
        write_line();

        switch (choice)
        {
        case 1:
            write("What is the name of the song: ");
            song_name = read_line();
            write("Path to the file: ");
            line = read_line();

            load_music(song_name, line);
            if (has_music(song_name))
            {
                write_line("Loading " + line + "passed!");
            }
            else
            {
                write_line("Loading " + line + " failed!");
            }
            break;

        case 2:
            if (has_music(song_name))
            {
                write("What is the name of the song: ");
                song_name = read_line();
                play_music(song_name);
                write_line("(music starts playing)");
            }
            else
            {
                write("What is the name of the song: ");
                song_name = read_line();
                write_line("there is nothing called" + song_name + "loaded");
            }
            break;

        case 3:
            if (music_playing())
            {
                stop_music();
                write_line("Music stopped.");
            }
            else
            {
                write_line("No music is playing.");
            }
            break;

        case 4:
            write_line("Bye");
            break;

        default:
            write_line("Invalid option!");
        }
        write_line();
    } while (choice != 4);

    close_audio();
    return 0;
}