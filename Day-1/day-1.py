# https://adventofcode.com/2022/day/1
# Problem statement: There is no way to identify who has the most calories, and there are too many elf's to find the answer manually. 
# goal: determine which elf has the most calories
# when someone is describing an problem, use that time to determine what the user's problem statement is. 

# step 1
# use spaces to separate everything into discrete chunks

# create an empty list, name it
elf_cal_list = []
temp = 0

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    if line != "\n":
        temp += int(line)
    else:
        elf_cal_list.append(temp)
        temp = 0

elf_cal_list.sort(reverse=True)

print(elf_cal_list[0])


#step 4
# select the one with the highest carried calories
# Using sudo code to outline the code is a huge help
