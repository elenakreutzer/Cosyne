#!/usr/bin/env python2
# encoding: utf-8

import matplotlib as mpl

import matplotlib.image as mpimg
from matplotlib import gridspec as gs
from matplotlib import collections as coll
import pylab as p
p.style.use(['matplotlibrc'])
import copy
import numpy as np
import plotfunctions as plotf
from cycler import cycler

import core
from core import log

#set global plot parameters
#mpl.rcParams['axes.labelsize'] = core.linewidth["labelsize"]
#mpl.rcParams['xtick.labelsize'] = core.linewidth["ticksize"]
#mpl.rcParams['ytick.labelsize'] = core.linewidth["ticksize"]



def get_gridspec():
    """
        Return dict: plot -> gridspec
    """
    # TODO: Adjust positioning
    gs_main = gs.GridSpec(1, 1, hspace=.65,
                          left=0.02, right=0.95, top=.9, bottom=0.15)
    gs_aux = gs.GridSpecFromSubplotSpec(1, 5, gs_main[0, 0], wspace=1.3,
                                           width_ratios=[.3,.1,2.,2.,2.])
    gs_aux2 = gs.GridSpecFromSubplotSpec(2, 1, gs_aux[0, 2], hspace=1.,
                                           height_ratios=[2., 1.2])
    gs_aux3 = gs.GridSpecFromSubplotSpec(2, 1, gs_aux[0, 3], hspace=1.,
                                           height_ratios=[2., 1.2])
    gs_aux4 = gs.GridSpecFromSubplotSpec(2, 1, gs_aux[0, 4], hspace=1.,
                                           height_ratios=[2., 1.2])
    gs_aux5=gs.GridSpecFromSubplotSpec(15, 1, gs_aux[0, 0], hspace=.1,
                                           height_ratios=[1.,1.,1.,1.,1.,1.,1.,1., 1.,1.,1.,1.,1.,1., 1.])

    return {
            # these are needed for proper labelling
            # core.make_axes takes care of them
            "placeholder":gs_aux5[0,0],
            
            "placeholder1":gs_aux5[1,0],
            
            "placeholder2":gs_aux5[3,0],
            
            "spikes_stim":gs_aux5[2,0],
            
            "spikes_stim1":gs_aux5[4,0],
            
            "spikes_stim2":gs_aux5[6,0],
            
            "spikes_post":gs_aux5[14,0],
                        
            "stimulation_schema" : gs_aux[0, 1],

            "heatplot_homsyn" : gs_aux2[0, 0],
            
            "heatplot_heterosyn" : gs_aux3[0, 0],

            "heatplot_hom_het_comparison" : gs_aux4[0, 0],
            
            "phase1" : gs_aux2[1, 0],
            
            "phase2" : gs_aux3[1, 0],
            
            "phase3" :gs_aux4[1,0]
        }

def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.itervalues():
        core.hide_axis(ax)

    for k in [
            "placeholder",
            "placeholder1",
            "placeholder2",
            "spikes_stim",
            "spikes_stim1",
            "spikes_stim2",
            "spikes_post",
            "stimulation_schema"
        ]:
        axes[k].set_frame_on(False)

def plot_labels(axes):
    core.plot_labels(axes,
        labels_to_plot=[
            "placeholder",
            "heatplot_homsyn",
            "heatplot_heterosyn",
            "heatplot_hom_het_comparison",
            "phase1",
            "phase2",
            "phase3"
        ],
        label_ypos = {"placeholder":.9,
            "heatplot_homsyn":1.,
            "heatplot_heterosyn":1.,
            "heatplot_hom_het_comparison":1.,
            "phase1":1.,
            "phase2":1.,
            "phase3":1.
                      },
        label_xpos = { "placeholder": 0.02,
                    "heatplot_heterosyn": 0.02,
                    "heatplot_homosyn":0.02,
                    "heatplot_hom_het_comparison":0.02,
                    "phase1":0.02,
                    "phase2":0.02,
                    "phase3":0.02
                    }
        )

def get_fig_kwargs():
    return { "figsize" : (18.5/2.54,6.8/2.54) }



###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
    
#
    
def plot_placeholder(ax):
    
    pass

def plot_placeholder1(ax):
    
    pass

def plot_placeholder2(ax):
    
    pass


def plot_spikes_stim(ax):
    data=core.get_data('fig5/inputspikes_stim_illu.npy')
    
    ax.plot(data[5,0:500],color=core.label_to_color["aux_lines"],linewidth=core.linewidth["spikes"])
    
    core.hide_axis(ax)
    
    
    pass    

def plot_spikes_stim1(ax):
    data=core.get_data('fig5/inputspikes_stim_illu.npy')
    
    ax.plot(data[1,0:500],color=core.label_to_color["aux_lines"],linewidth=core.linewidth["spikes"])
    
    core.hide_axis(ax)
    
    
    pass    

def plot_spikes_stim2(ax):
    data=core.get_data('fig5/inputspikes_stim_illu.npy')
    
    ax.plot(data[20,0:500],color=core.label_to_color["aux_lines"],linewidth=core.linewidth["spikes"])
    
    core.hide_axis(ax)
    
    
    pass    

def plot_spikes_post(ax):
    data=core.get_data('fig5/teacher_spikes_illu.npy')
    ax.plot(data[10,0:500],color=core.label_to_color["aux_lines"],linewidth=core.linewidth["spikes"])
    
    core.hide_axis(ax)
    
    pass    

