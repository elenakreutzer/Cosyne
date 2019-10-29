#########################################################################
#import modules
#########################################################################
import numpy as np
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


class MidpointNormalize(Normalize):
	def __init__(self,vmin=None,vmax=None,midpoint=None,clip=True):
		self.midpoint=midpoint
		Normalize.__init__(self,vmin,vmax,clip)
	def __call__(self,value,clip=True):
		x,y=[self.vmin,self.midpoint,self.vmax],[0.,0.5,1.]
		return(np.ma.masked_array(np.interp(value,x,y)))


w_change_hom,w_change_het=np.zeros((2,200,200))
for i in range(200):
	startweight=np.load("hom"+str(i+1)+".npy")
	w_change_hom[i,:]=np.load("foo_hom"+str(i+1)+".npy")
	w_change_het[i,:]=np.load("foo_het"+str(i+1)+".npy")
sign_change=np.multiply(np.sign(w_change_hom),np.sign(w_change_het))
fig=plt.figure()
norm=MidpointNormalize(midpoint=0)
plt.imshow(w_change_hom,norm=norm,cmap="RdBu",origin="lower",interpolation="nearest")
plt.colorbar()
fig.savefig("heatplot_hom.svg")

fig2=plt.figure()
norm=MidpointNormalize(midpoint=0)
plt.imshow(w_change_het,norm=norm,cmap="RdBu",origin="lower",interpolation="nearest")
plt.colorbar()
fig2.savefig("heatplot_het.svg")

fig3=plt.figure()
norm=MidpointNormalize(midpoint=0)
plt.imshow(sign_change,norm=norm,cmap="RdBu",origin="lower",interpolation="nearest")
plt.colorbar()
fig3.savefig("heatplot_sign.svg")
