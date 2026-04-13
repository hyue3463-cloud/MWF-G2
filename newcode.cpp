#include <splashkit.h>

int main()
{
    string game_timer = "Game Timer";

    int screen_width = 800;
    int screen_height = 600;
    int spider_radius = 25;
    int spider_speed = 3;

    int fly_radius = 3;

    int x = screen_width / 2;
    int y = screen_height / 2;

    int fly_x = rnd(800);
    int fly_y = rnd(600);
    bool fly_appeared = false;
    long appear_at_time = 1000 + rnd(2000);
    open_window("Fly Catch", screen_width, screen_height);

    create_timer(game_timer);
    start_timer(game_timer);

    while (!quit_requested())
    {
        if (key_down(RIGHT_KEY) && x + spider_radius < screen_width)
        {
            x += spider_speed;
        }

        if (key_down(LEFT_KEY) && x - spider_radius > 0)
        {
            x -= spider_speed;
        }
        if (!fly_appeared && timer_ticks(game_timer) > appear_at_time)
        {
            fly_appeared = true;
            fly_x = rnd(screen_width);
            fly_y = rnd(screen_height);
        }

        clear_screen(color_white());
        fill_circle(color_black(), x, y, spider_radius);

        if (fly_appeared)
        {
            fill_circle(color_dark_green(), fly_x, fly_y, fly_radius);
        }

        refresh_screen(60);
        process_events();
    }
}