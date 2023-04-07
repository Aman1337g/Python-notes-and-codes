import os


if (not os.path.exists("Data")):
    os.mkdir("Data")

# Creating 5 folders
for i in range(5):
    os.mkdir(f"Data/Day {i}")
    # for folders name to start with 1 using os.rename(source, destination)
    os.rename(f"Data/Day {i}", f"Data/Day {i+1}")
