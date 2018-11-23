import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid', context='notebook')
cols = ['RM', 'TAX', 'PTRATIO', 'LSTAT', 'MEDV']
sns.pairplot(df[cols
             ])