def plot_stimulation_schema(ax):
    
    pass


def plot_heatplot_homsyn(ax):
    data = core.get_data('fig5/Delta_w_hom_grid.npy')
    data_aux = core.get_data('fig5/Delta_w_het_grid.npy')
    w_range = core.get_data('fig5/w_range.npy')

    
    vmin=min(np.amin(data),np.amin(data_aux))
    vmax=max(np.amax(data),np.amax(data_aux))
    
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    label=r"$\Delta w_{\mathrm{st}}$ [%]"
    labelpad=-8.

    plotf.hplot(ax,data,vmin,vmax,w_range,label,labelpad)
    ax.axhline(y=1.85,color=core.label_to_color["aux_line_heat"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.set_xlabel(core.x_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])
    ax.set_ylabel(core.y_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])


    pass

def plot_heatplot_heterosyn(ax):
    data =core.get_data('fig5/Delta_w_het_grid.npy')
    data_aux=core.get_data('fig5/Delta_w_hom_grid.npy')
    
    vmin=min(np.amin(data),np.amin(data_aux))
    vmax=max(np.amax(data),np.amax(data_aux))
    
    
    w_range = core.get_data('fig5/w_range.npy')
    
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    label=r"$\Delta w_{\mathrm{ust}}$ [%]"
    labelpad=-8.

    plotf.hplot(ax,data,vmin,vmax,w_range,label,labelpad)
    ax.axhline(y=1.85,color=core.label_to_color["aux_line_heat"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.set_xlabel(core.x_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])
    ax.set_ylabel(core.y_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])

    pass

def plot_heatplot_hom_het_comparison(ax):
    data = core.get_data('fig5/Sign_delta_w_comparison.npy')
    
    w_range = core.get_data('fig5/w_range.npy')

    core.show_axis(ax)
    core.make_spines(ax)
    labelpad=-1.
    
    label=r"$\rm{Sign}(\Delta w_{\mathrm{st}}\times\Delta w_{\mathrm{unst}})$"

    plotf.hplot(ax,data,-1.,1.,w_range,label=label,labelpad=labelpad)
    ax.axhline(y=1.85,color=core.label_to_color["aux_line_heat"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    
    ax.set_xlabel(core.x_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])
    ax.set_ylabel(core.y_labels["heat_plot"],labelpad=core.linewidth["lp_heat"])

    
    pass

def plot_phase1(ax):
    data_hom = core.get_data('fig5/w_hom_phase1.npy')
    data_het = core.get_data('fig5/w_het_phase1.npy')
    time_params=core.get_data('fig5/time_parameters.npy').item()
    
    ax.set_xlim([-.5,5.5])
    x_ticks = np.array((0.,2.5,5.))
    ax.xaxis.set_ticks(x_ticks) 
    
    
    weighttrace=np.concatenate(((data_hom,),(data_het,)))
    
    ax.set_prop_cycle(cycler('color',[core.label_to_color["stim"],core.label_to_color["unstim"]] ))

    core.show_axis(ax)
    core.make_spines(ax)
    
   
    
    plotf.trace_plot(ax,weighttrace,time_params,linewidth=core.linewidth["normal"])
    ax.axvline(x=0,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(0.,10.,r"$t_0$")
    
    ax.axvline(x=5,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(5.,10.,r"$t_1$")
    
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot"])
    

    pass

def plot_phase2(ax):
    data_hom = core.get_data('fig5/w_hom_phase2.npy')
    data_het = core.get_data('fig5/w_het_phase2.npy')
    time_params=core.get_data('fig5/time_parameters.npy').item()
    
    ax.set_xlim([-.5,5.5])
    x_ticks = np.array((0.,2.5,5.))
    ax.xaxis.set_ticks(x_ticks) 
    
    
    
    
    weighttrace=np.concatenate(((data_hom,),(data_het,)))
    
    ax.set_prop_cycle(cycler('color',[core.label_to_color["stim"],core.label_to_color["unstim"]] ))

    core.show_axis(ax)
    core.make_spines(ax)
    

    plotf.trace_plot(ax,weighttrace,time_params,linewidth=core.linewidth["normal"])
    ax.axvline(x=0,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(0.,98.,r"$t_0$")
    ax.axvline(x=5,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(5.,98.,r"$t_1$")
    
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot"])


    pass

def plot_phase3(ax):
    
    data_hom = core.get_data('fig5/w_hom_phase3.npy')
    data_het = core.get_data('fig5/w_het_phase3.npy')
    time_params=core.get_data('fig5/time_parameters.npy').item()
    ax.set_xlim([-.5,5.5])
    x_ticks = np.array((0.,2.5,5.))
    ax.xaxis.set_ticks(x_ticks) 
    
    weighttrace=np.concatenate(((data_hom,),(data_het,)))
    ax.set_prop_cycle(cycler('color',[core.label_to_color["stim"],core.label_to_color["unstim"]]))

    core.show_axis(ax)
    core.make_spines(ax)

    plotf.trace_plot(ax,weighttrace,time_params,linewidth=core.linewidth["normal"])
    ax.axvline(x=0,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(0.,99.05,r"$t_0$")
    ax.axvline(x=5,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(5.,99.05,r"$t_1$")
    
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot"])
    ax.legend((r"$w_{\rm st}$",r"$w_{\rm ust}$"),loc=0,fontsize=8.,labelspacing=0.1,borderaxespad=0.1,borderpad=0.,handlelength=0.5,frameon=False)
    


    
    pass




