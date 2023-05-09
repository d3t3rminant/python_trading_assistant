from asset_analyzer import AssetAnalyzer
from constants import Constants
import logging

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def welcome_user():
    print("*** Welcome to Forex Trading Assistent 1.0 *** \nTo start analysis, enter '1'. \nTo print help, enter '2' \nTo "
          "exit the program, enter '3'")
    while True:
        try:
            choice = int(input("Your selection: "))
            if choice in [1,2,3]:
                return choice
            else:
                print("\nInvalid input, please try again")
        except ValueError:
            print("\nPlease enter a valid number")


def print_help():
    print('This is a simple forex trading assistant / analyzer. ')

def new_analysis_choice():
    print("To analyze new ticker, enter 1. To see most trending pairs, enter 2. To return to main menu, enter 3: ")

    while True:
        try:
            choice = int(input("Your selection: "))
            if choice in [1,2,3]:
                return choice
            else:
                print("\nInvalid input, please try again")
        except ValueError:
            print("\nPlease enter a valid number")


def print_out_analysis_results(ticker, data):
    print(f"Analysis for {ticker}:")
    print("- Market Sentiment: {} Short, {} Long".format(data['sentiment']['short'], data['sentiment']['long']))
    print("- TradingView Technical Analysis:")
    print("  * Weekly: {}".format(data['trading_view']['1W'].upper()))
    print("  * Daily: {}".format(data['trading_view']['1D'].upper()))
    print("  * 4 Hour: {}".format(data['trading_view']['4h'].capitalize()))
    print("  * 1 Hour: {}".format(data['trading_view']['1h'].capitalize()))
    print("  * 15 Minute: {}".format(data['trading_view']['15m'].capitalize()))
    print("  * 5 Minute: {}".format(data['trading_view']['5m'].capitalize()))
    print("- Investing.com Technical Analysis:")
    print("  * Weekly: {}".format(data['investing']['1W'].upper()))
    print("  * Daily: {}".format(data['investing']['1D'].upper()))
    print("  * 1 Hour: {}".format(data['investing']['1H'].capitalize()))
    print("  * 15 Minute: {}".format(data['investing']['15M'].capitalize()))
    print("  * 5 Minute: {}".format(data['investing']['5M'].capitalize()))




def run_program():
    try:
        menu_choice = welcome_user()

        while menu_choice != 3: # 3 == end of program
            if menu_choice == 1: # User wants to start new analysis
                analyze_choice = new_analysis_choice() # user selects between types of analysis

                while analyze_choice != 3: # 3 == return to main menu
                    if analyze_choice == 1: # Single ticker analysis
                        ticker = input("Enter a ticker to analyze: ")
                        asset_analyzer = AssetAnalyzer()
                        analysis_results = asset_analyzer.analyze_ticker(ticker)
                        print_out_analysis_results(ticker, analysis_results)

                        analyze_choice = new_analysis_choice()

                    elif analyze_choice == 2: # Most trending assets
                        print("Function not ready yet")
                        analyze_choice = new_analysis_choice()

                    else: # Invalid choice
                        print("Invalid choice. Please try again.")
                        analyze_choice = new_analysis_choice()

                menu_choice = welcome_user() # return to main menu

            elif menu_choice == 2: # User wants help
                print_help()
                input("Press enter to return to main menu ")
                menu_choice = welcome_user()

        print("End of program")
    except Exception as e:
        print("Oops, some unexpected error occured. ")
        logging.error('Error: ', e)









if __name__ == "__main__":
    run_program()



