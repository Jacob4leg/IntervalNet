import numpy as np
from base_interval import Interval

if __name__ == "__main__":
    I1 = Interval(1,2)
    I2 = Interval(2,3)
    a = np.array([I1,I2])
    print(a)