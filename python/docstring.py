def main():
    message = '''    
Hello TO_NAME,
                
    Python is a widely used high-level programming language for general-purpose programming, 
created by Guido van Rossum and first released in 1991. An interpreted language, Python has 
a design philosophy which emphasizes code readability (notably using whitespace indentation 
to delimit code blocks rather than curly brackets or keywords), and a syntax which allows 
programmers to express concepts in fewer lines of code than possible in languages such as 
C++ or Java.

Thanks,
FROM_NAME
'''

    print(message.replace("TO_NAME", "Jon Smith").replace("FROM_NAME", "Nick"))

if __name__ == "__main__":
    main()