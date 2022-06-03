"""
Places I plan to Visit
"""

visit =  ['Berlin','Copenhagen','Beijing', 'Dubai', 'Rwanda']
print("Places i'd like to visit ",visit,"\n")

#Use the sorted feature to temporarily print the data sorted
srtd_vist = sorted(visit)
print("Places alphabetically: ",srtd_vist)
#Below is the Same Order
print("\nStill in the same Order ",visit,"\n")
#Reverse
visit.reverse()
print("Reverse Order ",visit,"\n")
#Reverse the Reversal
visit.reverse()
print("I am Reversing Reversal the Places",visit)
#Sort
visit.sort()
print("\nSorted Order ",visit,"\n")

#Sort in reverse
visit.sort(reverse=True)
print("\nReverse Sorted Order ",visit,"\n")
