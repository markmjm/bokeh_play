from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np
import pandas as pd

# Making basic Bokeh graph
x = [3,7.5,10]
y = [3,6,9]

# prepare the output file
output_file('triangle.html')

# create figure
f=figure()
print(dir(f))
# create line plot
f.triangle(x,y,size=5, color='blue', alpha=0.5)

# write the plot in the figure objecy
show(f)

# create line plot
f.circle(x,y,size=5, color='blue', alpha=0.5)

# write the plot in the figure objecy
show(f)