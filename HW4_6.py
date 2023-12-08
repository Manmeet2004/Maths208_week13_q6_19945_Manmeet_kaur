import numpy as np
from scipy.stats import  norm
import datetime
total__batteries= 150
defect_rate = 0.06  

mean= total__batteries * defect_rate
stdev = np.sqrt(total__batteries * defect_rate * (1 - defect_rate))

normal_prob = 1 - norm.cdf(11.5, mean, stdev)

print("Date:" , datetime.datetime.today())
print(f"Prob of 12 or more defective is,{normal_prob}")