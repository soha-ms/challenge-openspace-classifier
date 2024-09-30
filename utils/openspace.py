from utils.table import Table
import random

class OpenSpace():

    """
        This class identify how many tables are in the room 
        AND define tables object
    """

    def __init__(self,num_table,num_seat):
        self.tables = []
        #Create list of tables when initiliaze open space object
        for x in range(num_table):
           table = Table(num_seat)
           self.tables.append(table)

   #**randomly** assign people to `Seat` objects
   #in the different `Table` object
    def organize(self,names):
       random.shuffle(names)
       
       for table in self.tables: 
            seated_names = []
            for name in names:  
                if table.has_free_spot() : 
                    table.assign_seat(name)
                    seated_names.append(name) 
                elif(table.capacity == 0) : 
                    #Assign lead to a table after assign all seats
                    table.assign_team_lead()                          
                    set_difference = set(names) - set(seated_names)
                    names = list(set_difference)
                    #name.diff(seated_names))
                continue       
            
                                  
    def display(self):
        #Display all tables with assignd names
        for x in range(1,len(self.tables)+1): 
            table = self.tables[x-1] 
            print (f"Table #{x} has following people:")   
            lead = table.teamLead       
            for seat in table.seats:
                if(not seat.is_free) : 
                    if(seat.occupant == lead):
                        print ( seat.occupant + " Lead")
                    else:
                        print(seat.occupant)
                    

   #TO DO
   #def store(filename):  
   #READ ME