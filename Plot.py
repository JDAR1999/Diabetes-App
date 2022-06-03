import numpy as np
import matplotlib.pyplot as plt

#%% THRESHOLD
# Hypoglycemia threshold vector.  
# 
def Plot(ts,ys,tp_pred, yp_pred, hypo, hyper, mu, ph):  
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