
    
all_stocks = {
        'Amazon' : 3000,
        'Apple' : 100,
        'Facebook' : 250,
        'Google' : 1400,
        'Microsoft' : 200
        }
    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
name = input("What is your name?")

    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
amount = int(input("How much would you like to invest? $"))

    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
if stock_name == 'Amazon':
    stocks = amazon
elif stock_name == "Apple":
    stocks = apple
elif stock_name == "Facebook":
    stocks = fb
elif stock_name == "Google":
    stocks = google
elif stock_name == "Microsoft":
    stocks = msft
else:
        print("You have entered an invalid stock name")
    
number_stocks = amount // all_stocks[stock_name]  

    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
print(f'{name} has ${amount} to invest and can buy {number_stocks} shares of {stock_name} at the current price of ${all_stocks[stock_name]}.')
# stock_purchases()
    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.
#stock_purchases()