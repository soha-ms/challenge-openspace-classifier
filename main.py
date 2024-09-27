from utils.table import Table, Seat
from utils.openspace import OpenSpace

names = ["Soha","Basma","Rasmata", "Veena",
        "Yusra", "Rik","Drishya","Iza",
        "Mustafa", "Ihor","Zelim","Majid",
        "Petra","Levin","Kelli","Yeliz",
        "Martin","Kevin","ursonc",
        "Wouter","Nicolaas","Tom","Anastasiia",
        "Muntadter","Minh","Adeeba"]
numTables = 6
numSeats = 4
open_space = OpenSpace(numTables,numSeats)
open_space.organize(names)
open_space.display()

