from asset_analyzer import AssetAnalyzer
from constants import Constants
import logging

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
constants = Constants()

def welcome_user():
    """
    Display welcome message and ask the user for their choice
    :return: int: The user's choice, either 1, 2 or 3
    """
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
    print('This is a simple forex trading assistant / analyzer. More info can be found in readme.md')

def new_analysis_choice():
    """
    Prompts the user to choose what kind of analysis is required
    :return: int: The user's choice, either 1, 2 or 3
    """
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

# The best DRY you've ever seen ↓ :))
def print_out_analysis_results(ticker, data):
    try:
        trading_view_data = {k: v.upper() for k, v in data['trading_view'].items()}
        investing_data = {k: v.upper() for k, v in data['investing'].items()}

        print(f"Analysis for {ticker}:")
        print("- Market Sentiment: {} Short, {} Long".format(data['sentiment']['short'], data['sentiment']['long']))
        print("- TradingView Technical Analysis:")
        print("  * Weekly: {}".format(trading_view_data.get('1W', 'NA')))
        print("  * Daily: {}".format(trading_view_data.get('1D', 'NA')))
        print("  * 4 Hour: {}".format(trading_view_data.get('4h', 'NA')))
        print("  * 1 Hour: {}".format(trading_view_data.get('1h', 'NA')))
        print("  * 15 Minute: {}".format(trading_view_data.get('15m', 'NA')))
        print("  * 5 Minute: {}".format(trading_view_data.get('5m', 'NA')))
        print("- Investing.com Technical Analysis:")
        print("  * Weekly: {}".format(investing_data.get('1W', 'NA')))
        print("  * Daily: {}".format(investing_data.get('1D', 'NA')))
        print("  * 1 Hour: {}".format(investing_data.get('1H', 'NA')))
        print("  * 15 Minute: {}".format(investing_data.get('15M', 'NA')))
        print("  * 5 Minute: {}".format(investing_data.get('5M', 'NA')))
    except:
        print("Error while trying to print out the analysis ")


def ask_user_for_ticker():
    while True:
        ticker = input("Please enter a ticker to analyse: ")
        if ticker.upper() in constants.known_forex_tickers:  # Use the object to access the property
            return ticker
        else:
            print("This ticker is not recognized. Results may not be complete \nTo continue, enter 'Y'"
                    "\nTo select a new ticker, enter 'N'. \nTo print out list of recognized tickers, enter 'T'.")
            while True:
                choice = input('Your choice: ')
                if choice.upper() == "Y":
                    return ticker
                elif choice.upper() == "T":
                    print(constants.known_forex_tickers)
                    break
                elif choice.upper() == "N":
                    break


def run_program():
    """
    Run the main program loop. This involves displaying the menu,
    handling the user's choice and running the appropriate analysis
    """
    try:
        menu_choice = welcome_user()

        while menu_choice != 3: # 3 == end of program
            if menu_choice == 1: # User wants to start new analysis
                analyze_choice = new_analysis_choice() # user selects between types of analysis

                while analyze_choice != 3: # 3 == return to main menu
                    if analyze_choice == 1: # Single ticker analysis
                        ticker = ask_user_for_ticker()
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

            elif menu_choice == 2: # User wants to print help
                print_help()
                input("Press enter to return to main menu ")
                menu_choice = welcome_user()

        #Menu choice == 3 ↓
        print("End of program")

    except Exception as e:
        print("Oops, some unexpected error occured. \nProgram shutting down")
        logger.error('Error: %s', e)





if __name__ == "__main__":
    run_program()



