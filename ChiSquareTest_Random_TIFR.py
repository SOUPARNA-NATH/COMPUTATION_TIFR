import numpy as np
import scipy.stats as st

obs_1 = np.array([4,10,10,13,20,18,18,11,13,14,13])
obs_2 = np.array([3,7,11,15,19,24,21,17,13,9,5])

expectation = np.array([1,2,3,4,5,6,5,4,3,2,1])

var_1 = sum((obs_1 - expectation)**2/obs_1)
var_2 = sum((obs_2 - expectation)**2/obs_2)

test_1 = (1.0 - st.chi2.cdf(var_1,10.0))*100
test_2 = (1.0 - st.chi2.cdf(var_2,10.0))*100

print("First Test:-\n")

if (test_1 < 1.0 or test_1 > 99.0):
    print("Not Sufficiently Random")
elif (1.0 < test_1 < 5.0 or 95.0 < test_1 < 99.0):
    print("Suspect")
elif(5.0 < test_1 < 10.0 or 90.0 < test_1 < 95.0):
    print("Almost Suspect")
else:
    print("Sufficiently Random")

print("\nSecond Test:-\n")

if (test_2 < 1.0 or test_2 > 99.0):
    print("Not Sufficiently Random")
elif (1.0 < test_2 < 5.0 or 95.0 < test_2 < 99.0):
    print("Suspect")
elif(5.0 < test_2 < 10.0 or 90.0 < test_2 < 95.0):
    print("Almost Suspect")
else:
    print("Sufficiently Random")

