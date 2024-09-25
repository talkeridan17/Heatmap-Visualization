# Correlation Heatmap

## Author
@IdanTalker

## Description
Assuming correlation data is formatted correctly and stored in a csv file, then using public libaries pandas,
seaborn and matplotlib to read and present the data in a 2D heatmap. Each slot in the heatmap showcase the
correlation between the two intersecting categories of its row and column. Works for MacOS/Linux enviorment.

## Installation
To run this project, you need to have Python installed on your machine along with the following libraries:
- pandas
- seaborn
- matplotlib
You can install the required libraries using pip:
pip install pandas seaborn matplotlib

## Instructions
Add the csv file in the correct format (example in the heatmap.csv file) to the "CSV_Files" folder. Change
the constant FILE_NAME at the top of the heatmap_gen.py python program to the name of the csv file from which
to make the heatmap, excluding the ".csv" extention. Run the heatmap_gen.py file, (may take a couple of seconds)
and your heatmap will generate in the "Heatmap_Results" directory as a png image under the same name of the csv
file you provided, aka "FILE_NAME.png".

## Notes
- This project uses a specific CSV file structure. Ensure your files follow the expected format.
- If you're running this on Windows, the file paths should work with forward slashes (`/`), but feel free to change them to backslashes (`\\`) if preferred.
- The heatmap is generated with a large figure size (40x40), so it might take a little longer to render for large datasets.
- Ensure that you have the required Python packages installed: `pandas`, `seaborn`, and `matplotlib`.

## Lisence
This project is licensed under the MIT License - see the [LICENSE](./LICENSE.txt) file for details.
