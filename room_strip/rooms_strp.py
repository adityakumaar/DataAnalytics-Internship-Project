filename = "rooms.txt"
f =  open(filename, 'r')
#------------------------------------------------
newfile = open("stripped_rooms.txt", "w+")
#------------------------------------------------
lines = list(open(filename, 'r'))
for i in range(1, len(lines)):
    #lines[i] = lines[i].astype(str)
    new_list = lines[i].replace('+', '')
    #lines[i] = lines[i].astype(int)
    newfile.write(new_list)
#------------------------------------------------
newfile.close()
