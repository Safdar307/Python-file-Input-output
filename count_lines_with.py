# Using with statement.

try:
    with open("input.txt", "r") as file:
        lines = file.readlines()

    line_count = len(lines)

    with open("count.txt", "w") as file:
        file.write(f"Number of lines: {line_count}")

    print("Line count written to count.txt successfully using 'with' statement!")

except FileNotFoundError:
    print("Error: 'input.txt' file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
