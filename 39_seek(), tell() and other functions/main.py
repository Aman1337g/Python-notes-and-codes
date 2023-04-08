with open('spidey.txt', 'r') as f:
    print(f"Current seek position : {f.tell()}")
    data = f.read()
    print("Initial data :", data)
    f.seek(5)
    print(f"Final seek position : {f.tell()}")
    data = f. read(5)  # reading 5 characters
    print('Reading 5 characters from the seeked position :', data)
'''
OUTPUT

Current seek position : 0
Initial data : 1234567amankumar Gupta
Final seek position : 5
67ama
'''
