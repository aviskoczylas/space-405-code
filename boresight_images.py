import numpy as np, h5py, matplotlib.pyplot as plt, matplotlib.image as mpimg

filepath='C:/Users/abrah/OneDrive/Desktop/space 405 project/Juno_MWR_TA_Footprint_ch06_pj19.h5'
f = h5py.File(filepath, 'r')

#creates 3 lists containing the members of each group
list_s1=[]
list_s2=[]
group_list=[list_s1, list_s2]
for group_name in f:
    group = f[group_name]
    #print("Group:", group_name)
    for member_name in group:
        member = group[member_name]
        #print("Member:", member_name)
        if(group_name=='s1'):
            list_s1.append(member)
        elif(group_name=='s2'):
            list_s2.append(member)
        else:
            continue

list_s1 = [np.array(member) for member in list_s1]
list_s2 = [np.array(member) for member in list_s2]

# Define boundary latitudes and longitudes
boundary_latitudes =  list_s1[0] # boundary latitudes  294 x 254 x 360
boundary_longitudes =  list_s1[1]# boundary longitudes 294 x 254 x 360
num_boundary_points = list_s1[2];  # footprint boundary points 294 x 254
# make a masked array for junk values
mask = boundary_latitudes == -999.9
boundary_latitudes_clean = np.ma.masked_array(boundary_latitudes, mask)
boundary_longitudes_clean = np.ma.masked_array(boundary_longitudes, mask)

# Load and plot image of jupiter
impath='C:/Users/abrah/OneDrive/Desktop/space 405 project/jup_flipped.png'
img = mpimg.imread(impath, 'r')
plt.imshow(img, extent=[0, 360, -90, 90])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Boresights plotted on Jupiter\'s surface')

#plots slices of data at chosen intervals, adjust sampling_rate to change how much data you see
sampling_rate=14
selected_longs = boundary_longitudes[::sampling_rate, ::sampling_rate,:]
selected_lats = boundary_latitudes[::sampling_rate, ::sampling_rate,:]
selected_num= num_boundary_points[::sampling_rate, ::sampling_rate]
for row in range(selected_longs.shape[0]):
    for col in range(selected_longs.shape[1]):
        if(selected_num[row,col]==360):
            plt.plot(selected_longs[row,col,:], selected_lats[row,col,:], color='black', linewidth=2)
            bore_site_latitude = np.sum(selected_lats[row,col,:])/selected_num[row,col]
            bore_site_longitude = np.sum(selected_longs[row,col,:])/selected_num[row,col]
            plt.plot(bore_site_longitude, bore_site_latitude, 'yo', markersize=3)
plt.show()
