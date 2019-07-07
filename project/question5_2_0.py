# COMP9334 project (19-T1) -- University of New South Wales
# Fog/cloud Computing
# Written by Jiaquan Xu

import matplotlib.pyplot as plt
import proj

# self-set parameters
seed = 0
timeend = 1000
fogtimelimit = 0.1

# given parameters
mode = 'random'
arrival = [9.72]
service = [0.01,0.4,0.86]
network = [1.2,1.47]

# By observing image_1, we found that service time < 0.4
# So the question is to find best fogtimelimit in interval (0,0.4)
# I set seed to be 0, compute the mrt over different fogtimelimit value.
x = []
y = []

para = [fogtimelimit, 0.6, timeend]
arrival_1, service_1, network_1 = proj.random_solve(arrival, para, service, network, seed)
fog, net, cloud = proj.trace(arrival_1, para, service_1, network_1)
sum_mrt = 0

# Transient removal: remove first M job's response time.
for i in range(len(arrival_1)):
    if arrival_1[i] in net.keys():
        if cloud[arrival_1[i]] < para[2]:
            sum_mrt += (cloud[arrival_1[i]] - arrival_1[i])
    else:
        if fog[arrival_1[i]] < para[2]:
            sum_mrt += (fog[arrival_1[i]] - arrival_1[i])
    mrt = sum_mrt/(i+1)
    print(i+1,mrt)
    x.append(i)
    y.append(mrt)
plt.cla()
plt.plot(x,y)
plt.xlabel('k')
plt.ylabel('mrt of first k jobs')
plt.title('seed = 0, fogtimelimit = 0.1')
plt.savefig('image_0.png')  # get image_2 mrt over fogtimelimit in (0,0.4)
# We can find that after fogtimelimit > 0.2, the mrt increases rapidly.