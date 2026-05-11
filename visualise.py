import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns

def visualise(df1, save_path):
    counts=df1["compound"].value_counts()
    labels=counts.index.tolist()
    sizes= counts.values
    sns.set_style("whitegrid")
    colors=sns.color_palette("pastel", n_colors=3)

    #set up a figure with two subplots
    fig, (ax1, ax2)= plt.subplots(1, 2, figsize=(10, 5))
        
    
    #bar plot on axis 1
    counts.plot(kind="bar", color=colors, ax=ax1)
    ax1.set_title("Sentiment Distribution graph", fontsize=18, fontweight="bold", color="black")
    ax1.set_xlabel("Sentiment scores", fontsize=10)
    ax1.set_ylabel("Frequency", fontsize=10)

    #pie plot on axis 2
    ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True)
    ax2.set_title("Sentimennt Distribution (Pie)", fontsize=18, fontweight="bold", color="black")

    plt.tight_layout()
    
    plt.savefig(save_path)
    plt.close(fig)
    
    
'''
# USE OF WEBSITES TO MAKE BAR CHART MORE ATTRACTIVE
Using sns.set_style("whitegrid") and sns.color_palette("pastel")

https://seaborn.pydata.org/tutorial/aesthetics.html
https://seaborn.pydata.org/tutorial/color_palettes.html
''' 

"""USE OF COMET AI TO SHOW PERCENTAGE VALUES IN PIE CHART
If your plot does not show the percentages:

Make sure you include autopct="%1.1f%%" exactly as shown  in the ax2.pie() function. """