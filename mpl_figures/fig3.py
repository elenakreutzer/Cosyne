#!/usr/bin/env python2
# encoding: utf-8

import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib import gridspec as gs
from matplotlib import collections as coll
import pylab as p
import copy
import numpy as np
import plotfunctions as plotf
from cycler import cycler

import core
from core import log


def get_gridspec():
    """
        Return dict: plot -> gridspec
    """
    # TODO: Adjust positioning
    gs_main = gs.GridSpec(1, 1, hspace=0.65,
                          left=0.1, right=0.95, top=.9, bottom=0.1)
    gs_aux = gs.GridSpecFromSubplotSpec(2, 1, gs_main[0, 0], hspace=.4,
                                           height_ratios=[2.0, 1.0,])
    gs_aux1 = gs.GridSpecFromSubplotSpec(1, 4, gs_aux[0, 0], wspace=.7,
                                           width_ratios=[0.15,1., 1.0, 1.0,])
    gs_aux2 = gs.GridSpecFromSubplotSpec(4, 1, gs_aux1[0, 2], hspace=1.5,
                                           height_ratios=[1.,1.,1.,1.])
    gs_aux3 = gs.GridSpecFromSubplotSpec(4, 1, gs_aux1[0, 3], hspace=1.5,
                                           height_ratios=[1.,1.,1.,1.])
    gs_aux4 = gs.GridSpecFromSubplotSpec(1, 4, gs_aux[1, 0], wspace=.7,
                                           width_ratios=[0.15,1., 1.0, 1.0,])
    return {
            # these are needed for proper labelling
            # core.make_axes takes care of them

                        
            "network_schema" : gs_aux[0, 0],

            "spikes_before" : gs_aux2[0, 0],
            
            "spikes_after" : gs_aux3[0, 0],
            
            "spikes_before_teach" : gs_aux2[1, 0],
            
            "spikes_after_teach" : gs_aux3[1, 0],
            
            "histo_before":  gs_aux2[2, 0],
            
            "histo_after":  gs_aux3[2, 0],

            "voltage_before" : gs_aux2[3, 0],
            
            "voltage_after" : gs_aux3[3, 0],
            
            "weightpath_euc" : gs_aux4[0, 1],
            
            "weightpath_nat" :gs_aux4[0,2],
            
            "learningcurve":gs_aux4[0,3]
        }

def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.itervalues():
        core.hide_axis(ax)

    for k in [
            "network_schema"
        ]:
        axes[k].set_frame_on(False)

def plot_labels(axes):
    core.plot_labels(axes,
        labels_to_plot=[
            "network_schema",
            "spikes_before",            
            "spikes_after",
            #"spikes_before_teach",            
            #"spikes_after_teach",
            #"histo_before",
            #"histo_after",
            #"voltage_before",
            #"voltage_after",
            "weightpath_euc",
            "weightpath_nat",
            "learningcurve"
        ],
        label_ypos = {"network_schema":1.,
            "spikes_before":1.,
            "spikes_after":1.,
            "spikes_before_teach":1.,            
            "spikes_after_teach":1.,
            "histo_before":1.,
            "histo_after":1.,
            "voltage_before":1.,
            "voltage_after":1.,
            "weightpath_euc":1.,
            "weightpath_nat":1.,
            "learningcurve":1.,
                      },
        label_xpos = { "network_schema": 0.02,
                      "spikes_before":0.02,
                      "spikes_after":0.02,
                      "spikes_before":0.02,            
                      "spikes_after":0.02,
                      "histo_before":0.02,
                      "histo_after":0.02,
                      "voltage_before":0.02,
                    "voltage_after":0.02,
                    "weightpath_euc":0.02,
                    "weightpath_nat":0.02,
                    "learningcurve":0.02
                    }
        )

def get_fig_kwargs():
    return { "figsize" : (18/2.54, 14./2.54) }



###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
#
def plot_network_schema(ax):
    
    pass


def plot_spikes_before(ax):
    
    data = core.get_data('fig3/2019-02-02_output_spikes_psth_start.npy')
    
    ax.scatter(np.nonzero(data)[1],np.nonzero(data)[0],color=core.label_to_color["natural"],s=0.01)
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes"])
    ax.set_ylabel(core.y_labels["spikes"])

    pass



    
def plot_spikes_after(ax):
    
    data = core.get_data('fig3/2019-02-02_output_spikes_psth_end.npy')

    print(np.shape(np.nonzero(data)))
    ax.scatter(np.nonzero(data)[1],np.nonzero(data)[0],color=core.label_to_color["natural"],s=0.01)
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes"])
    ax.set_ylabel(core.y_labels["spikes"])

    
    pass

