#!/usr/bin/env python
# coding: utf-8

# # Plotting with Matplotlib

# ## Importing Matplotlib

# We import the 'pyplot' object from Matplotlib, which provides us with an interface for making figures. We usually abbreviate it.

# In[1]:


from matplotlib import pyplot as plt


# ## Notebook magics

# When we write:

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# We tell the Jupyter notebook to show figures we generate alongside the code that created it, rather than in a
# separate window. Lines beginning with a single percent are not python code: they control how the notebook deals with python code.

# Lines beginning with two percent signs are "cell magics", that tell Jupyter notebook how to interpret the particular cell;
# we've seen `%%writefile` and `%%bash` for example.

# ## A basic plot

# When we write:

# In[3]:


from math import sin, cos, pi

myfig = plt.plot([sin(pi * x / 100.0) for x in range(100)])


# The plot command *returns* a figure, just like the return value of any function. The notebook then displays this.

# To add a title, axis labels etc, we need to get that figure object, and manipulate it. 
# For convenience, matplotlib allows us to do this just by issuing commands to change the "current figure":

# In[4]:


plt.plot([sin(pi * x / 100.0) for x in range(100)])
plt.title("Hello")


# But this requires us to keep all our commands together in a single cell, and makes use of a "global" single "current plot",
# which, while convenient for quick exploratory sketches, is a bit cumbersome. To produce from our notebook proper plots
# to use in papers, Python's plotting library, matplotlib, defines some types we can use to treat individual figures as variables,
# and manipulate these.

# ## Figures and Axes

# We often want multiple graphs in a single figure (e.g. for figures which display a matrix of graphs of different variables for comparison).

# So Matplotlib divides a `figure` object up into axes: each pair of axes is one 'subplot'. 
# To make a boring figure with just one pair of axes, however, we can just ask for a default new figure, with
# brand new axes. The relevant function returns a (figure, axis) pair, which we can deal out with parallel assignment. 

# In[5]:


sine_graph, sine_graph_axes = plt.subplots()


# Once we have some axes, we can plot a graph on them:

# In[6]:


sine_graph_axes.plot([sin(pi * x / 100.0) for x in range(100)], label="sin(x)")


# We can add a title to a pair of axes:

# In[7]:


sine_graph_axes.set_title("My graph")


# In[8]:


sine_graph_axes.set_ylabel("f(x)")


# In[9]:


sine_graph_axes.set_xlabel("100 x")


# Now we need to actually display the figure. As always with the notebook, if we make a variable be returned by the last
# line of a code cell, it gets displayed:

# In[10]:


sine_graph


# We can add another curve:

# In[11]:


sine_graph_axes.plot([cos(pi * x / 100.0) for x in range(100)], label="cos(x)")


# In[12]:


sine_graph


# A legend will help us distinguish the curves:

# In[13]:


sine_graph_axes.legend()


# In[14]:


sine_graph


# ## Saving figures

# We must be able to save figures to disk, in order to use them in papers. This is really easy:

# In[15]:


sine_graph.savefig("my_graph.png")


# In order to be able to check that it worked, we need to know how to display an arbitrary image in the notebook.

# The programmatic way is like this:

# In[16]:


from IPython.display import (
    Image,
)  # Get the notebook's own library for manipulating itself.

Image(filename="my_graph.png")


# ## Subplots

# We might have wanted the $\sin$ and $\cos$ graphs on separate axes:

# In[17]:


double_graph = plt.figure()


# In[18]:


sin_axes = double_graph.add_subplot(2, 1, 1)  # 2 rows, 1 column, 1st subplot


# In[19]:


cos_axes = double_graph.add_subplot(2, 1, 2)


# In[20]:


double_graph


# In[21]:


sin_axes.plot([sin(pi * x / 100.0) for x in range(100)])


# In[22]:


sin_axes.set_ylabel("sin(x)")


# In[23]:


cos_axes.plot([cos(pi * x / 100.0) for x in range(100)])


# In[24]:


cos_axes.set_ylabel("cos(x)")


# In[25]:


cos_axes.set_xlabel("100 x")


# In[26]:


double_graph


# ## Versus plots

# When we specify a single `list` to `plot`, the x-values are just the array index number. We usually want to plot something
# more meaningful:

# In[27]:


double_graph = plt.figure()
sin_axes = double_graph.add_subplot(2, 1, 1)
cos_axes = double_graph.add_subplot(2, 1, 2)
cos_axes.set_ylabel("cos(x)")
sin_axes.set_ylabel("sin(x)")
cos_axes.set_xlabel("x")


# In[28]:


sin_axes.plot(
    [x / 100.0 for x in range(100)], [sin(pi * x / 100.0) for x in range(100)]
)
cos_axes.plot(
    [x / 100.0 for x in range(100)], [cos(pi * x / 100.0) for x in range(100)]
)


# In[29]:


double_graph


# ## Learning More

# There's so much more to learn about `matplotlib`: pie charts, bar charts, heat maps, 3-d plotting, animated plots, and so on. You can learn all this via the [Matplotlib Website](http://matplotlib.org/#).
# You should try to get comfortable with all this, so please use some time in class, or at home, to work your way through a bunch of the [examples](http://matplotlib.org/examples/index.html).