####### functions #########

# Iterate over the list to print the values
def show_equipment(equipment):
	for i in equipment:
		print (i)

# print messsage for info about available equipment		
def msg_following_equipment(equipment, contains):
	print "You have the following %s %s" % (equipment, contains)