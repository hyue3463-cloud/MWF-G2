#include "splashkit.h"

int main()
{
    string purpose;
    string user_input;
    double week_bfr_pur, saving;
    double goal;
    double saving_each_week;
    double remaining_need_to_save, week_to_save;

    write("What are you saving for? Enter title: ");
    purpose = read_line();
    write("How much do you need to save? Enter dollars: ");
    user_input = read_line();
    goal = to_double(user_input);

    write_line();
    write("How long before the purchase? Enter weeks: ");
    user_input = read_line();
    week_bfr_pur = to_double(user_input);

    write("How much do you have already? Enter dollars: ");
    user_input = read_line();
    saving = to_double(user_input);

    write("How much can you save each week? Enter dollars: ");
    user_input = read_line();
    saving_each_week = to_double(user_input);

    remaining_need_to_save = (goal - saving) / week_bfr_pur;

    write_line();
    write_line("For the " + purpose + ", you need to save " + to_string((int)remaining_need_to_save) + " dollars a week");

    week_to_save = (goal - saving) / saving_each_week;

    write_line("Based on current savings you will need " + to_string((int)week_to_save) + " weeks to save $" + to_string((int)goal));
}
