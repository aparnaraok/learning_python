import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-np.pi, np.pi, 256) #256 refers to no of points...more the no of points beter the curve
#-3.14 to + 3.14
Y1 = np.sin(X)
#Y1 = np.sqrt(1 - X*X)
Y2 = np.cos(X)
#try with sinh cosh tanh cos and tan....

plt.figure(figsize=(6,4), dpi=100) #dpi means dots per inch(resolution)(6,4) is specified by dpi
#if dpi is 10..clarity will be less (6,4) width(x axis) and height(y axis)
#largeness of the picture is decided by dpi.
#fignize is not absolute...

#plt.plot(X, Y1)
#plt.plot(X, Y1, color = "blue", linewidth=1, linestyle='--') #linewidth rep thickness
plt.plot(X, Y1, color = "blue", linewidth=2.5, linestyle='-.', label='sin') #linewidth rep thickness
#plt.plot(X, Y2)
plt.plot(X, Y2, color = "red", linewidth=2.5, linestyle=':', label='cos')

#-----------------margin alteration-----------------

#plt.xlim(X.min() * 1.5) #Squeeze/increase the left margin/border
#plt.xlim(X.max() * 0.5) #Squeeze/increase the right margin/border

#plt.ylim(Y1.min() * 1.5) #Squeeze/increase the bottom margin/border
#plt.ylim(Y1.max() * 0.5) #Squeeze/increase the top margin/border

#--------------------------------------------------------

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'], rotation=30) #Changes the exact values to xaxis -3.14 to +3.14)


#---------------------------------Spines-------------------
ax = plt.gca() #Gets the current axis(creates one if needed)
ax.spines['right'].set_color(None) #right line vanishes
ax.spines['top'].set_color(None) #top line vanishes
#ax.xaxis.set_ticks_position('top') #Moves the xticks to top
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0)) #intersects at (0,0)

#plt.legend(loc='upper right')
plt.legend(loc='best') #Chooses the best white space and displays.

#------------------Highlight the xtick and ytick values-----------
#alpha --->transparency...more small it is..more clarity

for labels in ax.get_xticklabels() + ax.get_yticklabels():
    labels.set_fontsize(16)
    labels.set_bbox(dict(facecolor='green',
                         edgecolor='yellow',
                         alpha=0.35))



#--------------------------Show----------------------------
plt.show() #All config need to be done before plt.show()



#-------------------------------Output-------------
# best
# 	upper right
# 	upper left
# 	lower left
# 	lower right
# 	right
# 	center left
# 	center right
# 	lower center
# 	upper center
# 	center
#
#   % (loc, '\n\t'.join(self.codes)))