def plot_spikes_before_teach(ax):
    
    
    data_teach=core.get_data("fig3/2019-02-02_output_spikes_psth_teacher.npy")
    
    ax.scatter(np.nonzero(data_teach)[1],np.nonzero(data_teach)[0],color=core.label_to_color["teacher"],s=0.01)
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes_teach"])
    ax.set_ylabel(core.y_labels["spikes_teach"])


    pass



    
def plot_spikes_after_teach(ax):
    
    
    data_teach=core.get_data("fig3/2019-02-02_output_spikes_psth_teacher.npy")
    
    ax.scatter(np.nonzero(data_teach)[1],np.nonzero(data_teach)[0],color=core.label_to_color["teacher"],s=0.01)
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes_teach"])
    ax.set_ylabel(core.y_labels["spikes_teach"])

    
    pass

def plot_histo_before(ax):
    
    data = core.get_data('fig3/2019-02-02_output_spikes_psth_start.npy')
    data_teach=core.get_data("fig3/2019-02-02_output_spikes_psth_teacher.npy")
    print("data",np.shape(data))
    spiketimes=np.nonzero(data)[1]*0.0005
    spiketimes_teach=np.nonzero(data_teach)[1]*0.0005
    
    
    ax.set_prop_cycle(cycler('color',[core.label_to_color["natural"],core.label_to_color["teacher"]] ))
    
    bins=np.linspace(0.,0.25,20,endpoint=False)
    ax.hist([spiketimes,spiketimes_teach], bins, label=['x', 'y'],normed=1.)

    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["histo"])
    ax.set_ylabel(core.y_labels["histo"])
    
    pass

def plot_histo_after(ax):
    
    data = core.get_data('fig3/2019-02-02_output_spikes_psth_end.npy')
    data_teach=core.get_data("fig3/2019-02-02_output_spikes_psth_teacher.npy")
    print("data",np.shape(data))
    spiketimes=np.nonzero(data)[1]*0.0005
    spiketimes_teach=np.nonzero(data_teach)[1]*0.0005
    
    
    ax.set_prop_cycle(cycler('color',[core.label_to_color["natural"],core.label_to_color["teacher"]] ))
    
    bins=np.linspace(0.,0.25,20,endpoint=False)
    ax.hist([spiketimes,spiketimes_teach], bins, label=['x', 'y'],normed=1.)

    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["histo"])
    ax.set_ylabel(core.y_labels["histo"])
    
    pass

def plot_voltage_before(ax):
    data = core.get_data('fig3/2019-02-02_membrane_potential_psth_start.npy')[10]
    data_teach=core.get_data("fig3/2019-02-02_membrane_potential_psth_teacher.npy")[10]
    time_params=core.get_data("fig3/time_parameters.npy").item()
    #ax.set_xlim([0.,.5])
    
    #subtract resting potential
    data=data-70.
    data_teach=data_teach-70.
    
    time=np.arange(0.,500,1.)*time_params["dt"]
    
    ax.set_prop_cycle(cycler('color',[core.label_to_color["natural"],core.label_to_color["teacher"]] ))
    
    ax.plot(time,data,color=core.label_to_color["natural"],linewidth=core.linewidth["voltage"])
    ax.plot(time,data_teach,color=core.label_to_color["teacher"],linewidth=core.linewidth["voltage"])


    core.show_axis(ax)
    core.make_spines(ax)

    #plotf.trace_plot(data)
    ax.set_xlabel(core.x_labels["voltage_trace"])
    ax.set_ylabel(core.y_labels["voltage_trace"])
    #ax.legend(("student","teacher"),loc=0,fontsize=8.,labelspacing=0.1,borderaxespad=0.1,borderpad=0.,handlelength=0.5,frameon=False)
    

    pass

def plot_voltage_after(ax):
    data = core.get_data('fig3/2019-02-02_membrane_potential_psth_end.npy')[10]
    data_teach=core.get_data("fig3/2019-02-02_membrane_potential_psth_teacher.npy")[10]
    time_params=core.get_data("fig3/time_parameters.npy").item()
    #ax.set_xlim([0.,.5])

    time=np.arange(0,500)*time_params["dt"]
    
    #subtract resting potential
    data=data-70.
    data_teach=data_teach-70.

    ax.plot(time,data,color=core.label_to_color["natural"],linewidth=core.linewidth["voltage"])
    ax.plot(time,data_teach,color=core.label_to_color["teacher"],linewidth=core.linewidth["voltage"])

    core.show_axis(ax)
    core.make_spines(ax)

    #plotf.trace_plot(data)
    ax.set_xlabel(core.x_labels["voltage_trace"])
    ax.set_ylabel(core.y_labels["voltage_trace"])
   #ax.legend(("student","teacher"),loc=0,fontsize=8.,labelspacing=0.1,borderaxespad=0.1,borderpad=0.,handlelength=0.5,frameon=False)
    


    pass

