from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

names=['test.csv', 'hello', 'plotname']
def performance_plot(names, legend, plot_name):

        df1 = pd.read_csv(
            names[0],
            names=[
                "bestfitness",
                "mean_allfitness",
                "time",
                "gen"])

        df1["Legend"] = legend


        plt.figure(figsize=(13, 8))
        sns.lineplot(data=df1, x="gen", y="best_allfitness", hue="Legend", ci=95)
        plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
        plt.ylabel("Average Best Fitness", fontsize=15)
        plt.xlabel("Generation", fontsize=15)
        plt.xticks(fontsize=13)
        plt.yticks(fontsize=13)

        # Save plot
        plt.savefig(plot_name + ".png", dpi=300)

        plt.show()
