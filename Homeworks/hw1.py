from random import uniform
# Define class Portfolio
class Portfolio(object):
    def __init__(self, cash=0, stock={}, fund={}):
    	# initialize dictionaries for a client's stocks and funds.
        self.cash = float(cash)
        self.stock = stock
        self.fund = fund

    # print function will display the client's name on one line, 
    # and her or his cash, stock & mutual funds in separate lines.
    def __str__(self): 
        return "Cash: %s \nStock: %s \nMutual Funds: %s" %(self.cash, self.stock, self.fund)

    # Add cash to the existing account and record it as a float.
    def addCash(self, num):
    	self.cash += float(num)
    	return self.cash

    # Withdraw cash from the existing account.
    def withdrawCash(self, num):
    	if num < self.cash:
    		self.cash -= float(num)
    	else:
    		raise TypeError, "You cannot without more money than you have!"
    	return self.cash

    # Buy stocks with existing cash in the portfolio.
    def buyStock(self, number, stock):
    	self.cash -= number * stock.price
    	if stock.stock_symbol in self.stock.keys():
    		self.stock[stock.stock_symbol] += number
    	else:
    		self.stock[stock.stock_symbol] = number
    	print self.stock

    # Sell stocks in the portfolio
	def sellStock(self, stock_symbol, number):
		if number < self.stock[stock_symbol]:
			self.stock[stock_symbol] -= number
			print "%s\n%s" %(self.cash, self.stock)
		elif number == self.stock[stock_symbol]:
			del self.stock[stock_symbol]
			print "%s\n%s" %(self.cash, self.stock)
		else:
			raise TypeError, "You cannot sell more stocks than you have!"
		lower = float(0.5) * All_stocks[stock_symbol]
		upper = float(1.5) * All_stocks[stock_symbol]
		self.cash += number * random.uniform(lower, upper)

# Define class Stock
All_stocks = {}
class Stock(object):
	def __init__(self, price, stock_symbol):
		self.price = float(price)
		self.stock_symbol = stock_symbol
		All_stocks[stock_symbol] = price

	# print function will display the stock's name and price in one line.
	def __str__(self):
		return "%s: %s" %(self.stock_symbol, self.price)

# Define class Mutual Fund
class MutualFund(object):
	def __init__(self, fund_symbol):
		self.fund_symbol = fund_symbol

	# print function will display the fund's name.
	def __str__(self):
		return self.fund_symbol

# -------- Test the codes -------
# Create Clients' protfolio
Luwei = Portfolio()
Erin = Portfolio(1000)

# Add cash
Luwei.addCash(266)

# Withdraw cash
Erin.withdrawCash(100)

# Create stocks
s1 = Stock(20, "HFH")
s2 = Stock(10, "CHO")

# Create mutual funds
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")

# Buy stocks
Luwei.buyStock(2, s1)
Luwei.buyStock(5, s2)

# Sell stocks
Luwei.sellStock('HFH', 1)

# Buy mutual funds
Luwei.buyMutualFund(2, s1)
Luwei.buyMutualFund(5, s2)

# Sell sell mutual funds
Luwei.sellMutualFund('HFH', 1)