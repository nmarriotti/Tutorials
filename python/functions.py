def main():
	name = "Nick"
	greeting(name)

def greeting(yourname):
	print("Hello {}, your name was passed into this function".format(yourname))

if __name__ == "__main__":
	main()