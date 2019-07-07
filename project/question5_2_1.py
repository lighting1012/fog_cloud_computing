# COMP9334 project (19-T1) -- University of New South Wales
# Fog/cloud Computing
# Written by Jiaquan Xu

import matplotlib.pyplot as plt
import random

# self-set parameters
seed = 0
timeend = 1000

# given parameters
mode = 'random'
arrival = [9.72]
service = [0.01,0.4,0.86]
network = [1.2,1.47]
# para = [fogtimelimit,0.6,timeend]
# We want to find the best fogtimelimit

x = []
y = []
i = 1
alpha_1,alpha_2,beita = service[0], service[1], service[2]
gamma = (1-beita)/(alpha_2**(1-beita)-alpha_1**(1-beita))
while i < 1000:
    service_time = (random.random() * (1 - beita) / gamma + alpha_1 ** (1 - beita)) ** (1 / (1 - beita))
    x.append(i)
    y.append(service_time)
    i += 1
plt.scatter(x,y,s=5,alpha=0.5)
plt.ylabel('Service time in fog time unit')
plt.title('Service time distribution')
plt.savefig('image_1.png')    # get image_1 service time distribution
# we found that service time < 0.4




