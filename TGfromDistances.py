import tanglegram as tg
import matplotlib.pyplot as plt
import pandas as pd

labelsA = ['TaxonA', 'TaxonB', 'TaxonC', 'TaxonD', 'TaxonE']  
data1 = [[0.0, 0.3, 0.8, 1.5, 2.4],
          [0.3, 0.0, 0.9, 1.6, 2.5],
          [0.8, 0.9, 0.0, 1.5, 2.4],
          [1.5, 1.6, 1.5, 0.0, 2.1],
          [2.4, 2.5, 2.4, 2.1, 0.0]]
labelsB = ['TaxonA', 'TaxonB', 'TaxonC', 'TaxonD', 'TaxonE', 'TaxonF']
data2 = [[0.0, 0.3, 0.8, 1.5, 3.4, 3.5],
          [0.3, 0.0, 0.9, 1.6, 3.5, 3.6],
          [0.8, 0.9, 0.0, 1.5, 3.4, 3.5],
          [1.5, 1.6, 1.5, 0.0, 3.1, 3.2],
          [3.4, 3.5, 3.4, 3.1, 0.0, 1.7],
          [3.5, 3.6, 3.5, 3.2, 1.7, 0.0]]
tg.plot(pd.DataFrame(data1, columns=labelsA, index=labelsA),
        pd.DataFrame(data2, columns=labelsB, index=labelsB), sort=False)   # "True" for minimizing the cross-overs
plt.show()
