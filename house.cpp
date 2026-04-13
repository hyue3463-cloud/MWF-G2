#include "splashkit.h"

int main()
{
    open_window("Shapes by Cedric", 1000, 1000);

    clear_screen(COLOR_LIGHT_SKY_BLUE);

    // Draw the clouds
    fill_ellipse(COLOR_WHITE_SMOKE, 20, 30, 200, 80);
    fill_ellipse(COLOR_WHITE_SMOKE, 70, 0, 100, 110);
    fill_ellipse(COLOR_WHITE_SMOKE, 535, 60, 200, 80);
    fill_ellipse(COLOR_WHITE_SMOKE, 590, 30, 100, 110);

    // Draw the ground
    fill_ellipse(COLOR_GREEN_YELLOW, -50, 400, 1500, 800);

    // Draw the walls
    fill_rectangle(COLOR_NAVAJO_WHITE, 300, 300, 200, 200);
    draw_rectangle(COLOR_PERU, 300, 300, 200, 200);
    fill_rectangle(COLOR_FLORAL_WHITE, 500, 300, 400, 200);
    draw_rectangle(COLOR_PERU, 500, 300, 400, 200);

    // Draw the roof
    fill_rectangle(COLOR_LIGHT_CORAL, 400, 150, 400, 151);
    fill_triangle(COLOR_INDIAN_RED, 250, 300, 400, 150, 550, 300);
    draw_triangle(COLOR_SADDLE_BROWN, 250, 300, 400, 150, 550, 300);
    fill_triangle(COLOR_LIGHT_CORAL, 650, 300, 800, 150, 950, 300);

    // Draw the door
    fill_rectangle(COLOR_SADDLE_BROWN, 350, 350, 100, 150);
    fill_ellipse(COLOR_DARK_GRAY, 360, 420, 10, 10);

    // Draw the window
    fill_rectangle(COLOR_CADET_BLUE, 550, 310, 270, 120);
    fill_rectangle(COLOR_POWDER_BLUE, 560, 320, 250, 100);
    refresh_screen();

    delay(10000);
    close_all_windows();
    return 0;
}