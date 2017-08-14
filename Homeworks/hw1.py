from random import uniform
# Define class Portfolio
class Portfolio(object):
    def __init__(self, cash=0, stock={}, fund={}, hist=[]):
        '''Initialize dictionaries for a client's stocks and funds'''
        self.cash = float(cash)
        self.stock = stock
        self.fund = fund
        self.hist = hist

    # print function will display the client's name on one line, 
    # and her or his cash, stock & mutual funds in separate lines.
    def __str__(self): 
        '''Print the current status of a portfolio'''
        return "Cash: %s \nStock: %s \nMutual Funds: %s" %(self.cash, self.stock, self.fund)
    
    def history(self):
        '''Print the history in the time order'''
        for i in self.hist:
            print i

    def addCash(self, num):
        '''Add cash to the existing account and record it as a float.'''
        self.cash += float(num)
        self.hist.append("Cash: + %.2f" %float(num))
        return self.cash

    def withdrawCash(self, num):
        '''Withdraw cash from the existing account.'''
    	money = float(self.cash)
    	if num < money:
    		self.cash -= float(num)
    	else:
    		raise TypeError, "You cannot withdraw more money than you have!"
        self.hist.append("Cash: - %.2f" %float(num))
    	return self.cash

    def buyStock(self, number, stock):
        '''Buy stocks with existing cash in the portfolio.'''
    	self.cash -= number * stock.price
    	if stock.stock_symbol in self.stock.keys():
    		self.stock[stock.stock_symbol] += number
    	else:
    		self.stock[stock.stock_symbol] = number
    	self.hist.append("Cash: - %.2f; Stocks: + %s * %s" %(float(number * stock.price), stock.stock_symbol, number))
        print self.stock

    def buyMutualFund(self, share, fund):
        '''Buy mutual funds with existing cash in the portfolio.'''
        self.cash -= share
        if fund.fund_symbol in self.fund.keys():
            self.fund[fund.fund_symbol] += share
        else:
            self.fund[fund.fund_symbol] = share
        self.hist.append("Cash: - %.2f; Mutual Funds: + %s * %s" %(float(share), fund.fund_symbol, share))
        print self.fund       

    def sellStock(self, stock_symbol, number):
        '''Sell stocks in the portfolio'''
        orgnum = float(self.stock[stock_symbol])
        if number < orgnum:
            self.stock[stock_symbol] -= float(number)
            print "%s\n%s" %(self.cash, self.stock)
        elif number == orgnum:
            del self.stock[stock_symbol]
            print "%s\n%s" %(self.cash, self.stock)
        else:
            raise TypeError, "You cannot sell more stocks than you have!"
        lower = float(0.5) * All_stocks[stock_symbol]
        upper = float(1.5) * All_stocks[stock_symbol]
        change = number * uniform(lower, upper)
        self.cash += change
        self.hist.append("Cash: + %.2f; Stocks: - %s * %s" %(float(change), stock_symbol, number))

    def sellMutualFund(self, fund_symbol, share):
        '''Sell mutual funds in the portfolio'''
        orgshare = float(self.fund[fund_symbol])
        if share < orgshare:
            self.fund[fund_symbol] -= float(share)
            print "%s\n%s" %(self.cash, self.fund)
        elif share == orgshare:
            del self.fund[fund_symbol]
            print "%s\n%s" %(self.cash, self.fund)
        else:
            raise TypeError, "You cannot sell more mutual funds than you have!"
        change = share * uniform(0.9, 1.2)
        self.cash += change
        self.hist.append("Cash: + %.2f; Mutual Funds: - %s * %s" %(float(change), fund_symbol, share))

# Define class Stock
All_stocks = {}
class Stock(object):
	def __init__(self, price, stock_symbol):
		self.price = float(price)
		self.stock_symbol = stock_symbol
		All_stocks[stock_symbol] = price

    # Print function will display the stock's name and price in one line.
	def __str__(self):
		return "%s: %s" %(self.stock_symbol, self.price)

# Define class Mutual Fund
class MutualFund(object):
	def __init__(self, fund_symbol):
		self.fund_symbol = fund_symbol
    
    # Print function will display the fund's name.
	def __str__(self):
		return self.fund_symbol

# -------- Test the codes -------
# Basic requirements
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio)
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellMutualFund("BRT", 7.3) #Sells 7.3 shares of BRT
print(portfolio) # "BRT" should disappear from the porfolio now
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions ordered by time

# -------- expect an error --------
portfolio.sellStock("HFH", 6) 
portfolio.sellMutualFund("BRT", 14.3)
portfolio.withdrawCash(500)