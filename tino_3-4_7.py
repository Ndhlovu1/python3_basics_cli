#Guest List

#Download the

guest_names = ['Oscar', 'Clemens', 'Dragons']

message = "Good day, we(Ndhlovu Inc.) invited to the annual gathering event."

print("Dear ", guest_names[0], "\n",message)

print("")

print("Dear ", guest_names[1], "\n",message)

print("")

print("Dear ", guest_names[2], "\n",message)

print("")
print("Apologies but ",guest_names[2]," [2] can't make it.")

#Replace the data that's showing on the list by removing the guest whose no longer be attending
guest_names[2] = "Tino"
print("Below is the Updated List of Guests:\n")

print("Dear ", guest_names[0], "\n",message)

print("")

print("Dear ", guest_names[1], "\n",message)

print("")

print("Dear ", guest_names[2], "\n",message)
print("")

#Inform the guests of the Current changes in the Number of people that will come
new_msg = "Good Day, We'd like to inform you that the number of guests has increased!"

#Add 3 more Users
guest_names.insert(0, "Rachel")
guest_names.insert(2, "Pena")
guest_names.append("Tatenda")

print("New Guest List: \n \t",guest_names)

print("")

print("Dear ",guest_names[0],"\t", new_msg)
print("")

print("Dear ",guest_names[1],"\t", new_msg)
print("")

print("Dear ",guest_names[2],"\t", new_msg)
print("")

print("Dear ",guest_names[3],"\t", new_msg)
print("")

print("Dear ",guest_names[4],"\t", new_msg)
print("")

print("Dear ",guest_names[5],"\t", new_msg)

#Print a message that tells you that ony two people are currently invited to the table
cancel_msg = "Apologies but you are no longer invited to the dinner."
print("\n Full Guest List: \n",guest_names,"\n")

removed_name1 = guest_names.pop(0)
print("Dear \t", removed_name1, " You have been uninvited.\n")
removed_name2 = guest_names.pop(1)
print("Dear \t", removed_name2, " You have been uninvited. \n")
removed_name3 = guest_names.pop(2)
print("Dear \t", removed_name3, " You have been uninvited.\n")

removed_name4 = guest_names.pop(-1)

print("Dear \t", removed_name1, " You have been uninvited.\n")

print("\n", "\n", "THE FOLLOWING PEOPLE ARE STILL ATTENDING.", len(guest_names), "\n",guest_names)

del guest_names[0]
del guest_names[-1]


print("\n", "\n", "THE FOLLOWING PEOPLE ARE STILL ATTENDING.", len(guest_names), "\n",guest_names)
