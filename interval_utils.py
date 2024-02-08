from typing import Tuple
import torch
import numpy as np
from base_interval import Interval


def interval_arr_from_tensor(A_l : torch.Tensor,A_u : torch.Tensor) -> np.array:
    '''
    Converts two tensors into numpy array of intervals
    '''
    assert A_l.shape == A_u.shape, "the shapes of lower and upper matrix should be equal"
    
    N,M = A_l.shape
    intervals = [[Interval(A_l[i,j], A_u[i,j]) for j in range(M)] for i in range(N)]
    return np.array(intervals)

def tensors_from_interval_arr(A : np.array) -> Tuple[torch.Tensor, torch.Tensor]:
    '''
    Converts numpy array of intervals into two tensors
    '''
    N,M = A.shape
    A_l = [[A[i,j].l for j in range(M)] for i in range(N)]
    A_u = [[A[i,j].u for j in range(M)] for i in range(N)]
    return torch.Tensor(A_l), torch.Tensor(A_u)