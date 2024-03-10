Python code written for the Space 405 project: Microwave Mapping of Jupiter’s Vortices

By Avi Skoczylas and Maddy Deming

Completed with help from Cheng Li and Jiheng Hu


Project description:
Jupiter is widely known for its global widespread storms, vortices, and convective clouds that dominate its upper atmosphere. 
These phenomena are closely linked to atmospheric dynamics and weather phenomenon. 
The Juno spacecraft is equipped with a microwave radiometer (MWR) capable of mapping Jupiter’s atmosphere using six centimeter-wave channels,
with frequencies ranging from 0.6 GHz (50 cm, channel 1) to 21.9 GHz (1.37 cm, channel 6) 1. These channels are designed to detect the dynamic 
characteristics of Jupiter’s sub-cloud atmosphere and the presently unknown variations in the abundances of ammonia and water deep within these 
cloud decks. During the 19-th flyby, the MWR observed several Jovian vortices in the mid-latitudes 2. Recent flybys have revealed features of the polar vortices.

Basic Goal

Make plots of the multiband microwave brightness temperature signals observed by Juno/MWR
Map and identify individual Jovian vortices.

Advanced Goal

Read the numerical simulation results of Jovian vortices.
Simulate the synthetic MWR antenna temperatures of the Jovian vortices.
A synthetic MWR antenna temperature is obtained by the integration of point-wise emission model with the MWR’s measurement response function (MRF). 
To perform the integration, we need to know the antenna pattern function, the spacecraft’s altitude, and the antenna beamwidth.

