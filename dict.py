'''
Created a menu that will calculate cost of your meal and print a recept with change
'''

prices = {
    "beef": 3.0,
    "chicken": 3.5,
    "cheese" : 1.5,
    "veggie" : 2.0,
    "salad" : 1.5,
    "soup" : 2.0,
    "garlic bread" : 1.0,
    "fries" : 0.5,
    "juice" : 2.0,
    "soda" : 1.5,
    "bottled water" : 1.0
}
print(prices)

#User input from the menu
sandwich = input("Choose a sandwich from : [beef, chicken, cheese, veggie]: ")
side_dish = input("Choose a side dish from : [salad, soup, garlic bread, fries]: ")
drink = input("Choose a drink from: [juice,soda, bottled water ]: ")
cash = int(input("Please enter cash in $: "))

#Computation of the recept
total = prices.get(sandwich) + prices.get(side_dish) + prices.get(drink)
print("Your Total is: ", total)
change = cash - total
print("Your Change is: ", change)

#Receipt
print("You chose ", sandwich, " $$ " , prices.get(sandwich), " ," , side_dish, " $$ ", prices.get(side_dish), " $$ ", drink , " $$ " , prices.get(drink))
