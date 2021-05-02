#Alyssa Ma Assignment_4
#function to take lsit of names and print the longest name 

#code from previous assignment
def longest_name(names_list):
    #variable to hold longest name
    longest_name = ""

    #loop through the names
    for name in names_list:
        #if current name length is greater than the current greatest
        if len(name) > len(longest_name):
            #set to new longest
            longest_name = name
    #return the longest name
    return longest_name

#sample list
names_list = ["fa", "ewaf", "fe", "wert", "wefoi"]

#call function and print
big_name = longest_name(names_list)
print (big_name)