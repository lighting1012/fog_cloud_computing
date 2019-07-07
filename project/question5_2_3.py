# COMP9334 project (19-T1) -- University of New South Wales
# Fog/cloud Computing
# Written by Jiaquan Xu

import matplotlib.pyplot as plt
import proj

# self-set parameters
seed = 0
timeend = 1000
M = 500

# given parameters
mode = 'random'
arrival = [9.72]
service = [0.01,0.4,0.86]
network = [1.2,1.47]

# We can find that after fogtimelimit > 0.2, the mrt increases rapidly.
# So I decide to plot one more time, mrt over fogtimelimit in interval (0,0.2)

x = []
y = []
fogtimelimit = 0
while fogtimelimit < 0.2:
    fogtimelimit += 0.01
    x.append(fogtimelimit)
for fogtimelimit in x:
    para = [fogtimelimit, 0.6, timeend]
    arrival_1, service_1, network_1 = proj.random_solve(arrival, para, service, network, seed)
    fog, net, cloud = proj.trace(arrival_1, para, service_1, network_1)
    mrt = 0

    # Transient removal: remove first M job's response time.
    for i in range(M, len(arrival_1)):
        if arrival_1[i] in net.keys():
            if cloud[arrival_1[i]] < para[2]:
                mrt += (cloud[arrival_1[i]] - arrival_1[i])
        else:
            if fog[arrival_1[i]] < para[2]:
                mrt += (fog[arrival_1[i]] - arrival_1[i])
    mrt /= (len(arrival_1) - M)
    print(fogtimelimit,mrt)
    y.append(mrt)
plt.cla()
plt.plot(x,y)
plt.xlabel('FogTimeLimit')
plt.ylabel('mrt')
plt.title('seed = 0')
plt.savefig('image_3.png')
# By observing the image_3, we conclude that mrt can take the minimum
# when fogtimelimit is between 0.08 and 0.12.
# So next step is compare fogtimelimit = 0.08,0.09,0.10,0.11,0.12