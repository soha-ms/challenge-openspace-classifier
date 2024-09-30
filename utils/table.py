import random


class Seat:

    """
    Class that defines a seat which is needed in table, openspace
    """

    def __init__(self):
        
        self.occupant = ""
        self.is_free = True
        
    def set_occupant(self,name):
        self.is_free = False
        self.occupant = name
        

    def remove_occupant(self):
        self.occupant = ""
        self.is_free = True



class Table():
    """  Class that defines a table , capacity of tha table 
         and list of seats 
    """         

    def __init__(self, capacity):
        self.capacity =  capacity
        self.seats = []
        self.teamLead = ""
        #create list of seats for eaxh table object
        for x in range(capacity):
            seat = Seat()        
            self.seats.append(seat)

    def has_free_spot(self):
        for seat in self.seats:
            if seat.is_free:
                return True
        return False
        
    
    def assign_seat(self,name):
        #set_occupant 
        #at the table  
        for seat in self.seats:
            if(seat.is_free):
                seat.set_occupant(name)
                self.capacity -= 1
                return True
        return False

    def assign_team_lead(self) :  
        #Choose random lead from assigned seats
        num = random.randint(0,len(self.seats) -1)       
        self.teamLead = self.seats[num].occupant

    def left_capacity(self):
        self.capacity -= 1
        return self.capacity

