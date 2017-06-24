def main():
	myNumber = 10
	myString = "Nick Marriotti"
	myFloat = 19.99
	myBoolean = True

	print(myString + " has " + str(myNumber) + " dollars")
	print("{name} has {money} dollars".format(name=myString, money=myNumber))


if __name__ == "__main__":
	main()