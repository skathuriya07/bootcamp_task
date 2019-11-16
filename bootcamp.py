"""
written by: Shreya Kathuriya
29506751
"""
list= []    #initialising blank list to append eements entered by the user
odd_list=[]     #initialising list for odd pair
even_list=[]       #initialising list for even pairs

num_of_elements= int(input("Please enter the number of elements: "))
print("Please enter the numbers, separated by 'enter' key")

for i in range(0,num_of_elements):
    num= int(input())
    list.append(num)    #creating a list of user entered elements

for n in range(len(list)):
    for m in range(1,len(list)):
        product= list[n]*list[m]

        if product%2 == 0:      #check for even product
            even_list.append((list[n], list[m]))

        else:
            odd_list.append((list[n], list[m]))

print("pair of numbers that give even products are:", even_list)
print("pair of numbers that give odd products are:", odd_list)

