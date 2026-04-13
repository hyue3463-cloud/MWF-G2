#include "splashkit.h"
int main()
{
    open_window("CAT", 1000, 1000);

    clear_screen(COLOR_WHITE);
    draw_text("CEDRIC - using SplashKit shapes:", COLOR_BLACK, 50, 50);

    // Draw the face
    fill_ellipse(COLOR_LIGHT_GRAY, 100, 200, 800, 500);

    // Draw the ears
    fill_triangle(COLOR_LIGHT_GRAY, 100, 100, 600, 500, 300, 600);
    fill_triangle(COLOR_LIGHT_GRAY, 900, 100, 400, 500, 700, 600);

    // Draw the eyes
    fill_ellipse(COLOR_BLACK, 300, 300, 100, 100);
    fill_ellipse(COLOR_BLACK, 600, 300, 100, 100);

    // Draw the nose
    fill_triangle(COLOR_LIGHT_PINK, 400, 350, 600, 350, 500, 500);

    // Draw the whiskers
    fill_triangle(COLOR_BLACK, 1000, 300, 700, 450, 700, 400);
    fill_triangle(COLOR_BLACK, 1000, 500, 700, 475, 700, 525);
    fill_triangle(COLOR_BLACK, 1000, 700, 700, 550, 700, 600);
    fill_triangle(COLOR_BLACK, 0, 300, 300, 450, 300, 400);
    fill_triangle(COLOR_BLACK, 0, 500, 300, 475, 300, 525);
    fill_triangle(COLOR_BLACK, 0, 700, 300, 550, 300, 600);

    // Draw the mouth
    fill_rectangle(COLOR_ANTIQUE_WHITE, 400, 575, 200, 80);

    refresh_screen();
    delay(10000);
}