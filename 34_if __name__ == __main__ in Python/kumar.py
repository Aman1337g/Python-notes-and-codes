import aman
aman.welcome()

'''
OUTPUT

hello duniya !!
Enter your name : aman
Welcome, aman to this 100 days of code !!
'''

'''
OUTPUT without [ if __name__ == "__main__" ]

hello duniya !!
Enter your name : aman
Welcome, aman to this 100 days of code !!
hello duniya !!
Enter your name : kumar
Welcome, kumar to this 100 days of code !!
'''


'''
The __pycache__ directory is a directory that is automatically created by Python to store compiled bytecode files, which are 
generated to improve the performance of Python programs.

When a Python module is imported or executed, Python compiles the source code into bytecode, which is a lower-level 
representation of the code that can be executed more quickly. The bytecode is then stored in the __pycache__ directory, which
is located in the same directory as the module.

The bytecode is created with the extension .pyc and contains instructions that can be executed directly by the Python 
interpreter. The bytecode files are automatically generated and updated by Python as needed.

The purpose of the __pycache__ directory is to speed up the importing of Python modules, as the interpreter can load the 
precompiled bytecode from the __pycache__ directory instead of having to recompile the source code every time the module is imported.
'''
