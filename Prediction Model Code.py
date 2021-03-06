#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from playsound import playsound


# In[4]:


#%% LOAD DATA
# Read the data files.
ys = np.genfromtxt(fname='ys.csv', delimiter=',')
ts = np.genfromtxt(fname='ts.csv', delimiter=',')

#ts=[0]
#x=0
#for i in range(0,len(ys)+1):
    #x+=15
    #ts = np.append(ts,x)

# Convert numpy array to pandas DataFrame.
ys = pd.DataFrame(ys)
ts = pd.DataFrame(ts)


#%% MODEL FIT AND PREDICTION
# First order polynomial model.

# Parameters of the predictive model. ph is Prediction horizon, mu is Forgetting factor.
ph = 30  
mu = 0.9  
hypo = 70
hyper = 160
#hypo = float(input("Set your hypoglycemia threshold"))
#hyper = float(input("Set your hyperglycemia threshold"))
n_s = len(ys)

# Arrays that will contain predicted values.
tp_pred = np.zeros(n_s-1) 
yp_pred = np.zeros(n_s-1)

# Real time data acquisition is here simulated and a prediction of ph minutes forward is estimated.
# At every iteration of the for cycle a new sample from CGM is acquired.
for i in range(2, (n_s+1)):
    ts_tmp = ts[0:i]
    ys_tmp = ys[0:i]
    ns = len(ys_tmp)
    
    # The mu**k coefficient represents the weight of the blood glucose sample 
    # at k instants before the current sampling time. Last acquired sample's 
    # weight is mu**k where k == 0, it has the greatetes weight.
    weights = np.ones(ns)*mu
    for k in range(ns):
        weights[k] = weights[k]**k
    weights = np.flip(weights, 0)
        

    # MODEL
    # Perform an Ordinary least squares Linear Regression.
    lm_tmp = linear_model.LinearRegression()    
    model_tmp = lm_tmp.fit(ts_tmp, ys_tmp, weights)
    # Coefficients of the linear model, y = mx + q 
    m_tmp = model_tmp.coef_
    q_tmp = model_tmp.intercept_

    # PREDICTION
    tp = ts.iloc[ns-1,0] + ph
    yp = m_tmp*tp + q_tmp
      
    tp_pred[i-2] = tp    
    yp_pred[i-2] = yp

    # Condition to make alarm
    if hyper > yp and yp > hypo:
        counter = 0
    
    if yp <= hypo:
        counter += 1
        if counter == 10:
            print("Watch out you could have hypoglicemic episode")
            playsound('alarm2.mp3')
        elif counter == 15:
            print("Watch out! We have predicted " + str(counter)  + " values in a row below the established threshold")
            #playsound('alarm2.mp3')
        elif counter == 30:
           print("Watch out! We have predicted " + str(counter) + " values in a row below the established threshold")
           #playsound('alarm2.mp3')
        elif counter == 45:
            print("Watch out! We have predicted " + str(counter) + " values in a row below the established threshold")
            #playsound('alarm2.mp3')
        elif counter == 60:
            print("Watch out! We have predicted " + str(counter) + " values in a row below the established threshold")
            #playsound('alarm2.mp3')

    if yp >= hyper:
        print("Watch out at you could have hyperglicemic")


#%% THRESHOLD
# Hypoglycemia threshold vector.    
t_tot = [l for l in range(int(ts.min()), int(tp_pred.max())+1)]
hypoline = hypo*np.ones(len(t_tot)) 
hyperline = hyper*np.ones(len(t_tot)) 
    
#PLOTING
fig, ax = plt.subplots()
fig.suptitle('Glucose prediction', fontsize=14, fontweight='bold')
ax.set_title('mu = %g, ph=%g ' %(mu, ph))
ax.plot(tp_pred, yp_pred, '--', label='Prediction') 
ax.plot(ts.iloc[:,0], ys.iloc[:,0], label='CGM data') 
ax.plot(t_tot, hypoline, label='Hypoglycemia threshold')
ax.plot(t_tot, hyperline, label='Hyperglycemia threshold')
ax.set_xlabel('time (min)')
ax.set_ylabel('glucose (mg/dl)')
ax.legend()
      

# %%
