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
    
    gs_main = gs.GridSpec(4, 1, hspace=0.6,
                          left=0.05, right=0.95, top=.9, bottom=0.1,
                          height_ratios=[.5,1.,1.,.9])
    gs_aux0 = gs.GridSpecFromSubplotSpec(1, 4, gs_main[0, 0], wspace=0.6,
                                          width_ratios=[1.0, 1.0,1.0,1.0])
    gs_aux1 = gs.GridSpecFromSubplotSpec(1, 4, gs_main[1, 0], wspace=0.6,
                                          width_ratios=[1.0, 1.0,1.0,1.0])
    gs_aux2 = gs.GridSpecFromSubplotSpec(1, 4, gs_main[2, 0], wspace=0.6,
                                          width_ratios=[1.0, 1.0,1.0,1.0])
    gs_aux3 = gs.GridSpecFromSubplotSpec(1, 4, gs_main[3, 0], wspace=0.6,
                                          width_ratios=[1.0, 1.0,1.0,1.0])

    return {
            # these are needed for proper labelling
            # core.make_axes takes care of them

            "dummy1" : gs_aux0[0, 0],
            "spikes_before_teach" : gs_aux0[0, 1],
            "spikes_before" : gs_aux0[0, 2],
            "spikes_after" : gs_aux0[0, 3],
            
            "dummy5" : gs_aux1[0, 0],
            "weightpath_euc" : gs_aux1[0, 1],
            "weightpath_nat" : gs_aux1[0, 2],
            "learningcurve" : gs_aux1[0, 3],
            
            "dummy9" : gs_aux2[0, 0],
            "heatplot_homsyn" : gs_aux2[0, 1],
            "heatplot_heterosyn" : gs_aux2[0, 2],
            "heatplot_hom_het_comparison" : gs_aux2[0, 3],
            
            "attenuation_summary_abs" : gs_aux3[0, 0],
            "attenuation_example_abs" : gs_aux3[0, 1],
            "var_result_summary" : gs_aux3[0, 2],
            "var_result_example" : gs_aux3[0, 3],
        }

def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.itervalues():
        core.hide_axis(ax)

    for k in [
          "dummy1",
          "dummy5",
          "dummy9"
       ]:
        axes[k].set_frame_on(False)

def plot_labels(axes):
    core.plot_labels(axes,
        labels_to_plot=[
            "dummy1",
            "spikes_before_teach",
            "weightpath_euc",
            "weightpath_nat",
            "learningcurve",
            "dummy9",
            "heatplot_homsyn",
            "heatplot_heterosyn",
            "heatplot_hom_het_comparison",
            "attenuation_summary_abs",
            "attenuation_example_abs",
            "var_result_summary",
            "var_result_example"
        ],
       label_ypos = {
             "dummy1":.8,
            "spikes_before_teach":.8,
            "weightpath_euc":.95,
            "weightpath_nat":.95,
            "learningcurve":.95,
            "dummy9":.9,
            "heatplot_homsyn":.95,
            "heatplot_heterosyn":0.95,
            "heatplot_hom_het_comparison":0.95,
            "attenuation_summary_abs":.95,
            "attenuation_example_abs":.95,
            "var_result_summary":.95,
            "var_result_example":.95
            } ,              
               
               
               
       label_xpos = {  "dummy1":-0.2,
            "spikes_before_teach":-0.2,
            "weightpath_euc":-0.2,
            "weightpath_nat":-0.2,
            "learningcurve":-0.2,
            "dummy9":-0.2,
            "heatplot_homsyn":-0.2,
            "heatplot_heterosyn":-0.2,
            "heatplot_hom_het_comparison":-0.2,
            "attenuation_summary_abs":-0.2,
            "attenuation_example_abs":-0.2,
            "var_result_summary":-0.2,
            "var_result_example":-0.2,
           }
        )

def get_fig_kwargs():
    return { "figsize" : (18./2.54,18./2.54) }



###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
#
def plot_dummy1(ax):
    pass

def plot_spikes_before_teach(ax):
    
    
    data_teach=core.get_data("fig3/2019-02-02_output_spikes_psth_teacher.npy")
    
    ax.scatter(np.nonzero(data_teach)[1],np.nonzero(data_teach)[0],color=core.label_to_color["teacher"],s=0.01)
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes_teach"])
    ax.set_ylabel(core.y_labels["spikes_teach"])


    pass


def plot_spikes_before(ax):
    
    data = core.get_data('fig3/2019-02-02_output_spikes_psth_start.npy')
    
    ax.scatter(np.nonzero(data)[1],np.nonzero(data)[0],color=core.label_to_color["natural"],s=0.01)
    
    core.show_axis(ax)
    core.make_spines(ax)
    
    ax.set_xlabel(core.x_labels["spikes"])
    ax.set_ylabel(core.y_labels["spikes"])

    pass



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



def plot_dummy5(ax):
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
    ax.legend(("Euclidean gradient","Natural gradient"),loc="upper_right",fontsize=8.,labelspacing=0.05,borderaxespad=0.,borderpad=0.,handlelength=0.2,frameon=False)
    



def plot_dummy9(ax):
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

def plot_attenuation_example_abs(ax):
    data_prox = core.get_data('fig6/attenuation_proximal_synapse.npy')
    data_dist = core.get_data('fig6/attenuation_distal_synapse.npy')
    time_params=core.get_data('fig6/time_parameters.npy').item()
    ax.set_prop_cycle(cycler('color',[core.label_to_color["attenuation_ldist"],core.label_to_color["attenuation_hdist"]] ))
    weighttrace=np.concatenate(((data_prox,),(data_dist,)))
    
    core.show_axis(ax)
    core.make_spines(ax)

    plotf.trace_plot(ax,weighttrace,time_params,perc=False,linewidth=core.linewidth["normal"])
    labelpad=-8.
    ax.set_xlabel(core.x_labels["trace_plot"])
    ax.set_ylabel(core.y_labels["trace_plot_dend_abs"],labelpad=labelpad)
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




