import csv
import random


class CsvRead:
    def __init__(self, file):
        try:
            file = open(file)       # Try to open the file
        except FileNotFoundError:
            print("File not found") # If the file is not found, print an error message

        self.file = file    # Store the file object
        self.reader = csv.DictReader(file)  # Create a CSV DictReader object to read the file as a dictionary


    def read(self):
        return random.choice(list(self.reader))
        # Convert the reader object to a list and return a random row from the CSV
