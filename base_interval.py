import torch
import numpy as np

class Interval:
    def __init__(self, l, u) -> None:
        """
        Basic interval implementation, mainly for testing with numpy. Useless with torch.
        Interval has a form [l,u] where l <= u.
        """
        assert l <= u, f"Wrong definition of interval {l} is not <= than {u}"
        self.l = l
        self.u = u
    
    def __add__(self, other):
        """
        Addition of two intervals
        [a,b] + [c,d] = [a+b, c+d]
        """
        return Interval(self.l + other.l, self.u + other.u)

    def __sub__(self, other):
        """
        Subtraction of two intervals
        [a,b] - [c,d] = [a-d, b-c]
        """
        return Interval(self.l - other.u, self.u - other.l)
    
    def __mul__(self, other):
        """
        Multiplication of two intervals
        [a,b] * [c,d] = [min{ac,ad,bc,bd},max{ac,ad,bc,bd}]
        """
        vals = [self.l * other.l, self.l * other.u, self.u * other.l, self.u * other.u]
        lower, upper = min(vals), max(vals)
        return Interval(lower, upper)
    
    def __truediv__(self, other):
        """
        Division of two intervals. If the second interval contains 0, then division if undefined
        [a,b] / [c,d] = [a,b] * [1/d, 1/c]
        """
        assert not (other.l == 0 or other.u == 0), f"Undefined division for {self} and {other}"
        assert not (other.l * other.u < 0), f"Undefined division for {self} and {other}"
        return self * Interval(1 / other.u, 1 / other.l)

    def __repr__(self) -> str:
        return f"[{self.l},{self.u}]"
