import pandas as pd

One_Feature = pd.Series()
One_Feature = pd.Series(
    index=['DSTPORT1', 'DSTPORT2', 'DSTPORT3', 'DSTPORT4', 'DSTPORT5', 'DSTPORT6', 'DSTPORT7', 'DSTPORT8', 'SRCPORT1',
           'SRCPORT1', 'SRCPORT1', 'SRCPORT2', 'SRCPORT3', 'SRCPORT4', 'SRCPORT5', 'SRCPORT6', 'SRCPORT17', 'SRCPORT8',
           'SRCIP1', 'SRCIP1', 'SRCIP1', 'SRCIP1', 'SRCIP2', 'SRCIP3', 'SRCIP4', 'SRCIP5', 'SRCIP6', 'SRCIP7', 'SRCIP8',
           'DSTIP1', 'DSTIP2', 'DSTIP3', 'DSTIP4', 'DSTIP5', 'DSTIP6', 'DSTIP7', 'DSTIP8'])
# One_Feature.set_value(0,1)
# One_Feature.loc[2]=1
print(One_Feature.describe())
