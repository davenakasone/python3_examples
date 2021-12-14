"""
colormap is a series of colors in a gradient that moves from start -> end
good to emphasize data

you can even save it, here it will just sit in the same directory
"""

import matplotlib.pyplot as plt

x_values = range (1, 1001) # 1 to 1000
y_values = [x**2 for x in x_values] # by list compression, list is filled

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10) 

ax.axis([0, 1_100, 0, 1_100_000]) # sets range for axis
ax.set_title('f(x) = x^2', fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)
#plt.show() # i think you have to cut this out to save graph
plt.savefig('squared_plot.png', bbox_inches = 'tight') # save with white space trimmed