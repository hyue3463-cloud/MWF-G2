#include "splashkit.h"

string read_string(string prompt)
{
  write(prompt);
  return read_line();
}

int read_integer(string prompt)
{
  string input = read_string(prompt);
  while (!is_integer(input))
  {
    write_line("Please enter a whole number");
    input = read_string(prompt);
  }
  return to_integer(input);
}

int read_integer(string prompt, int low, int high)
{
  int input = read_integer(prompt);
  while (input < 0 || input > 100)
  {
    write_line("Please enter a value between 0 and 100");
    input = read_integer(prompt);
  }
  return input;
}

bool perform_guess(int guess_number, int target)
{
  int guess;

  guess = read_integer("Guess " + to_string(guess_number) + ": ");

  if (target < guess)
  {
    write_line("The number is less than " + to_string(guess));
  }
  else if (target > guess)
  {
    write_line("The number is larger than " + to_string(guess)); 
  }
  else
  {
    write_line("Well done... the number was " + to_string(guess));
  }

  return guess == target;
}

void print_line(int length)
{
  int i = 0;
  while (i < length)
  {
    write("-");
    i++;
  }
  write_line("\n");
}

const int MAX_NUMBER = 100;
const int MAX_GUESSES = 7;

void play_game()
{
  int my_number, guess_number;
  bool got_it;

  my_number = rnd(1, MAX_NUMBER);
  guess_number = 0;

  write_line("I am thinking of a number between 1 and " + to_string(MAX_NUMBER) + "\n");

  do
  {
    guess_number++;
    got_it = perform_guess(guess_number, my_number);
  } while (guess_number < MAX_GUESSES && !got_it);

  if (!got_it)
  {
    write_line("You ran out of guesses... the number was " + to_string(my_number) + "\n");

  }
  
}

int main()
{
 string again = " ";

 do
 {
  play_game();

  write_line();
  print_line(50);
  again = read_string("Do you want to play again [Y/n]? ");
 } while (again != "N" && again != "n");
 
  write_line("\nBye - enjoy the rest of your day!");
  return 0;
}