#!/usr/bin/env python2
# encoding: utf-8

import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib import gridspec as gs
from matplotlib import collections as coll
from matplotlib import transforms
import matplotlib.pyplot as plt
import pylab as p
import copy
import numpy as np
import plotfunctions as plotf
from cycler import cycler
import matplotlib.ticker as ticker



import core
from core import log


def get_gridspec():
    """
        Return dict: plot -> gridspec
    """
    # TODO: Adjust positioning
    gs_main = gs.GridSpec(1, 1, hspace=0.65,
                          left=0.1, right=0.9, top=.9, bottom=0.1)
    gs_aux = gs.GridSpecFromSubplotSpec(2, 1, gs_main[0, 0], hspace=0.25,
                                           height_ratios=[0.5, 0.5,])
    gs_aux1 = gs.GridSpecFromSubplotSpec(1, 2, gs_aux[0, 0], wspace=.65,
                                           width_ratios=[1.0, 1.0,])
    gs_aux1a = gs.GridSpecFromSubplotSpec(2, 1, gs_aux1[0, 0], hspace=.7,
                                           height_ratios=[1.0, 1.0,])
    gs_aux1b = gs.GridSpecFromSubplotSpec(2, 1, gs_aux1[0, 1], hspace=.7,
                                           height_ratios=[1.0, 1.0,])
    
    gs_aux2 = gs.GridSpecFromSubplotSpec(1,2, gs_aux[1, 0], wspace=.65,
                                           width_ratios=[1.,1.])
    gs_aux2a = gs.GridSpecFromSubplotSpec(1,2, gs_aux2[0, 0], wspace=1.5,
                                           width_ratios=[.3,.7])
    gs_aux3=gs.GridSpecFromSubplotSpec(3,1, gs_aux2a[0, 0], hspace=1.,
                                           height_ratios=[1., 1.,1.])
    gs_aux4=gs.GridSpecFromSubplotSpec(3,1, gs_aux2a[0, 1], hspace=1.,
                                           height_ratios=[1., 1.,1.])
    gs_aux5=gs.GridSpecFromSubplotSpec(2,1, gs_aux2[0, 1], hspace=0.4,
                                           height_ratios=[1., 1.])
    

    return {
            # these are needed for proper labelling
            # core.make_axes takes care of them

                        
            "attenuation_example_perc" : gs_aux1a[0, 0],

            "attenuation_summary_perc" : gs_aux1b[0, 0],
            
            "attenuation_example_abs" : gs_aux1a[1, 0],

            "attenuation_summary_abs" : gs_aux1b[1, 0],
            
            "var_hist_hr_ht":       gs_aux3[0,0],
            
            "var_hist_lr_ht":       gs_aux3[1,0],
             
            "var_hist_hr_lt":      gs_aux3[2,0],
                
            
            "var_highr_hightau" : gs_aux4[0, 0],

            "var_lowr_hightau" : gs_aux4[1, 0],
            
            "var_highr_lowtau" : gs_aux4[2, 0],
            
            "var_result_example" : gs_aux5[0, 0],
            
            "var_result_summary" :gs_aux5[1,0]
        }

def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.itervalues():
        core.hide_axis(ax)

    #for k in [
    #        "dummy1",
    #        "dummy2"
    #    ]:
    #    axes[k].set_frame_on(False)

