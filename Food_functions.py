import pprint
import pyfiglet
from rich.console import Console
from rich.table import Table
from currency_converter import CurrencyConverter
from Currency import converter
c = CurrencyConverter()

console = Console()
def menutable():
    Food = {
        'Nasi Lemak': converter(3.00),
        'Nasi Goreng': converter(3.50),
        'Roti Chanai':  converter(2.50),
        'Pani Puri': converter(2.25),
        'Curly Fries': converter(1.50),
        'Biryani': converter(4.00),
        'Satay Chicken': converter(3.50),
        'Chicken Tikka Masala': converter(4.50),
        'Lamb Ribs': converter(5.00),
        'Fries': converter(1.25),
        }

    Drinks = {
        'Prime': converter(2.00),
        'Water': converter(0.50),
        'Sparkling Water': converter(1.00),
        'Milkshake': converter(2.00),
        'Mango Lassi': converter(1.75),
        'Lemonade': converter(1.50),
        'Coca Cola': converter(1.00),
        'Jasmine Tea': converter(0.80),
        'Bubble Tea': converter(2.00),
        'Mojito': converter(1.50), 
    }     
    
    
    result = pyfiglet.figlet_format("MENU")
    console.print(result, style="bold red", justify="center")


    # TABLE CONFIG

    table = Table(show_header=True,show_edge=True,show_lines=False, header_style="bold red")
    table.add_column("Meals", width=20)
    table.add_column("Price", width=12, justify="right")
    table.add_column("Drinks", width=20)
    table.add_column("Price", width=12, justify="right")

    # ROWS

    table.add_row(
        "Nasi Lemak", str(converter(3.00)), "Water", str(converter(0.50))
    )
    table.add_row(
        "Nasi Goreng", str(converter(3.50)), "Prime", str(converter(2.00))
    )
    table.add_row(
        "Roti Chanai", str(converter(2.50)), "Sparkling Water", str(converter(1.00))
    )
    table.add_row(
        "Pani Puri", str(converter(2.25)), "Milkshake", str(converter(2.00))
    )
    table.add_row(
        "Biryani", str(converter(4.00)), "Chai", str(converter(1.00))
    )
    table.add_row(
        "Satay Chicken", str(converter(3.50)), "Lemonade", str(converter(1.50))
    )
    table.add_row(
        "Chicken Tikka Masala", str(converter(4.50)), "Coca Cola", str(converter(1.00))
    )
    table.add_row(
        "Lamb Ribs", str(converter(5.00)), "Jasmine Tea", str(converter(0.80))
    )
    table.add_row(
        "Fries", str(converter(1.25)), "Bubble Tea", str(converter(2.00))
    )
    table.add_row(
        "Curly Fries", str(converter(1.50)), "Mojito", str(converter(2.50))
    )
    
    console.print(table, justify="center")


    shopping_cart = []
    print("What would you like to buy: ")
    print("Type # when finished")
    shop = True
    while shop == True:
        shopping_cart.append(input())
        if '#' in shopping_cart:
            print("Items added to Shopping Cart")
            shopping_cart.remove("#")
            print(shopping_cart)
            break
        for x in shopping_cart:
            if x not in Food and x not in Drinks:
             shopping_cart.remove(x)

            
