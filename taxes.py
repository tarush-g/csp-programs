price = input('whats your price? ')
state = 0.04
county = 0.02
final_price = int(price)*(1+state+county)
print('state tax = ' + str(state) + '$\ncounty = ' + str(county) + '$\nfinal price = ' + str(final_price) + '$\noriginal price = ' + price + '$')
