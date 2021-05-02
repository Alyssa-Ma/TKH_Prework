#Alyssa Ma Assignment_3
#compare name lengths and print longest one

#given names list
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

#variable to hold longest name
longest_name = ""

#loop through the names
for name in names_list:
    #if current name length is greater than the current greatest
    if len(name) > len(longest_name):
        #set to new longest
        longest_name = name
    #don't need another else statement, do nothing if it's shorter
#print out longest name
print (longest_name)
