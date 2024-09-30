from utils.openspace import OpenSpace
import csv

names1 = ["Soha","Basma","Rasmata", "Veena",
        "Yusra", "Rik","Drishya","Iza",
        "Mustafa", "Ihor","Zelim","Majid",
        "Petra","Levin","Kelli","Yeliz",
        "Martin","Kevin","ursonc",
        "Wouter","Nicolaas","Tom","Anastasiia",
        "Muntadter","Minh","Adeeba"]

with open("new_colleagues.csv", newline="") as csv_file:
    contents = csv.reader(csv_file, delimiter=" ", quotechar="|")
    names = []
    for row in contents:
        names.append(row[0])

numTables = 6
numSeats = 4
open_space = OpenSpace(numTables,numSeats)
open_space.organize(names)
open_space.display()

