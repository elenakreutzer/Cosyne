#!/usr/bin/env python2
# encoding: utf-8

"""
    Core utils for all figures.
"""

import itertools as it
import numpy as np
import os
import os.path as osp
import pylab as p
p.style.use(['matplotlibrc'])
import string

np.random.seed(424242)

folders = {}
folders["root"] = osp.join(osp.dirname(osp.abspath(__file__)), "..")


folders["fig"] = osp.join(folders["root"], "fig")
# Create the fig folder as a child of the root folder if it does not exist, 
if not osp.exists(folders["fig"]):
	os.makedirs(folders["fig"])

folders["data"] = osp.join(folders["root"], "data")

def make_log(name):
    import logging
    import os
    log = logging.Logger(name)
    if "DEBUG" in os.environ:
        log_level = logging.DEBUG
        log_formatter = logging.Formatter("%(asctime)s %(levelname)s: "
            "%(message)s", datefmt="%y-%m-%d %H:%M:%S")
    else:
        log_level = logging.INFO
        log_formatter = logging.Formatter("%(asctime)s %(levelname)s: "
            "%(message)s", datefmt="%y-%m-%d %H:%M:%S")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(log_formatter)
    log.addHandler(log_handler)
    log.setLevel(log_level)
    return log
log = make_log("paper-natural_gradient")

# in order to have consistent coloring, please have all colors be defined here

label_to_color = {
    # preliminary:
    # global
    "aux_lines":"black",
    
    #figure3
    "euclidean":"darkblue",
    "natural":"indianred",
    "teacher":"darkorange",

    # figure 5
    "attenuation_ldist":"indianred",
    "attenuation_hdist":"darkmagenta",
    "attenuation_im":"black",
    "hr_ht":"seagreen",
    "lr_ht":"darkorange",
    "hr_lt":"darkblue",
    # figure6
    "stim":"darkorange",
    "unstim":"indianred",
    "aux_line_heat":"white",
    
    #figureS1
    "approx":"orange",
    "coefficients":"darkblue",
    "nonlinearity":"seagreen",
    
}

layer_to_color = {
    "hidden" : "orange",
    "label" : "blue",
    "bad" : "red",
}
layer_alpha = 0.75

dataset_to_color = {
    "train" : "g",
    "test" : "b",
    "train_theo" : "darkgreen",
    "test_theo" : "#062A78",
    #  "hw_mean" : "deepskyblue", 
    #  "hw_span" : "aqua",
    "hw_mean" :  "#A67B5B",
    "hw_span" : "wheat",
}

#linewidths/labelpads
linewidth={
        "normal":2.,
        "aux_lines":1.,
        "scatter":15.,
        "labelsize":10.,
        "ticksize":8.,
        "lp_heat":0.,
        "arrow":0.0033,
        "contour":1.,
        "spikes":.5,
        "voltage":1.,
        "cb":8.,
        }

#labels
x_labels={
        #figure 3
        "isi":r"$\Delta t$ [s]",
        
        "voltage_trace":'t [s]',
        "spikes":'t [s]',
        "histo":'t [s]',
        "spikes_teach":'t [s]',
        "weight_path": r'$w_1$ [a.u.]',
        "lc":'t [min]',
        
        #figure 5
        "trace_plot":'t [s]',
        "usp_trace":"t [s]",
        "hist":r'$\mathrm{log p}(x^{\epsilon})$',
        
        #figure 6
        "heat_plot":r'$w_{\mathrm{ust}}(t_0)$ [a.u.]',
        
        #figure S1
        "g0":r"$\mu_{\rm v}$",
        "g1":"approximation",
        "g2":"approximation",
        
        #figure S2
        "angles_approx":"Fisher angle approx/ng [deg]",
        "angles_euc":"Fisher angle eg/ng [deg]",
        "norm_approx":"Fisher norm ratio approx/ng",
        "norm_euc":"Fisher norm ratio eg/ng"
        
        }

y_labels={
        #figure 3
        "isi":r"$p(\Delta t)$",
        "spikes":'# trial',
        "histo":'p',
        "spikes_teach":'# trial',
        'voltage_trace':'V [mV]',
        "weight_path": r'$w_2$ [a.u.]',
        "lc":r'$DKL(p*\|p_{\bf w})$',
        
        
        #figure 5
        "trace_plot":'w [%]',
        "trace_plot_dend":'$w^d$ [%]',
        "trace_plot_dend_abs":'$w^d$ [a.u.]',
        "usp_trace":r'$x^{\epsilon}$ [mV]',
        "weightchange":r'$\Delta$ w [%]',
        "weightchange_dend":r'$\Delta w^d$ [%]',
        "weightchange_dend_abs":r'$\Delta w^d$ [a.u.]',
        
        #figure 6
        "heat_plot":r'$w_{\mathrm{st}}(t_0)$ [a.u.]',
        
        #figure S1
        "g0":r"$\gamma_{\rm s}$",
        "g0_nl":"Output rate [Hz]",
        "g1":r"$\gamma_{\rm u}$",
        "g2":r"$\gamma_{\rm w}$",
        
        
        }
