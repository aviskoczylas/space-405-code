import numpy as np, h5py, matplotlib.pyplot as plt
filepath='C:/Users/abrah/Downloads/Juno_MWR-Antenna_Temperatures-Swath-Perijove_19.h5'
f = h5py.File(filepath, 'r')

#creates 3 lists containing the members of each group
list_s0=[]
list_s1=[]
list_s2=[]
for group_name in f:
    group = f[group_name]
    print("Group:", group_name)

    for member_name in group:
        member = group[member_name]
        print("Member:", member_name)
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

time_axis = np.arange(0, len(list_s0[0]))

#plot latitude vs time
plt.plot(time_axis, list_s0[0])
plt.xlabel('Time')
plt.ylabel('Latitude')
plt.title('Latitude of Spacecraft Over Time')
plt.show()

#plot longitude vs time
plt.plot(time_axis, list_s0[1])
plt.xlabel('Time')
plt.ylabel('Longitude')
plt.title('Longitude of Spacecraft Over Time')
plt.show()

#plot parametric curve, or latitude + longitude vs time
plt.plot(list_s0[0], list_s0[1])
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.title('Path of Spacecraft Over Time')

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

#plot local zenith angle vs location
plt.pcolor(list_s1[0])
plt.xlabel('X axis (unknown units atm)')
plt.ylabel('Y axis (unknown units atm)')
plt.title('Local Zenith Angle')
plt.show()

#plot temperature vs location
plt.pcolor(list_s1[1])
plt.xlabel('X axis (unknown units atm)')
plt.ylabel('Y axis (unknown units atm)')
plt.title('Channel 1 Temperature')
plt.show()
