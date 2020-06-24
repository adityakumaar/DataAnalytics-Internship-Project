import io
#-------------------------------------------------------------------
filename = "mixed_char_cities.txt"
f = io.open(filename, "r")
new_file = open("init_cap_cities.txt", "w+", encoding = "utf-8")
#-------------------------------------------------------------------
lines = list(open(filename, "r"))
#lines = [x.strip() for x in lines]
for i in range(0, len(lines)):
    new_list = lines[i].title()
    new_file.write(str(new_list))
#print(lines)
#new_list = [lines.upper() for i in lines]
new_file.close()
#-------------------------------------------------------------------






#ignore the commented part..... trash code
"""
f = open(filename, 'r')
lines = list(open(filename, 'r'))
lines = [x.strip() for x in lines]
new_file = open("Capitalnames.txt", "w+")
for i in lines:
    newfile.write(lines.upper())
"""
