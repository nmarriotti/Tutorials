class exampleClass:
	name = "Nick Marriotti"
	age = 28
	
	def thisMethod(self):
		return "Hey this method worked"
		

def main():
	exampleObject = exampleClass()
	print(exampleObject.thisMethod())

if __name__ == "__main__":
	main()