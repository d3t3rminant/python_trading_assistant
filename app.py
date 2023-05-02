import os
from asset_analyzer import AssetAnalyzer


def welcome_user():
    print("*** Welcome to Trading Assistent 1.0 *** \nTo start analysis, enter '1'. \nTo print help, enter '2' \nTo "
          "exit the program, enter '3'")
    choice = int(input("Your selection: "))
    return choice


def print_help():
    print('This is a simple trading assistant / asset analyzer. ')

def new_analysis_choice():
    choice = int(input("To analyze new ticker, enter 1. To return to main menu, enter 2: "))
    return choice




def run_program():
    menu_choice = welcome_user()

    while menu_choice != 3:
        if menu_choice == 1:
            analyze_choice = new_analysis_choice()
            if analyze_choice == 1:
                ticker = input("Enter a ticker to analyze: ")
                ticker_analyzer = AssetAnalyzer(ticker)
            else:
                menu_choice = welcome_user()

        elif menu_choice == 2:
            print_help()
            input("Press enter to return to main menu ")
            menu_choice = welcome_user()



    print("End of program")











if __name__ == "__main__":
    run_program()