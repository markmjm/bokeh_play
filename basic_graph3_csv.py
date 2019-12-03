#
# https://docs.bokeh.org/en/latest/
# https://docs.bokeh.org/en/latest/docs/reference.html
#

from bokeh.io import output_file, show, save
from bokeh.plotting import figure
import numpy as np
import pandas as pd

# Making basic Bokeh graph
df = pd.read_csv('bachelors.csv')
x = df['Year']
y= df['Engineering']
# prepare the output file
output_file('triangle.html')

# create figure
f=figure()
print(dir(f))
# create line plot
f.line(x,y)

# write the plot in the figure objecy
# show has a bug as it append canges (full data set) over and over and over in the html file.
# use save when you only want to save
show(f)
# save(f)

