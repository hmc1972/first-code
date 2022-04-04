from pstats import Stats
import numpy
from scipy import stats
# Data Types
# Three main categories:
# - Numerical
#   Numerical data are numbers, and ca be split into tow numerical categories:
#   - Discrete Data
#   - Continuous Data
# - Categorical
# - Ordinal

# Mean -  the average value
# Median - the mid point value
# Mode - the most common value

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Median - the mid point value
xmed = numpy.median(speed)
print(xmed)

xmode = stats.mode(speed)
print(xmode)
#
sort = numpy.sort(speed)
print(sort)