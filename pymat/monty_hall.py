import matplotlib.pyplot as plt
import numpy as np

# [0,1,2] # 0 = closed goat, 1 = closed car, 2 = opened goat


#doors = [0] * n #n = number of doors
# N-1
# N(N-p-1)


N = int(input("how many doors?"))
p = int(input("how many doors should Monty open?"))

prob = 100*(N-1)/(N*(N-p-1))
print(prob)

dat = [0]*p
xax = list(range(1,p+1))

dat = np.asarray(dat,dtype=np.float32)
xax = np.asarray(xax)

for i in range(1, p+1):
    dat[i-1] = (N-1)/(N*(N-i-1))
    #print(i ,"\t", dat[i-1], "\n")

#print (dat, "\n")
#print (xax)

#print (dat, "\n")
#print (xax)

plt.plot(xax, dat, "ro", lw=2.0)
plt.axis([0,p+100, 0, np.amax(dat)+1])
#plt.yscale('log')
plt.ylabel('Probability')
plt.xlabel('Number of doors opened')
plt.title('Monty hall win probability for N doors')
plt.show()
