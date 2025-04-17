import os

os.chdir("./wing_list/airfoiltools.com/airfoil/")

dirs = os.listdir()
dats = []
for i in dirs:
    if "dat" in i:
        dats += [i]
        # print(i)
# print(dats)

dats_w_points = []
for i in dats:
    arr_add = []

    with open(i,"r") as file:
        contends = file.readlines()
    
    clean_contence = []
        
    for j in contends[1:]:
        j = j.strip().split('\n')
        print(j)
        try:
            clean_contence[0] = j[1]
        except:
            pass
            clean_contence += j
        print(clean_contence)


