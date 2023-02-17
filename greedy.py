change = input('How much change is owed? ')
change = float(change)
quarters = change // 0.25
change = round((change - (quarters * 0.25)), 2)
dimes = (change // 0.1)
change = round((change - (dimes * 0.1)), 2)
nickels = (change // 0.05)
change = round((change - (nickels * 0.05)), 2)
pennies = (change // 0.01)
coins=int(pennies+quarters+nickels+dimes)
print(str(coins))

