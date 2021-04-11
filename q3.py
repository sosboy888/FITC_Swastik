# Python3 Program to find
# best buying and selling days

def productBuySell(price, n):
	
	
	if (n==1):
		return
	
	
	i = 0
	while (i<n-1):
		
	
		while (i<n-1 and price[i+1]<=price[i]):
			i += 1
		
		
		if (i == n - 1):
			break
		
		# Store the index of minima
		buy = i
		i = i+1
		
		
		while (i<n and price[i]>=price[i-1]):
			i += 1
			
		# Store the index of maxima
		sell = i-1
		
		print("Buy on day: ",buy,"\t",
				"Sell on day: ",sell)
		
# Driver code

# product prices on consecutive days
price = [100, 180, 260, 310, 40, 535, 695]
n = len(price)

# Fucntion call
productBuySell(price, n)


