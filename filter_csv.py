# write a script that reads data.cvc, filters rows with age > 25, and writes them to filtered.cvc using dictreader and disctwriter.


import csv

try:
    with open("data.csv", "r") as infile:
        reader = csv.DictReader(infile)
        rows = []

        for row in reader:
            try:
                if int(row["Age"]) > 25:
                    rows.append(row)
            except ValueError:
                print(f"Invalid age value in row: {row}")

    with open("filtered.csv", "w", newline="") as outfile:
        fieldnames = ["Name", "Age", "City"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

    print("Filtered data written to filtered.csv successfully!")

except FileNotFoundError:
    print("Error: 'data.csv' file not found.")
except KeyError:
    print("Error: 'Age' column missing in data.csv.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
