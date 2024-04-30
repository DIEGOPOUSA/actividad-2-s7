# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:43:19 2024

@author: dpous
"""

import numpy as np


matriz = np.zeros((3, 3))


np.fill_diagonal(matriz, [1, 2, 3])


print(matriz)