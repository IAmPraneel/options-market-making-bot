# Implementing Black-Scholes model in python

import numpy as np
from scipy.stats import norm

# define variables

r = 0.01 # interest rate
S = 30 # underlying price
K = 40 # strike price
T = 240/365 # time out of 365 days
sigma= 0.30 # variance

# call or put is the type of action
def blackScholes(r,S,K,T,sigma,type="C"):
    '''calculate black scholes option price for a call or put '''
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/(sigma*(T**0.5))
    d2 = (np.log(S/K) + (r - sigma**2/2)*T)/(sigma*(T**0.5))
    # d2 can also be defined as d1- sigma*np.sqrt(T)

    try:
        if type=="C": # call
            price=S*norm.cdf(d1,0,1) - K*np.exp(-r*T)*norm.cdf(d2,0,1)# cdf here is cumulative distribution function of normal distribution
        elif type=="P": # put
            price= K*np.exp(-r*T)*norm.cdf(-d2,0,1) - S*norm.cdf(-d1,0,1)
        return(price)
    except:
        print("Please confirm all option parameters above !!!")

print("Option price is : ",round(blackScholes(r,S,K,T,sigma,type="C"),2))


