# Ask input what needs to be created
def start_question():

	sq_input = raw_input(
	"What would you like to do?"
	"\n1. Would you like to create something?"
	"\n2.Would you like to have a look at what you have?"
	"\n3.Would you like to alter something?"
	"\n\nPress 0 to quit"
	"\n"
	)
	
	if sq_input == "0":
		return("stop")
	
	elif sq_input == "1":
		create_input = raw_input(
		"\nWhat would you like to create?"
		"\n1. Dataroom."
		"\n2. Rack."
		"\n"
		)
		
		if create_input == "1":	
			return ("dr")
			
		elif create_input == "2":
			return ("rack")
		
		else:
			pass
	
	elif sq_input == "2":
		show = raw_input(
		"\nWhat would you like to see?"
		"\n1. Datarooms."
		"\n2. Racks."
		"\n"
		)
		
		if show == "1":
			return("show_datarooms")
			
		elif show == "2":
			return("show_racks")
	
		else:
			pass
	
	elif sq_input == "3":
		alter = raw_input(
		"\nWhat would you like to alter?"
		"\n1. A dataroom?"
		"\n2. A rack?"
		"\n"
		)
		
		if alter == "1":
			return ("alter_datarooms")
			
		elif alter == "2":
			return ("alter_racks")
	
	else:
		pass	
			
	
#all other questions that can be asked (usually to set class-attributes)
def other_questions(i):
	
	if i == "name":
		name_question = raw_input("What is the name?\n")
		return (name_question)
		
	elif i == "which_room":
		which_room = raw_input(
			"\nIs this piece of equipment located in a dataroom?"
			"\nY(es)"
			"\nN(o)"
			)
			
		if which_room == "y":
			which_room = raw_input("In which room is it located?\n")
			return (which_room)
		
		else:
			return ("none")
			
	elif i == "which_equipment":
		which_equipment = raw_input("\nEnter the name of the device you would like to change\n")
		return (which_equipment)
		
	else:
		return()
		
	