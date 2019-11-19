from monty.serialization import loadfn
import os
import numpy as np

data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                        "data_files")
atomic_weights = loadfn(os.path.join(data_dir, "atomic_weights.json"))
atomic_numbers = loadfn(os.path.join(data_dir, "atomic_numbers.json"))
crystals = loadfn(os.path.join(data_dir, "crystals.json"))
