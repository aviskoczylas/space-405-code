import numpy as np, h5py, matplotlib.pyplot as plt
filepath='C:/Users/abrah/OneDrive/Desktop/space 405 project/Juno_MWR-Antenna_Temperatures-Swath-Perijove_19.h5'
f = h5py.File(filepath, 'r')

#creates 3 lists containing the members of each group
list_s0=[]
list_s1=[]
list_s2=[]
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

time_axis = np.arange(0, len(list_s0[0]))

#uncomment any specific plot you want to see!

'''
#plot latitude vs time
plt.plot(time_axis, list_s0[0])
plt.xlabel('Time')
plt.ylabel('Latitude')
plt.title('Latitude of Spacecraft Over Time')
plt.show()
'''

'''
#plot longitude vs time
plt.plot(time_axis, list_s0[1])
plt.xlabel('Time')
plt.ylabel('Longitude')
plt.title('Longitude of Spacecraft Over Time')
plt.show()
'''

'''
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
'''

x1=[]
y1=[]
angle1=[]
tempch6=[]
for row_index, row in enumerate(list_s2[0]):
    for col_index, element in enumerate(row):
        angle1.append(element)
        x1.append(list_s2[7][row_index, col_index])
        y1.append(list_s2[6][row_index, col_index])
        tempch6.append(list_s2[5][row_index, col_index])

'''
#plot local zenith angle vs location
plt.scatter(x1,y1,c=angle1, cmap='viridis') 
plt.colorbar() 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Local Zenith Angle')
plt.show()
'''

'''
#plot channel 6 temperature vs location
plt.scatter(x1,y1,c=tempch6, cmap='viridis') 
plt.colorbar() 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Temperature in channel 6')
plt.show()
'''
