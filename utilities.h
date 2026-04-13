#ifndef UTILITIES_H
#define UTILITIES_H

#include "splashkit.h"

string read_string(string prompt);
int read_integer(string prompt);
int read_integer_range(string prompt, int low, int high);
bool read_boolean(string prompt);

void draw_heading_line(int width);
void draw_title(string title, int width);

int calculate_score(int goals, int behinds);

void print_menu();
void print_details(string team_name, int goals, int behinds);

#endif