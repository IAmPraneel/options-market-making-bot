import numpy as np
from scipy.stats import norm

def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

def delta(S, K, T, r, sigma, option_type='call'):
    if option_type == 'call':
        return norm.cdf(d1(S, K, T, r, sigma))
    else:
        return norm.cdf(d1(S, K, T, r, sigma)) - 1

def gamma(S, K, T, r, sigma):
    d1_val = d1(S, K, T, r, sigma)
    return norm.pdf(d1_val) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    d1_val = d1(S, K, T, r, sigma)
    return S * norm.pdf(d1_val) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type='call'):
    d1_val, d2_val = d1(S, K, T, r, sigma), d2(S, K, T, r, sigma)
    first_term = -(S * norm.pdf(d1_val) * sigma) / (2 * np.sqrt(T))
    if option_type == 'call':
        second_term = -r * K * np.exp(-r * T) * norm.cdf(d2_val)
    else:
        second_term = r * K * np.exp(-r * T) * norm.cdf(-d2_val)
    return first_term + second_term

def rho(S, K, T, r, sigma, option_type='call'):
    d2_val = d2(S, K, T, r, sigma)
    if option_type == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(d2_val)
    else:
        return -K * T * np.exp(-r * T) * norm.cdf(-d2_val)
