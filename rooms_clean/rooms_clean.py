filename1 = "raw_floors.txt"
filename2 = "floor1.txt"  #floor1

f1 = open(filename1, 'r')

newfile1 = open(filename2, "w+")
lines1 = list(open(filename1, 'r'))  #lines1
for i in range(0, len(lines1)):  #lines1
    new_list1 = lines1[i].replace(' Floors', '')  #new_list1, lines1
    newfile1.write(new_list1)    #new_list1

newfile1 = open("floor2.txt", "w+")   #floor2
lines2 = list(open(filename2, 'r'))  #lines2
for i in range(0, len(lines2)):      #lines2
    new_list2 = lines2[i].replace(' Floor', '')  #new_list2, lines2
    newfile1.write(new_list2)   #new_list2

newfile1 = open("floor3.txt", "w+")      #floor3
lines3 = list(open("floor2.txt", 'r'))    #lines3, floor2
for i in range(0, len(lines3)):     #lines3
    new_list3 = lines3[i].replace('Ground', '1')    #new_list3, lines3
    newfile1.write(new_list3)       #new_list3

newfile1 = open("floor4.txt", "w+")      #floor4
lines4 = list(open("floor3.txt", 'r'))   #lines4, floor3
for i in range(0, len(lines4)):     #lines4
    new_list4 = lines4[i].replace('G+1', '2')   #new_list4, lines4
    newfile1.write(new_list4)   #new_list4

newfile1 = open("floor5.txt", "w+")     #floor5
lines5 = list(open("floor4.txt", 'r'))   #lines5, floor4
for i in range(0, len(lines5)):     #lines5
    new_list5 = lines5[i].replace('G+2', '3')
    newfile1.write(new_list5)

newfile1 = open("floor6.txt", "w+")
lines6 = list(open("floor5.txt", 'r'))
for i in range(0, len(lines6)):
    new_list6 = lines6[i].replace('G+ 4+ floors', '5')
    newfile1.write(new_list6)

newfile1 = open("floor7.txt", "w+")
lines7 = list(open("floor6.txt", 'r'))
for i in range(0, len(lines7)):
    new_list7 = lines7[i].replace('G+3', '4')
    newfile1.write(new_list7)

newfile1 = open("floor8.txt", "w+")
lines8 = list(open("floor7.txt", 'r'))
for i in range(0, len(lines8)):
    new_list8 = lines8[i].replace('4+', '5')
    newfile1.write(new_list8)

f1.close()
newfile1.close()




'''
newfile1 = open("new_final_floors.txt", "w+")
new_lines = list(open("new_final_floors.txt", 'r'))
for i in range(1, len(new_lines)):
    new_list1 = new_lines[i].replace(' Floor', '')
    newfile1.write(new_list1)
'''

#newfile1.close()
