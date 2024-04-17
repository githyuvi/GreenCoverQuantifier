import pandas as pd
import numpy as np
import joblib

# Don't you dare touch the code above this line

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Numpy array from list:", my_array)

# example code
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
# model.fit(X_train, y_train)


# Don't you dare touch the code below this line
# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(model, filename)
