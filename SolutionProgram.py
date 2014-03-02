#!/usr/bin/env python

#Copyright (c) Payton Ide 2014
#View LICENSE.txt for copyright information
"""
Calculates Probability of winning a game of badminton based on the probability of winning a point
Author: Payton Ide
See README.txt for information regarding scipy stats, the binomial module, and the uses thereof in this program
"""

from scipy.stats import binom

#assign values as descriped in the explanation and solution file
p = input("Enter probablility: ")
e = binom.sf(20, 40, p, loc=0)
i = binom.pmf(20, 40, p, loc=0)
t = 2*p*(1-p)
d = p**2

#calculate game win probabilty using the derived formula
W = e + i*d + i*t*d + i*(t**2)*d + i*(t**3)*d + i*(t**4)*d + i*(t**5)*d + i*(t**6)*d + i*(t**7)*d + i*(t**8)*d + i*(t**9)*p

#calculate match win probabiltiy based on game win probability
V = W**2 + 2*(W**2)*(1-W)

#print user-inputted point win probability, followed by calculated game and match win probabilities
print "Probablity of winning a single point: ", p
print "Probablity of winning a game: ", W
print "Probability of winning a match: ", V

