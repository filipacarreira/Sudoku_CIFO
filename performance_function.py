from matplotlib import pyplot as plt
import pandas as pd

files = ['performance/test3.csv', 'performance/test2.csv']
legends = ['legenda', 'lengenda2']

def df(file):
    df1 = pd.read_csv(file, usecols=["bestfitness", "mean_allfitness", "time", "gen"])
    df1 = df1.iloc[:-1, :]
    return df1

plt.figure(figsize=(10, 6))
plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
plt.ylabel("Average Best Fitness", fontsize=15)
plt.xlabel("Generation", fontsize=15)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

for i in range(len(files)):
    dataframe = df(files[i])
    plt.plot(dataframe["gen"], dataframe["mean_allfitness"])

# Set legend
plt.legend(legends)
# Save plot
plt.savefig('hello' + ".png", dpi=300)
plt.show()




