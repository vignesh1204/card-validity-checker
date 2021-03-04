def creditCard(cardNumber):
	cardSum = 0
	altNum = False
	for i in range(len(cardNumber) - 1, -1, -1):
		d = int(cardNumber[i])
		if (altNum):
			d *= 2
		cardSum += d // 10
		cardSum += d % 10
		altNum = not altNum
	return ((cardSum % 10) == 0)

if __name__=="__main__":
	inp = input('Enter card number :')
	valid = creditCard(inp)
	if (valid):
		print("This is a valid card")
	else:
		print("This is not a valid card")
