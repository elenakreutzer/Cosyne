# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:25:04 2018

@author: Elena
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.ticker as ticker
import core
from mpl_toolkits.axes_grid1 import make_axes_locatable



#plot example traces for different phases
def trace_plot(ax,weighttraces,time_params,perc=True,**kwargs):  
    total_time=(time_params["pre_learning_time"]+time_params["learning_time"])
    step=time_params["interval_length"]
    time=np.arange(0.,total_time,step)-time_params["pre_learning_time"]

    for i,trace in enumerate(weighttraces):
             if perc==True:
                 #transform to percentage weight change
                 weighttraces[i]=weighttraces[i]/weighttraces[i][0] *100.
             ax.plot(time, weighttraces[i,:],**kwargs)
    if perc==True:
        ax.axhline(y=100,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")    



#normalize diverging heatplot colorbar such that lightest color is at zero


class MidpointNormalize(Normalize):
	def __init__(self,vmin=None,vmax=None,midpoint=None,clip=True):
		self.midpoint=midpoint
		Normalize.__init__(self,vmin,vmax,clip)
	def __call__(self,value,clip=True):
		x,y=[self.vmin,self.midpoint,self.vmax],[0.,0.5,1.]
		return(np.ma.masked_array(np.interp(value,x,y)))

#adjust colormap
cmap = mpl.cm.RdBu(np.linspace(0,1,100))
cmap = mpl.colors.ListedColormap(cmap[np.concatenate((np.arange(0,30,1),np.arange(70,100,1)))])




#heatplot of 3 dimensional data
def hplot(ax,data,vmin,vmax,extent,label,labelpad):
    norm=MidpointNormalize(vmin=vmin,vmax=vmax,midpoint=0)
    zeros=np.absolute(data)<10**(-2)
    data[zeros]=0

    
    img=ax.imshow(data,norm=norm,cmap=cmap,origin="lower",interpolation="none",extent=extent.tolist())
    
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)


    cb= plt.colorbar(img, cax=cax)
    cb.set_clim(vmin,vmax)
    cbar_ticks = np.array((int(vmin),0,int(vmax)))
    cb.set_ticks(cbar_ticks) 
    cb.ax.tick_params(labelsize=core.linewidth["cb"])
    cb.draw_all() 
    cb.set_label(label,labelpad=labelpad,fontsize=core.linewidth["cb"])
    cb.update_ticks()


def wpathplot(ax,vectorfield,weightpath,**para):
    
    target=para.get("target")
    color=para.get("color")
    wmin=para.get("wmin")
    wmax=para.get("wmax")
    precision=para.get("precision")
    W1,W2=np.meshgrid(np.arange(wmin,wmax,precision),np.arange(wmin,wmax,precision))
    #vectorfield=np.ones((10,10,2))
    ax.scatter(target[0],target[1],color=color)
    #ax.set_aspect("equal")
    ax.quiver(W2,W1,vectorfield[:,:,0],vectorfield[:,:,1],angles="xy",color=color) 
    ax.plot(weightpath[0,:],weightpath[1,:],color=color, linewidth=core.linewidth["aux_lines"],ls="dashed")

def contourplot(ax,cost,levels,**para):
    
    color=para.get("color")
    wmin=para.get("wmin")
    wmax=para.get("wmax")
    precisioncost=para.get("precisioncost")
    W1,W2=np.meshgrid(np.arange(wmin,wmax,precisioncost),np.arange(wmin,wmax,precisioncost))

    img=ax.contour(W2,W1,cost,levels=levels,marker='s',alpha=0.9,linewidths=core.linewidth["contour"],colors=color,angles="xy")
   # divider = make_axes_locatable(ax)
    #cax = divider.append_axes("right", size="5%", pad=0.05)

    #cb= plt.colorbar(img, cax=cax)
    
    #tick_locator = ticker.MaxNLocator(nbins=2)
    #cb.locator = tick_locator
    #cb.update_ticks()
    
def vecplot(ax,vectorfield,**para):
    
    target=para.get("target")
    color=para.get("color")
    wmin=para.get("wmin")
    wmax=para.get("wmax")
    precision=para.get("precision")
    W1,W2=np.meshgrid(np.arange(wmin,wmax,precision),np.arange(wmin,wmax,precision))
    #vectorfield=np.ones((10,10,2))
    ax.scatter(target[0],target[1],color=color)
    #ax.set_aspect("equal")
    ax.quiver(W2,W1,vectorfield[:,:,0],vectorfield[:,:,1],angles="xy",color=color) 
    