def plot_weightpath_euc(ax):
    import parameter_vectorplot as parameter
    
    para=parameter.parameter
    para["color"]=core.label_to_color["euclidean"]
    N=2
    
    
    
    data_quiver = core.get_data('fig3/2019-01-07_vectorplot_euc.npy')
    data_wpath=core.get_data("fig3/2018-08-24_ewpath.npy")
    data_wpath=N*data_wpath
    norm_data=np.sqrt(np.square(data_quiver[:,:,0])+np.square(data_quiver[:,:,1]))
    data_quiver[:,:,0]=data_quiver[:,:,0]/norm_data
    data_quiver[:,:,1]=data_quiver[:,:,1]/norm_data
    
    data_cost=core.get_data('fig3/2019-01-07_contour_cost.npy')
    
    plotf.wpathplot(ax,data_quiver,data_wpath,**para)
    
    
    
    levels=[0.001,0.003,0.005,0.009,0.015,0.02,0.03,0.04]
    plotf.contourplot(ax,data_cost, levels=levels,**para)
    
    #normalize
    
    core.show_axis(ax)
    core.make_spines(ax)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    

    ax.set_xlabel(core.x_labels["weight_path"])
    ax.set_ylabel(core.y_labels["weight_path"])


    pass

def plot_weightpath_nat(ax):
       
    import parameter_vectorplot as parameter
    N=2
    
    para=parameter.parameter
    para["color"]=core.label_to_color["natural"]
    
    
    
    data_quiver = core.get_data('fig3/2019-01-07_vectorplot_nat.npy')
    data_cost=core.get_data('fig3/2019-01-07_contour_cost.npy')
    data_wpath=core.get_data("fig3/2018-08-24_nwpath.npy")
    data_wpath=N*data_wpath
    
    #normalize
    norm_data=np.sqrt(np.square(data_quiver[:,:,0])+np.square(data_quiver[:,:,1]))
    data_quiver[:,:,0]=data_quiver[:,:,0]/norm_data
    data_quiver[:,:,1]=data_quiver[:,:,1]/norm_data
    
    plotf.wpathplot(ax,data_quiver,data_wpath,**para)
    
    
    levels=[0.001,0.003,0.005,0.009,0.015,0.02,0.03,0.04]
    plotf.contourplot(ax,data_cost, levels=levels,**para)
    
   
    core.show_axis(ax)
    core.make_spines(ax)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    

    ax.set_xlabel(core.x_labels["weight_path"])
    ax.set_ylabel(core.y_labels["weight_path"])


    pass
    
   

def plot_learningcurve(ax):
    data_nat=core.get_data("fig3/2018-08-24_naturalgradient_KL_errorN100.npy")
    data_euc=core.get_data("fig3/2018-08-24_euclideangradient_KL_errorN100.npy")
    #data_nat_std=core.get_data("fig3/2018-08-24_naturalgradient_rate_error_std.npy")
    #data_euc_std=core.get_data("fig3/2018-08-24_euclideangradient_rate_error_std.npy")
    data_time=np.arange(0.,16.,1.)*400./60.#core.get_data("fig3/lc_time.npy")
    
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.semilogy(data_time,data_euc[0:16],color=core.label_to_color["euclidean"],linewidth=core.linewidth["normal"])
    ax.semilogy(data_time,data_nat[0:16],color=core.label_to_color["natural"],linewidth=core.linewidth["normal"])
    
    #ax.plot(data_time,data_euc+data_euc_std,color=core.label_to_color["euclidean"],linewidth=core.linewidth["normal"])
    #ax.plot(data_time,data_nat+data_nat_std,color=core.label_to_color["natural"],linewidth=core.linewidth["normal"])
    
    #ax.plot(data_time,data_euc-data_euc_std,color=core.label_to_color["euclidean"],linewidth=core.linewidth["normal"])
    #ax.plot(data_time,data_nat-data_nat_std,color=core.label_to_color["natural"],linewidth=core.linewidth["normal"])
    
    ax.set_xlabel(core.x_labels["lc"])
    ax.set_ylabel(core.y_labels["lc"])
    ax.legend(("Euclidean gradient","Natural gradient"),loc=0,fontsize=8.,labelspacing=0.1,borderaxespad=0.1,borderpad=0.,handlelength=0.5,frameon=False)
    




