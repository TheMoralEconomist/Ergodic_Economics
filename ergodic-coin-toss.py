import numpy as np
import matplotlib.pyplot as plt

#Source
#https://ergodicityeconomics.files.wordpress.com/2018/06/ergodicity_economics.pdf

#Coin Toss Outcomes
rOfT = [.6, 1.5]

#if 0 multiply wealth by .6, if 1 multiply wealth by 1.5
def coinTossFunction(wealth):
    coinToss = np.random.random_integers(0,1)
    if (coinToss == 0):
        wealth = rOfT[0]*wealth
    else:
        wealth = rOfT[1]*wealth
    return wealth

#number of coin tosses- change to 1000 to see long term average
numCoinToss = 52
#number of parallel iterations, simple case is 1
numParallelGames = 1000
#keep track of each parallel game
wealthEnsemble = []
for y in range(numParallelGames):    
    #Keep track of time and wealth to plot
    time = []
    wealth = []
    #Fix initial wealth to one
    initialWealth = 1
    #for 52 iterations calculate wealth according to above function
    for x in range(numCoinToss):
        time.append(x)
        if x==0:
            wealth.append(coinTossFunction(initialWealth))
        else: 
            wealth.append(coinTossFunction(wealth[x-1]))
    
    wealthEnsemble.append(wealth)
#funtion computers the finite ensemble average
averageWealth = []
for x in range(numCoinToss):
    sum = 0
    for int, value in enumerate(wealthEnsemble):
        sum = sum + wealthEnsemble[int][x]
    average = sum/numParallelGames
    averageWealth.append(average)
    print(int, value)

#print(averageWealth)
fig, ax = plt.subplots()
plt.xlabel("Number of Tosses")
plt.ylabel("Wealth Multiple")
ax.plot(time, averageWealth, label="Coin Toss")
plt.show()
