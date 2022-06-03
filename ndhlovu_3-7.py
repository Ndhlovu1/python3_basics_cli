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

