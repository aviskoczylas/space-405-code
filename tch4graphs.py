import numpy as np, h5py, matplotlib.pyplot as plt, matplotlib.image as mpimg

filepath1='C:/Users/abrah/OneDrive/Desktop/space 405 project/Juno_MWR_TA_Footprint_ch06_pj19.h5'
filepath2='C:/Users/abrah/OneDrive/Desktop/space 405 project/Juno_MWR-Antenna_Temperatures-Swath-Perijove_19.h5'
f = h5py.File(filepath1, 'r')
g = h5py.File(filepath2, 'r')

list_s0_1=[]
list_s1_1=[]
list_s2_1=[]
for group_name in g:
    group = g[group_name]
    #print("Group:", group_name)

    for member_name in group:
        member = group[member_name]
        #print("Member:", member_name)
        if(group_name=='s0'):
            list_s0_1.append(member)
        elif(group_name=='s1'):
            list_s1_1.append(member)
        elif(group_name=='s2'):
            list_s2_1.append(member)
        else:
            print("ERROR, there should only be 3 groups!")
list_s0_1 = [np.array(member) for member in list_s0_1]
list_s1_1 = [np.array(member) for member in list_s1_1]
list_s2_1 = [np.array(member) for member in list_s2_1]

list_s1_2=[]
list_s2_2=[]
for group_name in f:
    group = f[group_name]
    #print("Group:", group_name)
    for member_name in group:
        member = group[member_name]
        #print("Member:", member_name)
        if(group_name=='s1'):
            list_s1_2.append(member)
        elif(group_name=='s2'):
            list_s2_2.append(member)
list_s1_2 = [np.array(member) for member in list_s1_2]
list_s2_2 = [np.array(member) for member in list_s2_2]

#we're only looking at certain longitudes, so we define them here.
longmin=200
longmax=320

boundary_latitudes =  list_s1_2[0] 
boundary_longitudes =  list_s1_2[1]
num_boundary_points = list_s1_2[2];  

mask = boundary_latitudes == -999.9
boundary_latitudes = np.ma.masked_array(boundary_latitudes, mask)
boundary_longitudes = np.ma.masked_array(boundary_longitudes, mask)

bs_lats=[]
bs_longs=[]
for row in range(boundary_longitudes.shape[0]):
    for col in range(boundary_longitudes.shape[1]):
        if(all(boundary_longitudes[row,col,:]>longmin) and all(boundary_longitudes[row,col,:]<longmax)):
            if(num_boundary_points[row,col]==360):
                bs_lats.append(np.sum(boundary_latitudes[row,col,:])/num_boundary_points[row,col])
                bs_longs.append(np.sum(boundary_longitudes[row,col,:])/num_boundary_points[row,col])
bs_lats=np.array(bs_lats)
bs_longs=np.array(bs_longs)
plt.scatter(bs_longs, bs_lats,c='y', marker='o', s=0.5)
plt.show()

longs=[]
lats=[]
tempch4=[]
angles=[]
for row_index, row in enumerate(list_s2_1[0]):
    for col_index, col in enumerate(row):
        if(list_s2_1[7][row_index, col_index]>(longmin-360) and list_s2_1[7][row_index, col_index]<(longmax-360)):
            longs.append(list_s2_1[7][row_index, col_index]+360)
            lats.append(list_s2_1[6][row_index, col_index])
            tempch4.append(list_s2_1[3][row_index, col_index])
            angles.append(col)
longs=np.array(longs)
lats=np.array(lats)

points1 = np.column_stack((lats, longs))
points2 = np.column_stack((bs_lats, bs_longs))

shared_indexes = []
distance_threshold = 1

for index, point1 in enumerate(points1):
    for point2 in points2:
        lat_diff = point1[0] - point2[0]
        long_diff = point1[1] - point2[1]
        dist = np.sqrt(lat_diff**2 + long_diff**2)
        if dist < distance_threshold:
            shared_indexes.append(index)

shared_indexes = np.array(shared_indexes)
tempch4 = np.array(tempch4)[shared_indexes]
angles = np.array(angles)[shared_indexes]
lats = lats[shared_indexes]
longs = longs[shared_indexes]

trutharr=(tempch4>180)&(angles<60)
lats = lats[trutharr]
longs = longs[trutharr]
tempch4=tempch4[trutharr]

#plot channel 6 temperature vs location
plt.scatter(longs,lats,c=tempch4, cmap='viridis') 
plt.colorbar() 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Temperature in channel 4')
plt.show()
