import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class RF_feature_selection:
    """Random Forest feature selection by importance score"""
    def __init__(self):
        self.model = RandomForestClassifier(random_state = 0)
        