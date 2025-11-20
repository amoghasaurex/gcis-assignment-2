# Simple Food Ordering Program
# GCIS 123 – Assignment 3
# Amogh - 434003103
# add your name and uid
# add your name and uid


menu = {
    "Drinks": {
        "Cola" : 5.0, 
        "Juice": 7.0
        
    },
    "Entrees": {
        "Burger": 20.0,
          "Pizza": 25.0
    },
    "Sides": {
        "Fries": 8.0, 
        "Salad": 10.0
    }
}



def show_menu():
    """
    This function buits a menu display for the user to see the available items.
    """
    print("\n----MENU----")
    for category, items in menu.items():
        print(f"\n{category}:")
        for name, price in items.items():
            print(f"  {name} - {price} AED")
    print("----------------------------")



def get_item(category):
    """
    This functions asks the user to choose an item from a specific category.
    it returns the selected item as a string.
    and in case the user enters things wrong it will return the empty string.
    """
    while True:
        choice = input(f"Choose a {category} (press Enter to skip): ").strip()

        if choice == "":
            return ""
        
        choice = choice.title()


        if choice in menu[category]:
            return choice
        print("Invalid choice. Please try again.")



def create_combo():
    """
    This function creates a  combo by asking the user for a drink,
    entree and side, it returns a dictionary with combo details.
    """

    print("\n--------Create a Combo--------")

    drink = get_item("Drinks")
    entree = get_item("Entrees")
    side = get_item("Sides")

    total = 0
    if drink:
        total += menu["Drinks"][drink]
    if entree:
        total += menu["Entrees"][entree]
    if side:
        total += menu["Sides"][side]

    return {
        "Drink": drink,
        "Entree": entree,
        "Side": side,
        "Total": total
    }



def print_receipt(combos):
    """
    this function prints the receipt for all combos ordered and shows the final total amount.
    """
    print("\n========= RECEIPT =========")

    final_total = 0
    count = 1   

    for combo in combos:
        print(f"\nCombo {count}:")
        print(f"  Drink:  {combo['Drink'] or 'None'}")
        print(f"  Entree: {combo['Entree'] or 'None'}")
        print(f"  Side:   {combo['Side'] or 'None'}")
        print(f"  Combo Total: {combo['Total']} AED")

        final_total += combo["Total"]
        count += 1

    print("\nFinal Amount:", final_total, "AED")
    print("===========================")
    


def main():
    """
    This is the main function that runs the food ordering program.
    """
    show_menu()

    all_combos = []

    while True:
        combo = create_combo()
        if combo["Total"] == 0:
            print("No valid items selected. Combo not added.")
        else:
            all_combos.append(combo)
            print("\nCombo added successfully.")

        again = input("\nAdd another combo? (y/n): ").strip().lower()
        if again != "y":
            break

    print_receipt(all_combos)


# Run the program
main()

