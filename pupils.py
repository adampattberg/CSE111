import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

# def extract_birtdate(student):
#     return student[BIRTHDATE_INDEX]

def main():
    students_list = read_compound_list("pupils.csv")

    # get_birthdate = lambda student : student[BIRTHDATE_INDEX]
    # get_surname = lambda student : student[SURNAME_INDEX]
    # get_monthday = lambda student : student[BIRTHDATE_INDEX][5:]

    # students_list_birthdate = sorted(students_list, key=get_birthdate)
    # students_list_surname = sorted(students_list, key=get_surname)
    # students_list_monthday = sorted(students_list, key=get_monthday)
    # print_list(students_list_birthdate)

    display_sorted(students_list, lambda student : student[BIRTHDATE_INDEX])
    print("======================")
    display_sorted(students_list, lambda student : student[SURNAME_INDEX])
    print("======================")
    display_sorted(students_list, lambda student : student[BIRTHDATE_INDEX][5:])

def display_sorted(students):
    students_sorted = sorted(students, key=sort_key)
    print_list(students_sorted)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(data):
    for item in data:
        print(item)

if __name__ == "__main__":
    main()