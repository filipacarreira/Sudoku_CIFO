from matplotlib import pyplot as plt
import pandas as pd

files = ['performance/test6.csv', 'performance/test8.csv']
legends = ['legenda', 'lengenda2']

def df(file):

    column_names = ['gen', 'bestfitness', 'mean_allfitness', 'time']
    df1 = pd.read_csv(file, names=column_names, usecols=[1, 2, 3, 4])
    print(df1)
    df1 = df1.dropna(how='all')
    df1 = df1.groupby(['gen']).mean()
    df1['gen'] = df1.index

    return df1

plt.figure(figsize=(10, 6))
plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
plt.ylabel("Average Best Fitness", fontsize=15)
plt.xlabel("Generation", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

for file in files:

    dataframe = df(file)
    plt.plot(dataframe["gen"], dataframe["bestfitness"])

# Set legend
plt.legend(legends)
# Save plot
plt.savefig('hello' + ".png", dpi=300)
plt.show()