def make_figure(name):
    log.info("--- Creating figure: {} ---".format(name))

    plotscript = get_plotscript(name)

    class FigureNotDone(Exception):
        pass

    def throw_figure_not_done():
        raise FigureNotDone

    try:
        gs = getattr(plotscript, "get_gridspec",
                lambda: throw_figure_not_done())()
    except FigureNotDone:
        log.error("Work on {} hasn't even started yet, sheesh!".format(name))
        return

    fig_kwargs = getattr(plotscript, "get_fig_kwargs", lambda: {})()

    fig, axes = make_axes(gs, fig_kwargs=fig_kwargs)

    # call possible axes adjustment script for figure
    getattr(plotscript, "adjust_axes", lambda axes: None)(axes)

    for k, ax in axes.iteritems():
        log.info("Plotting subfigure: {}".format(k))
        getattr(plotscript, "plot_{}".format(k), lambda ax: log.warn(
            "Plotscript missing for subplot <{}> in figure <{}>!"
            "".format(k, name)))(ax)

    log.info("Plotting labels…")
    getattr(plotscript, "plot_labels", lambda axes: log.warn(
        "Not plotting labels for figure {}".format(name)))(axes)

    save_figure(fig, name)
    p.close(fig)

def get_plotscript(name):
    print(name)
    try:
        exec("import {} as plotscript".format(name))
    except ImportError:
        log.error("Plotscript for figure {} not found!".format(name))
        raise
    return plotscript

def save_figure(fig, name):
    print(osp.join(folders["fig"], name))
    fig.savefig(osp.join(folders["fig"], name))


def make_axes(gridspec, fig_kwargs=None):
    """
        Turn gridspec information into plots.
    """
    if fig_kwargs is None:
        fig_kwargs = {}

    fig = p.figure(**fig_kwargs)
    axes = {}

    for k, gs in gridspec.iteritems():
        # we just add a label to make sure all axes are actually created
        log.debug("Creating subplot: {}".format(k))
        axes[k] = fig.add_subplot(gs, label=k)

    return fig, axes


def get_data(filename):
    return np.load(osp.join(folders["data"], filename))

def plot_labels(axes, labels_to_plot, xpos_default=.04, ypos_default=.90,
        label_xpos={}, label_ypos={}, label_color={}, fontdict={}):

    for l, c in zip((l for l in labels_to_plot),
            string.ascii_uppercase):
        log.info("Subplot {0} receives label {1}".format( l, c ))
        c = c
        plot_caption(axes[l], c,
                label_xpos.get(l, xpos_default),
                label_ypos.get(l, ypos_default), label_color.get(l, "k"),
                fontdict=fontdict)

def plot_caption(ax, caption, xpos=.04, ypos=.88, color="k", fontdict={}):
    # find out how our caption will look in reality
    caption_args={
            "ha" : "left", "va" : "bottom",
            #"weight" : "bold",
            "style" : "normal",
            "size" : 12,
            "color": color,
            "zorder" : 1000,
        }
    # r = get_renderer(ax.figure)
    # bb = t.get_window_extent(renderer=r)

    # if fontdict is None:
        # fontdict = {"family": "Linux Biolinum Kb"}
        # size = caption_args["size"]
        # bbox = mpatches.FancyBboxPatch(ax.transAxes.transform((xpos, ypos)),
                # size *1.0, size*1.0, zorder=10,
                # edgecolor="k", facecolor="r", boxstyle="round")
        # ax.patches.append(bbox)

    t = ax.text(xpos, ypos, caption, fontdict=fontdict, transform=ax.transAxes,
            **caption_args )

def hide_axis(ax):
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

def show_axis(ax):
    ax.get_xaxis().set_visible(True)
    ax.get_yaxis().set_visible(True)

def hide_ticks(ax, axis=u'both', minormajor=u'both'):
    ax.tick_params(axis=axis, which=minormajor,length=0)

def make_spines(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def make_arrow(ax, pos_from, pos_to, color="r", arrowstyle="<|-|>",
        shrinkA=0., shrinkB=0., transform="data"):
    ax.annotate("", xy=pos_to, xytext=pos_from,
            xycoords=transform, textcoords=transform,
            arrowprops=dict(arrowstyle=arrowstyle, color=color,
                shrinkA=shrinkA, shrinkB=shrinkB))

def make_arrow_lines(ax, xpos, xlength, ypos, color="r", arrowstyle="<|-|>",
        line_alpha=0.75, text_ypos_adjustment=0., text_va="center", text=""):

    make_arrow(ax, (xpos, ypos), (xpos+xlength, ypos), color=color, arrowstyle=arrowstyle)

    ax.text(xpos+xlength/2., ypos - text_ypos_adjustment, text,
            va=text_va, color="r", ha="center")

    ax.axvline(x=xpos, ls="-", alpha=line_alpha, color=color)
    ax.axvline(x=xpos+xlength, ls="-", alpha=line_alpha, color=color)