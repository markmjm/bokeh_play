from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np
import pandas as pd

# Making basic Bokeh graph
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# prepare the output file
output_file('line.html')

# create figure
f=figure()
print(dir(f))
# create line plot
f.line(x,y)

# write the plot in the figure objecy
show(f)