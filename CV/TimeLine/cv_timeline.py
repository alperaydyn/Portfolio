# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import seaborn as sns
import pandas as pd
from numpy import linspace

d = [
     ['Weka, SAS, R',2014, 2014],
     ['Weka, SAS, R',2011, 2012],
     ['Weka, SAS, R',2015, 2015],
     ['Weka, SAS, R',2018, 2018],
     ['Neural Networks',2016, 2019],
     ['Machine Learning',2015, 2023],
     ['JQuery',2015, 2023],
     ['Data Mining',2012, 2023],
     ['SQL',2010, 2023],
     ['NLP, NLU',2018, 2019],
     ['NLP, NLU',2020, 2023],
     ['RL, AI',2018, 2018],
     ['RL, AI',2019, 2023],
     ['ASP, ASP.Net, Flask',2008, 2010],
     ['ASP, ASP.Net, Flask',2011, 2017],
     ['ASP, ASP.Net, Flask',2018, 2023],
     ['VB, C#, Python',2010, 2016],
     ['VB, C#, Python',2017, 2022],
     ['VB, C#, Python',2002, 2009],
    ]

dx = ([(s[0],y,i) for i,s in enumerate(d) for y in range(s[1], s[2]+1) if y<=2022 ])
df=pd.DataFrame(dx, columns=['year','skill','i'])


c = [
     ['Certificates',2014, 2014],
     ['Certificates',2015, 2015],
     ['Certificates',2015.2, 2015.2],
     ['Certificates',2016, 2016],
     ['Certificates',2018, 2018],
     ['Certificates',2018.2, 2018.2],
     ['Certificates',2020, 2020],
     ['Certificates',2021, 2021],
     ['Certificates',2021.9, 2021.9],
    ]
cf=pd.DataFrame(c, columns=['year','skill','i'])



#print(plt.style.available)
plt.style.use('tableau-colorblind10')

#colors:
colors = [ cm.jet(x) for x in linspace(0.10, 0.40, 20) ]

# plot
fig, ax = plt.subplots(figsize=(12,5)) # [10,3,29], [12,4,36], [15-5-44]

cfi = cf['i'].value_counts().sort_index()
for i,f in cfi.items():
    bars = ax.plot( 'skill', 'year', data=cf[cf['i']==i], linestyle='', 
                   marker='*', markeredgewidth=1, markersize=20, alpha=0.8)
dfi = df['i'].value_counts().sort_index()
for i,f in dfi.items():
    bars = ax.plot( 'skill', 'year', data=df[df['i']==i], linestyle='', 
                   marker='_', markeredgewidth=15, markersize=33, alpha=1)


ax.set_xticks(np.unique(df.skill))
ax.set_facecolor('w')
ax.xaxis.grid(color='white', alpha=0.0, linestyle='-', linewidth=0.5)
ax.yaxis.grid(color='gray', alpha=0.5, linestyle='-', linewidth=0.5)
ax.xaxis.set_label_position('top') 
ax.xaxis.tick_top()
ax.axvline(x=2022, linewidth=2, color='green', linestyle='dashed', alpha=0.5)
plt.box(on=None)

plt.savefig('exp_2022.png', format='png', dpi=200)
plt.show()
