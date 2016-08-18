from questions_sr2 import * # holds all the question and some functionality
from classes_sr2 import * # holds all the classes
from functions_sr2 import * # holds all the functions 

####### variables #########
#set emply lists to hold the equipment individually
datarooms = [] 
racks = [] 
dataroom_racks = {}


#main
a = "0"			
while a != "stop":
	a = start_question()

#the create part	
	if a == "dr":
		dataroom = Dataroom()
		datarooms.append(dataroom.name)
		
	elif a == "rack":
		rack = Rack()
		racks.append(rack.name)
		dataroom_racks[rack.dataroom] = rack.name
			
# The show part		
	elif a == "show_datarooms":
		show_equipment(datarooms)
	
	elif a == "show_racks":
		show_equipment(racks)
		
	else:
		pass

# the alter part
	if a == "alter_datarooms":
		msg_following_equipment("datarooms", datarooms)
		other_questions("which_equipment")
		
	elif a == "alter_racks":
		pass
		
	
	else:
		pass

		
print ("Datarooms", datarooms,"\nRacks", racks, "\nRacks in datarooms", dataroom_racks)