def plot_labels(axes):
    core.plot_labels(axes,
        labels_to_plot=[
            "attenuation_example_perc",
            "attenuation_summary_perc",
            "attenuation_example_abs",
            "attenuation_summary_abs",
            "var_hist_hr_ht",
            "var_hist_lr_ht",
            "var_hist_hr_lt",
            "var_highr_hightau",
            "var_lowr_hightau",
            "var_highr_lowtau",
            "var_result_example",
            "var_result_summary"
        ],
        label_ypos = {"attenuation_example_perc":1.,
            "attenuation_summary_perc":1.,
            "attenuation_example_abs":1.,
            "attenuation_summary_abs":1.,
            "var_hist_hr_ht":1.,
            "var_hist_lr_ht":1.,
            "var_hist_hr_lt":1.,
            "var_highr_hightau":1.,
            "var_lowr_hightau":1.,
            "var_highr_lowtau":1.,
            "var_result_example":1.,
            "var_result_summary":1.
                      },
        label_xpos = { "attenuation_example_perc":0.02,
            "attenuation_summary_perc":0.02,
            "attenuation_example_abs":0.02,
            "attenuation_summary_abs":0.02,
            "var_hist_hr_ht":0.02,
            "var_hist_lr_ht":0.02,
            "var_hist_hr_lt":0.02,
            "var_highr_hightau":0.02,
            "var_lowr_hightau":0.02,
            "var_highr_lowtau":0.02,
            "var_result_example":0.02,
            "var_result_summary":0.02
                    }
        )

def get_fig_kwargs():
    return { "figsize" : (15./2.54, 20./2.54) }



###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
#
def plot_attenuation_example_perc(ax):
    data_prox = core.get_data('fig6/attenuation_proximal_synapse.npy')
    data_dist = core.get_data('fig6/attenuation_distal_synapse.npy')
    time_params=core.get_data('fig6/time_parameters.npy').item()
   
    ax.set_prop_cycle(cycler(color=[core.label_to_color["attenuation_ldist"],core.label_to_color["attenuation_hdist"]],linestyle=['-', '-.'] ))
    weighttrace=np.concatenate(((data_prox,),(data_dist,)))
    
    core.show_axis(ax)
    core.make_spines(ax)

    plotf.trace_plot(ax,weighttrace,time_params,linewidth=core.linewidth["normal"])
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot_dend"])
    
    ax.legend((r"$d=3\mu m$",r"$d=7\mu m$"),loc=2,fontsize=8.,handlelength=0.5,frameon=False)
    

    
    pass

def plot_attenuation_summary_perc(ax):
    
    ax.set_xlim([0.,11.])
    
    data_wchange = core.get_data('fig6/att_weight_change_perc.npy')
    data_dist = core.get_data('fig6/distances.npy')
    color=[core.label_to_color["attenuation_im"]]*np.shape(data_dist)[0]
    color[2]=core.label_to_color["attenuation_ldist"]
    color[-3]=core.label_to_color["attenuation_hdist"]
    core.show_axis(ax)
    core.make_spines(ax)

    ax.scatter(data_dist,data_wchange,color=color,s=core.linewidth["scatter"])
    ax.get_yaxis().get_major_formatter().set_scientific(False)#prevent exponent notation on axis
    ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))#cut y axis ticks 2 digits behind floating point
    ticks = np.linspace(0.,50.,2.)
    ax.yaxis.set_ticks(ticks) 
    ax.set_xlabel(r"$d[\mu m]$")
    ax.set_ylabel(core.y_labels["weightchange_dend"])
    


    pass

def plot_attenuation_example_abs(ax):
    data_prox = core.get_data('fig6/attenuation_proximal_synapse.npy')
    data_dist = core.get_data('fig6/attenuation_distal_synapse.npy')
    time_params=core.get_data('fig6/time_parameters.npy').item()
    ax.set_prop_cycle(cycler('color',[core.label_to_color["attenuation_ldist"],core.label_to_color["attenuation_hdist"]] ))
    weighttrace=np.concatenate(((data_prox,),(data_dist,)))
    
    core.show_axis(ax)
    core.make_spines(ax)

    plotf.trace_plot(ax,weighttrace,time_params,perc=False,linewidth=core.linewidth["normal"])
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot_dend_abs"])
   # ax.legend((r"$d=3\mu m$",r"$d=7\mu m$"),loc=2,fontsize=8.,handlelength=0.5,frameon=False)

    
    pass


