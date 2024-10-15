import tanglegram as tg
import matplotlib.pyplot as plt
import pandas as pd

#Replace your Taxa names and your distance matrices with the ones in labels and data. 

labelsA= ['TaxonA', 'TaxonB', 'TaxonC', 'TaxonD', 'TaxonE']  
data1 = [
      [0.0, 0.30000000000000004, 0.8, 1.5, 2.4000000000000004],
      [0.30000000000000004, 0.0, 0.9, 1.6, 2.5],
      [0.8, 0.9, 0.0, 1.5, 2.4000000000000004],
      [1.5, 1.6, 1.5, 0.0, 2.0999999999999996],
      [2.4000000000000004, 2.5, 2.4000000000000004, 2.0999999999999996, 0.0]
      ]
labelsB = ['TaxonA', 'TaxonB', 'TaxonC', 'TaxonD', 'TaxonE', 'TaxonF']
data2 = [
         [0.0, 0.30000000000000004, 0.8, 1.5, 3.4000000000000004, 3.5],
         [0.30000000000000004, 0.0, 0.9, 1.6, 3.5, 3.5999999999999996],
         [0.8, 0.9, 0.0, 1.5, 3.4000000000000004, 3.5],
         [1.5, 1.6, 1.5, 0.0, 3.0999999999999996, 3.1999999999999997],
         [3.4000000000000004, 3.5, 3.4000000000000004, 3.0999999999999996, 0.0, 1.7000000000000002],
         [3.5, 3.5999999999999996, 3.5, 3.1999999999999997, 1.7000000000000002, 0.0]
         ]
mat1 = pd.DataFrame(data1, columns=labelsA, index=labelsA)
mat2 = pd.DataFrame(data2, columns=labelsB, index=labelsB)
fig = tg.plot(mat1, mat2, sort=False)                       # "True" for minimizing the cross-overs
plt.show()
