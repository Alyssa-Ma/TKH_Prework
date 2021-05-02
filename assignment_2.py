#Alyssa Ma Assignment_2
#compare given list to 25, print if over or under 25

#given over under list
over_under_list = [1, 45, 32, 21, 5, 17, 43, 93]

#for the number of elements in list, loop through
for num in over_under_list:
    #if 25 is greater than the number, it is over
    if num > 25:
        print ("over")
    #equality case
    elif num == 25:
        print ("equal")
    #else it is under
    else:
        print ("under")