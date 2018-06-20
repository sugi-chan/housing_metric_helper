

import pandas as pd
import numpy as np

dat = pd.read_csv('C:/Users/micha/Downloads/rent1.csv')

dat['util_score'] = dat.water + dat.gas +dat.sewer +dat.trash +dat.electrcit1
dat['kitchen'] = dat.stove + dat.refrigerator +dat.dishwasher

#calculate standard deviations from mean
price_mean = dat.price.mean()
std_price = dat.price.describe()[2]

dat['price_std_deviation'] = (dat.price - price_mean) /std_price



### sqfoot deviation
sqft_mean = dat.sqft.mean()
std_sqft = dat.sqft.describe()[2]

dat['sqft_std_deviation'] = (dat.sqft - sqft_mean) /std_sqft


### composite scores?

### sqfoot deviation
util_mean = dat.util_score.mean()
util_std = dat.util_score.describe()[2]



### sqfoot deviation
kitchen_mean = dat.kitchen.mean()
kitchen_std = dat.kitchen.describe()[2]

kitchen_weight = 1
util_weight = 1
price_weight = 1.5
sqft_weight = 1.25



dat['composite'] = ( kitchen_weight*((dat.kitchen - kitchen_mean) /kitchen_std) +
                     util_weight*( (dat.util_score - util_mean) /util_std) +
                     sqft_weight *dat.sqft_std_deviation +
                     price_weight*-1*dat.price_std_deviation ) /4

dat.to_csv('C:/Users/micha/Downloads/rent1.csv')

