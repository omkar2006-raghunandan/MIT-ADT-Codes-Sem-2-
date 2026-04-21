# Program to open a file and handle exceptions

file_name = input("Enter filename: ")

try:
    file = open(file_name, "r")
    content = file.read()
    print("\nFile opened successfully.\n")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied. Cannot read the file.")