import numpy as np, h5py, matplotlib.pyplot as plt
filepath='C:/Users/abrah/Downloads/Juno_MWR-Antenna_Temperatures-Swath-Perijove_19.h5'
f = h5py.File(filepath, 'r')

#notes: for a file f, f.keys() gets you all keys in the file
#f[x] gets you the group corresponding to the group's name (in this case, 'x')
#for a group x, x[something] gets you the member corresponding to the member's name (in this case, 'something')

#creates 3 lists containing the members of each group
list_s0=[]
list_s1=[]
list_s2=[]
group_list=[list_s0, list_s1, list_s2]
for group_name in f:
    group = f[group_name]
    #print("Group:", group_name)

    for member_name in group:
        member = group[member_name]
        #print("Member:", member_name)
        if(group_name=='s0'):
            list_s0.append(member)
        elif(group_name=='s1'):
            list_s1.append(member)
        elif(group_name=='s2'):
            list_s2.append(member)
        else:
            print("ERROR, there should only be 3 groups!")
#print(list_s0)
#print(list_s1)
#print(list_s2)
list_s0 = [np.array(member) for member in list_s0]
list_s1 = [np.array(member) for member in list_s1]
list_s2 = [np.array(member) for member in list_s2]
#all members are now in lists as numpy arrays!
#now let's plot them!
time_axis = np.arange(0, len(list_s0[0]))

plt.show()
#plot latitude
plt.plot(time_axis, list_s0[0])
plt.xlabel('Time')
plt.ylabel('Latitude')
plt.show()

#plot longitude
plt.plot(time_axis, list_s0[1])
plt.xlabel('Time')
plt.ylabel('Longitude')
plt.show()

#plot parametric curve
plt.plot(list_s0[0], list_s0[1])
plt.xlabel('Latitude')
plt.ylabel('Longitude')

#add time points
x=[]
y=[]
t=[]
for a in range(9):
    x.append(list_s0[0][a*10000])
    y.append(list_s0[1][a*10000])
    t.append(a*100000)
plt.scatter(x, y)  
for i, (x_val,y_val,t_val) in enumerate(zip(x,y,t)):
    plt.text(x_val, y_val, t_val)
plt.show()