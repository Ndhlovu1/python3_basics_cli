#The Code below is built to have 
def move_messages(txt_msgs,sent_msgs):
    #Because we myt not know the total number of items in the list a WHile loop is best to use
    while txt_msgs:
        #Create a variable that is going to be keeping track of the items being removed from the txt_msgs
        current_msg =txt_msgs.pop()
        #Pass/add that variable to the sendmsgs list
        sent_msgs.append(current_msg)
#The function below is used to show all messages sent.
#Pass the sent_msgs list as it is supposed to be having data from the txt_msgs list
def show_messages(sent_msgs):
    print("*****************The Following Messages have been Sent*****************")
    for msg in sent_msgs:
        print(f"{msg}")

def send_messages(txt_msges):
    print("Below is a Copy of all the Messages\n")
    for msg in txt_msges:
        print(msg)

txt_msges = ["I'll call you back shortly", "Call me later, i can't talk","Call me in 30min"]
sent_msgs = []
send_messages(txt_msges[:])
move_messages(txt_msges,sent_msgs)
show_messages(sent_msgs)
