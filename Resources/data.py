import pandas as pd
import os

# Establish path to CSV
file_path = os.path.join("cities_convert.csv")

# Convert CSV to Pandas df
df = pd.read_csv(file_path)

# Establish path to HTML output file
output_path = os.path.join("..", "assets", "cities.html")

# Convert df to HTML file
df.to_html(output_path)