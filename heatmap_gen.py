import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# The csv file name to open (excluding the .csv extention)
# EDIT THIS ACCORDIG TO TARGET FILE NAME
FILE_NAME = 'Book1'

# The size of the final heatmap (will be square, so FIGUE_SIZE)
FIGURE_SIZE = 40

try:
    # Load the correlation matrix csv file
    df = pd.read_csv(f"./CSV_Files/{FILE_NAME}.csv", index_col=0)
    
except FileNotFoundError as e:
    print(f"Error: The file '{FILE_NAME}.csv' was not found.\n{e}\n")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    # Set up the figure size
    plt.figure(figsize=(FIGURE_SIZE, FIGURE_SIZE))

    # Calculate font size based on the number of cells in the heatmap
    cell_height = FIGURE_SIZE / len(df.index)  # Height of each cell in inches
    font_size = cell_height * 0.1 * 72  # Convert to points (1 inch = 72 points)

    # Create a heatmap with the desired customizations
    heatmap = sns.heatmap(df,
                annot=True,
                fmt='.3f',
                cmap='viridis', # Colorblind friendly, YlGnBu also looks nice
                linewidths=0.5,
                linecolor='black',
                annot_kws={"size": font_size, "weight": "bold"})

    # Add title and customize axis labels
    plt.title('Pearlson Correlation Heatmap', fontsize=font_size+10, fontweight='bold', pad=font_size+10)
    plt.xlabel('Variables', fontsize=font_size, fontweight='bold')
    plt.ylabel('Variables', fontsize=font_size, fontweight='bold')

    # Customize ticks
    plt.xticks(rotation=45, fontsize=font_size/2)  # Rotate x-axis labels for readability
    plt.yticks(rotation=0, fontsize=font_size/2)  # Keep y-axis labels horizontal

    # Adjust color bar label size after creating the heatmap
    cbar = heatmap.collections[0].colorbar.ax  
    cbar.set_ylabel("Correlation Coefficient", fontsize=font_size)  
    cbar.tick_params(labelsize=font_size/2) 

    # Save the heatmap as an image
    plt.savefig(f'./Heatmap_Results/{FILE_NAME}.png', dpi=300)

    # Display the heatmap
    plt.show()



