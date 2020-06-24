fname = "all_city_list.txt"
#----------------------------------------
lines = tuple(open(fname, 'r'))
lines = [x.strip() for x in lines]
#----------------------------------------
#print(lines)
print(len(lines))
#----------------------------------------
lines1 = list(dict.fromkeys(lines))
print(len(lines1))
new_file = open("all_city_list_new.txt", "w+")
new_file.write("all_cities = ")
new_file.write(str(lines1))
new_file.close()












#ignore the commented part.....trash code
'''
Use this code to see the number of lines in the file.
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print("Total number of lines is:", count)

f = open(fname, 'r')
file_contents = f.readlines()
file_contents = [x.strip() for x in file_contents]
print(file_contents)
f.close()
'''
