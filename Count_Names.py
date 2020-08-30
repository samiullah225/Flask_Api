elist=["Yonus Khan","Babar siddique","Umer siddique","Jhanzaib Alam","Rizwan siddique","Tahir Sheikh"]
count=0
for e in elist:
    e=e.split(' ')[-1]
    if(e=="siddique"):
        count=count+1
print(elist," Contains ",count," number of siddique last names")