def plot_attenuation_summary_abs(ax):
    
    ax.set_xlim([0.,11.])
    
    data_wchange = core.get_data('fig6/att_weight_change_abs.npy')
    data_dist = core.get_data('fig6/distances.npy')
    color=[core.label_to_color["attenuation_im"]]*np.shape(data_dist)[0]
    color[2]=core.label_to_color["attenuation_ldist"]
    color[-3]=core.label_to_color["attenuation_hdist"]
    core.show_axis(ax)
    core.make_spines(ax)

    ax.scatter(data_dist,data_wchange,color=color,s=core.linewidth["scatter"])
    ax.set_xlabel(r"$d[\mu m]$")
    ax.set_ylabel(core.y_labels["weightchange_dend_abs"])
    

    pass



def plot_var_hist_hr_ht(ax):
    data_usp = core.get_data('fig6/histogram_hr_ht.npy')   


    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,5.])
    
    
    
    counts,bins,patches=ax.hist(data_usp,bins=np.arange(0.,25.,.5),log=1,orientation="horizontal",density=1,rwidth=1.,color=core.label_to_color["hr_ht"])
    ax.set_xlim(ax.get_xlim()[::-1])
   
    ax.spines['left'].set_position(('axes', 1.))
    ax.tick_params(axis="y",direction="in", pad=-15.)
    ax.tick_params(axis="x",direction="out", pad=-0.3)
   
    core.show_axis(ax)
    core.make_spines(ax)
    tick_formatter =ticker.LogFormatterExponent()
    ax.xaxis.set_major_formatter(tick_formatter)

    
    ax.set_xlabel(core.x_labels["hist"],labelpad=-2.)
    
    
    
    pass

def plot_var_hist_lr_ht(ax):
    data_usp = core.get_data('fig6/histogram_hr_lt.npy')
    
    
    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,5.])
    
    counts,bins,patches=ax.hist(data_usp,bins=np.arange(0.,25.,.5),log=1,orientation="horizontal",density=1,rwidth=1.,color=core.label_to_color["lr_ht"])

    ax.set_xlim(ax.get_xlim()[::-1])
   
    ax.spines['left'].set_position(('axes', 1.))
    ax.tick_params(axis="y",direction="in", pad=-15.)
    ax.tick_params(axis="x",direction="out", pad=-0.3)
   
    core.show_axis(ax)
    core.make_spines(ax)
    tick_formatter =ticker.LogFormatterExponent()
    ax.xaxis.set_major_formatter(tick_formatter)
    
    ax.set_xlabel(core.x_labels["hist"],labelpad=-2.)
    
    
    pass


def plot_var_hist_hr_lt(ax):
    data_usp = core.get_data('fig6/histogram_lr_ht.npy')
  
    
    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,5.])
    
    counts,bins,patches=ax.hist(data_usp,bins=np.arange(0.,25.,.5),log=1,orientation="horizontal",density=1,rwidth=1.,color=core.label_to_color["hr_lt"])

    ax.set_xlim(ax.get_xlim()[::-1])

    ax.spines['left'].set_position(('axes', 1.))
    ax.tick_params(axis="y",direction="in", pad=-15.)
    ax.tick_params(axis="x",direction="out", pad=-0.3)
   
    core.show_axis(ax)
    core.make_spines(ax)
    tick_formatter =ticker.LogFormatterExponent()
    ax.xaxis.set_major_formatter(tick_formatter)
    
    ax.set_xlabel(core.x_labels["hist"],labelpad=-2.)
    
    pass

def plot_var_highr_hightau(ax):
    data = core.get_data('fig6/usp_trace_hr_ht.npy')[0]

    
    
    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,0.5])
    time_params=core.get_data('fig6/time_parameters.npy').item()
    time=np.arange(0,time_params["learning_time"],time_params["dt"])
    ax.text(0.3,22,r"$r_1=10\rm{ Hz }$")
    ax.text(0.3,17,r"$\tau_1=15\rm{ ms}$")
    core.show_axis(ax)
    core.make_spines(ax)

    ax.plot(time,data,color=core.label_to_color["hr_ht"],linewidth=core.linewidth["normal"])
    
    ax.set_xlabel(core.x_labels["usp_trace"])
    ax.set_ylabel(core.y_labels["usp_trace"])
    
    
    
    pass

