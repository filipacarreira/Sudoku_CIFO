from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

def performance_plot(names, legend, plot_name, subheading):

        df1 = pd.read_csv(
            names[0],
            names=[
                "gen",
                "Best_r",
                "Best fitness",
                "Worst_r",
                "Worst fitness",
                "Avg fitness",])
        df1["Legend"] = legend




    plt.figure(figsize=(13, 8))
    sns.lineplot(data=new, x="Generation", y="Best fitness", hue="Type", ci=95)
    plt.title(subheading, fontsize=23)
    plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
    plt.ylabel("Average Best Fitness", fontsize=15)
    plt.xlabel("Generation", fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)

    # Save plot
    plt.savefig(plot_name + ".png", dpi=300)

    plt.show()
