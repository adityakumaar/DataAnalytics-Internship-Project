filename1 = "two_wheelers.txt"
filename2 = "four_wheelers.txt"
#filename1_1 = "new_two_wheelers1.txt"
#filename2_1 = "new_four_wheelers1.txt"
#-------------------------------------------------------------------
f1 = open(filename1, 'r')
f2 = open(filename2, 'r')
#-------------------------------------------------------------------
newfile1 = open("new_two_wheelers.txt", "w+")
lines1 = list(open(filename1, 'r'))
for i in range(0, len(lines1)):
    new_list1 = lines1[i].replace('Do not own any', '0')
    newfile1.write(new_list1)
#newfile1.close()
#-------------------------------------------------------------------
newfile1 = open("new_two_wheelers1.txt", "w+")
new_list1 = list(open("new_two_wheelers.txt", 'r'))
for i in range(0, len(new_list1)):
    new_list11 = new_list1[i].replace('+', '')
    newfile1.write(new_list11)
newfile1.close()
#-------------------------------------------------------------------
newfile2 = open("new_four_wheelers.txt", "w+")
lines2 = list(open(filename2, 'r'))
for i in range(0, len(lines2)):
    new_list2 = lines2[i].replace('Do not own any', '0')
    newfile2.write(new_list2)
#newfile2.close()
#-------------------------------------------------------------------
newfile2 = open("new_four_wheelers1.txt", "w+")
new_list2 = list(open("new_four_wheelers.txt", "r"))
for i in range(0, len(new_list2)):
    new_list21 = new_list2[i].replace('+', '')
    newfile2.write(new_list21)
newfile2.close()
