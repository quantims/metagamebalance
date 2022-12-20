import numpy as np
from scipy.optimize import linprog


#The script expects a payoff matrix, so your matrix should have positive values for winning matchups and negative values for losing matchups
#For instance, if a row character has a 45% chance of winning a matchup, the matrix value for that matchup should be -.05, NOT .45
gamemat = np.loadtxt(r'C:\Users\timrs\ssb64mat.csv', delimiter=',') #Path to file of game matrix; change this & the path on line 69 for your own use

#Adjust these two values for your own needs
stdev = .1 #set standard deviation. This is how much the matchup matrix varies between players; bigger means the game differs more from player to player
nsims = 1000 #the number of simulations we'll make

sims = range(nsims)
dimension = range(len(gamemat))
#print(dimension)
ne_array = np.empty(shape =(nsims,len(gamemat)), dtype = 'float') #array of nash equilibria

#initialize two dimensional list to store results
usageresults = [ [0]*len(gamemat) for i in sims]

#Create matrix for averaging usage
usage = [[0.] * len(gamemat) for i in range(nsims)]

#The Nash Equilibrium solving script is adapter from: 
#https://github.com/sid230798/Game_Theory/blob/master/Problem3/analyse_equilibrium.py

## Calculate MSNE for Zero sum game
def msne(a) :

    ## One zero array for later (z, x)
    ess = np.ones(a.shape[0]+1)
    ess[0] = 0

    c = -1*(1-ess)  ##[-1, 0 ,0 ,0] -1 coeff for z and 0 for x (Max z == min(-z))
    A_ub = np.concatenate((np.ones((1, a.shape[1])), -1*a), axis=0).T
    B_ub = np.zeros(a.shape[1])
    A_eq = np.expand_dims(ess, axis=0)
    B_eq = np.ones(1)
    bounds = [(None, None)] + [(0,1)]*a.shape[0]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    p1_val, p1_distribution = result.x[0], result.x[1:]

    ## For 2nd player distribution
    ess = np.ones(a.shape[1]+1)
    ess[0] = 0
    c = (1-ess)
    A_ub = np.concatenate((-1*np.ones((a.shape[0], 1)), a), axis=1)
    B_ub = np.zeros(a.shape[0])
    A_eq = np.expand_dims(ess, axis=0)
    A_eq = np.concatenate((A_eq, 1-A_eq), axis=0)
    B_eq = np.array([1, p1_val]) ## Dual Principle w* = z*
    bounds = [(None, None)] + [(0,1)]*a.shape[1]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    p2_val, p2_distribution = result.x[0], result.x[1:]

    #Average MSNE for both players
    #convert tuples to arrays
    ##find tuple values & print them
    array1=np.asarray(p1_distribution)
    #print(array1[0])
    array2=np.asarray(p2_distribution)
    #print(array2)
    usage = .5*(array1+array2)
    #print(usage)
    for c in range(len(usage)):
        usageresults[n][c]=usage[c]
    
for n in sims:
    gamemat = np.loadtxt(r'C:\Users\timrs\ssb64mat.csv', delimiter=',') #resets gamemat. Not sure why, but this is necessary for correct results.
    gamematn = gamemat
    for i in dimension:
        for j in dimension:
            gamematn[i,j] = np.random.normal(gamemat[i,j],stdev)
    msne(gamematn)
    #print(gamematn)
#print(usageresults)
usagearray = np.array(usageresults)

avgusage = np.average(usagearray,axis=0)

print(avgusage) #Prints array showing average usage of each character/option
