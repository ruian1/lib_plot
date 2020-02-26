import numpy as np
import matplotlib.pyplot as plt
cls=['#2b8cbe','#31a354','#e34a33','#fed976','#756bb1']#,'cyan','black']

def make_energy_dist(df_input):
    fig,(ax0,ax1,ax2,ax3,ax4)=plt.subplots(1,5,figsize=(20,6))
    ax0.hist(df_input[df_input.eng_ini0>0].eng_ini0*1000, bins=np.arange(0, 1100, 10), color=cls[0])
    ax1.hist(df_input[df_input.eng_ini1>0].eng_ini1*1000, bins=np.arange(0, 1100, 10), color=cls[1])
    ax2.hist(df_input[df_input.eng_ini2>0].eng_ini2*1000, bins=np.arange(0, 1100, 10), color=cls[2])
    ax3.hist(df_input[df_input.eng_ini3>0].eng_ini3*1000, bins=np.arange(0, 1100, 10), color=cls[3])
    ax4.hist(df_input[df_input.eng_ini4>0].eng_ini4*1000 - 938, bins=np.arange(0, 1100, 10), color=cls[4])
    ax0.set_xlabel("DepE_electron")
    ax1.set_xlabel("DepE_gamma")
    ax2.set_xlabel("DepE_mu")
    ax3.set_xlabel("DepE_pi")
    ax4.set_xlabel("DepE_proton")
    plt.show()

def make_stack_plot(df_all, title):
    
    bin_space=0.02
    if (title==r'1 Proton 1 $\mu^-$ 1 $\gamma$'):
        df_all=df_all[df_all.label0>=0]
        df_all=df_all[df_all.label1>=0]
        df_all=df_all[df_all.label2>=0]
        df_all=df_all[df_all.label3>=0]
        df_all=df_all[df_all.label4>=0]
    if (title==r'1 Proton 1 $\gamma$'):
        df_all=df_all[df_all.label0==0]
        df_all=df_all[df_all.label1==1]
        df_all=df_all[df_all.label2==0]
        df_all=df_all[df_all.label3==0]
        df_all=df_all[df_all.label4==1]
    if (title==r'1 Proton 1 $e^-$'):
        print title
        df_all=df_all[df_all.label0==1]
        df_all=df_all[df_all.label1==0]
        df_all=df_all[df_all.label2==0]
        df_all=df_all[df_all.label3==0]
        df_all=df_all[df_all.label4==1]
    if (title==r'1 Proton 1 $\mu^-$'):
        df_all=df_all[df_all.label0==0]
        df_all=df_all[df_all.label1==0]
        df_all=df_all[df_all.label2==1]
        df_all=df_all[df_all.label3==0]
        df_all=df_all[df_all.label4==1]
    print "there are %i entries. "%df_all.index.size

    ###################
    ### Overlap Plot###
    ###################
    bins=np.arange(0,1+bin_space,bin_space)
    fig, ax = plt.subplots(1,1,figsize=(8,6))
    alpha=0.8
    n_pion,b,p=ax.hist(df_all.score03.values, bins=bins, alpha=alpha,label = r'$\pi^\pm$',color = cls[3], edgecolor= 'black')
    n_muon,b,p=ax.hist(df_all.score02.values, bins=bins, alpha=alpha,label = r'$\mu$',color = cls[1], edgecolor= 'black')
    n_electron,b,p=ax.hist(df_all.score00.values, bins=bins, alpha=alpha,label = r'$e^-$',color = cls[0], edgecolor= 'black')
    n_gamma,b,p=ax.hist(df_all.score01.values, bins=bins, alpha=alpha,label = r'$\gamma$', color=cls[4],edgecolor='black')
    n_proton,b,p=ax.hist(df_all.score04.values, bins=bins, alpha=alpha,label = 'Proton',color = cls[2], edgecolor= 'black')
        
    ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, mode="expand", borderaxespad=0.)
    ax.grid()
    ax.set_xlabel('MPID Score')

    ##################
    ### Stack Plot ###
    ##################
    fig,ax1=plt.subplots(1,1,figsize=(8,6))
    bins=np.linspace(0,1,1/bin_space)
    
    ax1.hist([bins, bins, bins, bins, bins],\
             len(bins),
            weights = [ n_pion/np.sum(n_pion), n_muon/np.sum(n_muon), n_gamma/np.sum(n_gamma), n_electron/np.sum(n_electron), n_proton/np.sum(n_proton)], \
            edgecolor='black', \
            linewidth = 0.2, \
            label =   [r'$\pi^\pm$', r'$\mu^-$', r'$\gamma$', r'$e^-$'  , r'$p^+$' ],\
            color =   [cls[3]   , cls[1]   , cls[4]     , cls[0]      , cls[2]],\
            stacked=True)
    
    handles,labels = ax.get_legend_handles_labels()

    print labels
    
    handles = [handles[2], handles[3], handles[1], handles[0], handles[4]]
    labels  = [labels[2] , labels[3] , labels[1] ,  labels[0],  labels[4]]

#     if (title==r'1 Proton 1 $e^-$'):
#         ax.legend(handles,labels,loc=1, fontsize=15, ncol=5, bbox_to_anchor=(0.5, 0., 0.5, 1.15))
#     else:
#     ax.legend(handles,labels, fontsize=12)
        
    ax1.legend(handles,labels,loc=3, fontsize=12, ncol=5, bbox_to_anchor=(0., 1.01, 1., .101), mode="expand")
#     ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, mode="expand", borderaxespad=0., fontsize=14)

    ax1.grid(linestyle="--")
    ax1.set_xlabel("MPID Scores", fontsize=15)
    ax1.set_ylabel("Arbitrary Unit", fontsize=15)
    max_bin= ax1.get_ylim()[1]
#     ax1.text(0.01, max_bin*0.87,"MicroBooNE Simulation Preliminary", fontsize=15,fontweight='bold')
#     ax.set_title(title, fontsize=14)
#     ax.set_ylim(0,3500)
#     plt.legend()
#     plt.savefig("/Users/dayajun/Desktop/stacked_%s.png"%title)

    fig, ax2= plt.subplots(1,1,figsize=(8,6))
    ax2.hist([bins], len(bins), weights = [n_electron/np.sum(n_electron)], edgecolor='black', \
            linewidth = 0.2, label = [r'$e^-$'], color =   [cls[0]], stacked=False, alpha=0.8)
    ax2.hist([bins], len(bins)-1, weights = [n_gamma/np.sum(n_gamma)], edgecolor='black', linewidth = 0.2, \
            label =   [r'$\gamma$'], color = [cls[4]], stacked=False, alpha=0.8)
    ax2.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=5, borderaxespad=0.)
    ax2.grid()
    ax2.set_xlabel('MPID Score')

    ymax = ax1.get_ylim()[1]
    ax1.text(0.55, 0.9 * ymax,"MicroBooNE Simulation", fontsize=15)
#   plt.savefig("/Users/dayajun/Desktop/e_gamma_%s.png"%title)
