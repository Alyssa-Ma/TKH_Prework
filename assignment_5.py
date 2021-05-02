#Alyssa Ma Assignment_5
#takes in list of names and separates them into two lists based on whether their length is odd or even
#then change first letter of names in even list to b and odd list to c

#function to separate the list
def list_separator(name_list):
    #list to hold even names
    even_list = []
    #list to hold odd names
    odd_list = []
    #iterator for name
    iterator = 0

    #loop through list of names
    for element in name_list:
        #if length is even, add to even list
        if len(element) % 2 == 0:
            even_list.append(element)
        #else add to odd list
        else:
            odd_list.append(element)
    #change first letter to "b" for even list
    for name in even_list:
        name_str = even_list[iterator]
        #string for b_name
        b_name = list(name_str)
        b_name[0] = "b"
        #convert list back to string
        b_name_final = "".join(b_name)
        even_list[iterator] = b_name_final
        
        #update iteraors
        iterator += 1
    #reset iterator for next loop
    iterator = 0
    #change last letter to "c" for odd list
    for name in odd_list:
        name_str = odd_list[iterator]
        #string for b_name
        c_name = list(name_str)
        last_index = len(c_name) - 1
        c_name[last_index] = "c"
        #convert list back to string
        c_name_final = "".join(c_name)
        odd_list[iterator] = c_name_final
        
        
        #update iteraors
        iterator += 1
    #reset iterator for next loop
    iterator = 0
    #print even list
    for num in even_list:
        print (even_list[iterator])
        iterator += 1
    #reset iterator for next loop
    iterator = 0
    #print odd list
    for num in odd_list:
        print (odd_list[iterator])
        iterator += 1
    #reset iterator for next loop
    iterator = 0
    #return even list
    return even_list

#given list
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
#run function and print
even_list = list_separator(names_list)
#print even list
iterator = 0
for num in even_list:
    print (even_list[iterator])
    iterator += 1

