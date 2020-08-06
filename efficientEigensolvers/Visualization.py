import matplotlib.pyplot as plt
import pandas as pd
import os
import sns
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
csv_name = '/Users/yuqingliu/PycharmProjects/ICERM_ORG/EE_with_applications/efficientEigensolvers/test_result_july17/mathworld_wolfram_com/200/PowerMethod_page_rank.csv'


df = pd.read_csv(csv_name, header = None ,quoting=2)
data = df.iloc[24:40,:]
data[1].astype('float')
ax = df_new.plot.bar(x=df_new[0], y=df_new[1], rot=0)
#plt.title("Distribution of Tip Bill Amounts ($)", y=1.015, fontsize=22);
#data[0].hist()
#plt.xlim([0,100])
#plt.ylim([50,500])
plt.title("Data")
plt.xlabel("fruits")
plt.ylabel("Frequency")
plt.show()
"""
data = pd.read_csv(csv_name, sep=',',header=None, index_col =0)

data.plot(kind='bar')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.title('Title')

plt.show()
"""