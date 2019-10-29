#!/usr/bin/env python2
# encoding: utf-8

import matplotlib as mpl
import matplotlib.image as mpimg
from matplotlib import gridspec as gs
from matplotlib import collections as coll
import pylab as p
import copy
import numpy as np

import core
from core import log


def get_gridspec():
    """
        Return dict: plot -> gridspec
    """
    # TODO: Adjust positioning
    gs_main = gs.GridSpec(1, 1, hspace=0.65,
                          left=0.02, right=0.98, top=.9, bottom=0.1)
                
    gs_aux = gs.GridSpecFromSubplotSpec(1, 3, gs_main[0, 0], hspace=0.5,
                                           width_ratios=[1.,1., 3.0,])
    gs_aux1 = gs.GridSpecFromSubplotSpec(1, 2, gs_aux[0, 2], hspace=0.5,
                                           width_ratios=[1.,1.])
    gs_aux2 = gs.GridSpecFromSubplotSpec(2, 1, gs_aux1[0, 1], wspace=.5,
                                           height_ratios=[1.0, 1.0,]) 

    return {
            # these are needed for proper labelling
            # core.make_axes takes care of them

                        
            "plasticity_hom" : gs_aux[0, 0],
            
            "plasticity_het_u" : gs_aux[0, 1],
            
            "plasticity_het_p" : gs_aux1[0, 0],

            "proportional_plasticity_ss" : gs_aux2[0, 0],
            
            "proportional_plasticity_ws" : gs_aux2[1, 0]


            
        }

def adjust_axes(axes):
    """
        Settings for all plots.
    """
    # TODO: Uncomment & decide for each subplot!
    for ax in axes.itervalues():
        core.hide_axis(ax)

    for k in [
            "plasticity_hom",
            "plasticity_het_u",
            "plasticity_het_p",
            "proportional_plasticity_ss",
            "proportional_plasticity_ws"
        ]:
        axes[k].set_frame_on(False)

def plot_labels(axes):
    core.plot_labels(axes,
        labels_to_plot=[
            "plasticity_hom",
            "plasticity_het_u",
            "plasticity_het_p",
            
        ],
        label_ypos = {"plasticity_hom":.9,
            "plasticity_het_u":.9,
            "plasticity_het_p":.9,
            
                      },
        label_xpos = { "plasticity_hom":0.02,
            "plasticity_het_u":0.02,
            "plasticity_het_p":0.02,
            
                    }
        )

def get_fig_kwargs():
    return { "figsize" : (18.2/2.54, 8.63/2.54) }



###############################
# Plot functions for subplots #
###############################
#
# naming scheme: plot_<key>(ax)
#
# ax is the Axes to plot into
#
def plot_plasticity_hom(ax):
    
    pass

def plot_plasticity_het_u(ax):
    
    pass

def plot_plasticity_het_p(ax):
    
    pass


def plot_proportion_plasticity_ss(ax):
    
    pass
def plot_proportion_plasticity_ws(ax):
    
    pass


