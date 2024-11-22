
import csv

save_data = "library_data.csv"

def save_to_file(library):
    with open(save_data, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Author", "Year", "ISBN", "Price"])
        for book in library:
            writer.writerow([book['Title'], book['Author'], book['Year'], book['ISBN'], book['Price']])
    print("Library data saved successfully!")


def load_from_file():
    library = []

    try:
        with open(save_data,mode="r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                library.append({
                    'Title': row[0],
                    'Author': row[1],
                    'Year': row[2],
                    'ISBN': row[3],
                    'Price': row[4]
                })
    except FileNotFoundError:
        print()
    return library
