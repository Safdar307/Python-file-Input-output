# # create a script that reads a text file input.txt countd the lines, and writes the count t0 count.txt ..

try:
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()

    line_count = len(lines)

    file = open("count.txt", "w")
    file.write(f"Number of lines: {line_count}")
    file.close()

    print("Line count written to count.txt successfully!")

except FileNotFoundError:
    print("Error: 'input.txt' file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
