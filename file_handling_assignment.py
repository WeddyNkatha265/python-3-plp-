# file_handling_assignment.py

# File Creation
try:
    with open("my_file.txt", 'w') as file:
        file.write("Hello, this is the first line.\n")
        file.write("This is the second line with a number: 12345.\n")
        file.write("And this is the third line.\n")
    print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")

# File Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("File content read successfully. Here it is:")
    print(content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# File Appending
try:
    with open("my_file.txt", 'a') as file:
        file.write("Appending this fourth line.\n")
        file.write("Here is the fifth line with another number: 67890.\n")
        file.write("Finally, this is the sixth line.\n")
    print("Additional content appended successfully.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")

# Final Reading and Display
try:
    with open("my_file.txt", 'r') as file:
        content = file.read()
    print("Final file content after appending. Here it is:")
    print(content)
except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File handling operations completed.")
