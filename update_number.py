import os

def increment_number(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"{file_path} not found. Creating a new file with default value 0.")
        with open(file_path, 'w') as file:
            file.write("0")

    # Read the current number from the file
    with open(file_path, 'r') as file:
        current_number = int(file.read().strip())

    # Increment the number
    new_number = current_number + 1

    # Write the new number back to the file
    with open(file_path, 'w') as file:
        file.write(str(new_number))

    print(f"Incremented number: {new_number}")

if __name__ == "__main__":
    # Specify the path to the file
    file_path = "number.txt"

    # Increment the number
    increment_number(file_path)
