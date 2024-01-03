# pipeline.py

# import libraries
import sys
import pandas as pd

# set parameters
print(sys.argv)
day = sys.argv[1]

# transformation logic
print(pd.__version__)

# status
print(f'Success: pipeline sucessfully run for {day}')
