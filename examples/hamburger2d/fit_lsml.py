import numpy as np

from level_set_machine_learning import LevelSetMachineLearning as LSML
from level_set_machine_learning.feature.dim2 import simple_feature_map
from level_set_machine_learning.initializer.provided import random_ball as rand_init

# Seed a random number generator.
rs = np.random.RandomState(1234)

# Set simple feature map function.
fmap = simple_feature_map.simple_feature_map(sigmas=[0, 3])

# Set the level set init routine.
ifnc = rand_init.RandomBallInitializer(random_state=rs)

# Initialize the model.
lsl = LSML(data_file="./dataset.h5", feature_map=fmap,
           init_func=ifnc, band=3.0, rs=rs)

# See documentation for complete list of fit options.
lsl.set_fit_options(maxiters=100, remove_tmp=True,
                    logfile="./log.txt", logstamp=False, logstdout=True)

# Finally, start the fitting process.
lsl.fit()

