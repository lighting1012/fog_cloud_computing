# COMP9334 project (19-T1) -- University of New South Wales
# Fog/cloud Computing
# Written by Jiaquan Xu

import matplotlib.pyplot as plt
import proj

# self-set parameters
seedrange = 1000
timeend = 1000
M = 500

# given parameters
mode = 'random'
arrival = [9.72]
service = [0.01,0.4,0.86]
network = [1.2,1.47]
# By observing the image_5, when fogtimelimit = 0.08 and 0.09, its lower bound of confidence
# interval is greater than the upper bound of 0.11's. So we exclude these two answer.
# Now the question is to pick a best between [0.10,0.11,0.12]

x = [0.10,0.11]
y = []
for seed in range(seedrange):
    y_1 = []
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
        y_1.append(mrt)
    print('seed =',seed)
    y.append(y_1)

for i in range(len(y)):
    plt.scatter(x,y[i],marker='o',c='',edgecolors='b')
plt.xlabel('FogTimeLimit')
plt.ylabel('mrt')
plt.title('seed = 0,1,2,...,500')

# mark 95% confidence interval for sets of mrt results of each fogtimelimit value
# student_t is t(59,0.975)   look up in the Student T Distribution Table
confidence_interval = []
student_t = 1.960
T_list = []
for j in range(len(y[0])):
    T = 0
    for i in range(len(y)):
        T += y[i][j]
    T /= len(y)
    T_list.append(T)
for j in range(len(y[0])):
    SSD = 0
    for i in range(len(y)):
        SSD += (y[i][j] - T_list[j]) ** 2
    SSD = (SSD / (seedrange-1)) ** 0.5
    lower = T_list[j] - student_t * SSD / seedrange**0.5
    upper = T_list[j] + student_t * SSD / seedrange**0.5
    confidence_interval.append([lower,upper])
lower=[]
upper=[]
for i in range(len(x)):
    lower.append(confidence_interval[i][0])
    upper.append(confidence_interval[i][1])

for i in range(len(x)):
    print(x[i], '[', lower[i], upper[i], ']')

plt.scatter(x,lower,marker=1,s=100,c='r')
plt.scatter(x,upper,marker=1,s=100,c='r')
plt.savefig('image_6.png')