def plot_var_lowr_hightau(ax):
    data = core.get_data('fig6/usp_trace_lr_ht.npy')[0]
    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,0.5])
    time_params=core.get_data('fig6/time_parameters.npy').item()
    time=np.arange(0,time_params["learning_time"],time_params["dt"])
    ax.text(0.3,22,r"$r_2=5\rm{ Hz }$")
    ax.text(0.3,17,r"$\tau_2=15\rm{ ms}$")
    core.show_axis(ax)
    core.make_spines(ax)

    ax.plot(time,data,color=core.label_to_color["lr_ht"],linewidth=core.linewidth["normal"])
    
    ax.set_xlabel(core.x_labels["usp_trace"])
    ax.set_ylabel(core.y_labels["usp_trace"])
    pass

def plot_var_highr_lowtau(ax):
    data = core.get_data('fig6/usp_trace_hr_lt.npy')[0]
    ax.set_ylim([0.,20.])
    ax.set_xlim([0.,0.5])
    time_params=core.get_data('fig6/time_parameters.npy').item()
    time=np.arange(0,time_params["learning_time"],time_params["dt"])
    ax.text(0.3,22,r"$r_3=10\rm{ Hz }$")
    ax.text(0.3,17,r"$\tau_3=5\rm{ ms}$")
    core.show_axis(ax)
    core.make_spines(ax)

    ax.plot(time,data,color=core.label_to_color["hr_lt"],linewidth=core.linewidth["normal"])
    
    ax.set_xlabel(core.x_labels["usp_trace"])
    ax.set_ylabel(core.y_labels["usp_trace"])

    pass

def plot_var_result_example(ax):
    ax.set_xlim([-0.0,5.5])
    data_hr_ht = core.get_data('fig6/variance_hr_ht.npy')
    data_lr_ht = core.get_data('fig6/variance_lr_ht.npy')
    data_hr_lt = core.get_data('fig6/variance_hr_lt.npy')
    time_params=core.get_data('fig6/time_parameters.npy').item()


    weighttrace=np.concatenate(((data_hr_ht,),(data_lr_ht,),(data_hr_lt,)))
    
    core.show_axis(ax)
    core.make_spines(ax)
    ax.set_prop_cycle(cycler('color',[core.label_to_color["hr_ht"],core.label_to_color["lr_ht"],core.label_to_color["hr_lt"]] ))

    plotf.trace_plot(ax,weighttrace,time_params,linewidth=core.linewidth["normal"])
    ax.axvline(x=5,color=core.label_to_color["aux_lines"],linewidth=core.linewidth["aux_lines"],ls="dashed")
    ax.text(5.,75.,r"$t_0$")
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot"])
    ax.legend((r"$w_1$",r"$w_2$",r"$w_3$"),loc=2,fontsize=8.,handlelength=0.5,frameon=False)
    




    pass

def plot_var_result_summary(ax):
    
    ax.set_xlim([0.,31.])
    
    data_wchange = core.get_data('fig6/wfinal_com.npy')
    data_dist = core.get_data('fig6/usp_var_com.npy')


    core.show_axis(ax)
    core.make_spines(ax)
    color=[core.label_to_color["attenuation_im"]]*np.shape(data_dist)[0]
    color[4]=core.label_to_color["lr_ht"]
    color[20]=core.label_to_color["hr_lt"]
    color[24]=core.label_to_color["hr_ht"]
    
    
    ax.scatter(data_dist,data_wchange,color=color,s=core.linewidth["scatter"])
    ax.set_xlabel(r'$\sigma^2(\mathrm{USP})$')
    ax.set_ylabel(core.y_labels["weightchange"])
    
    pass




