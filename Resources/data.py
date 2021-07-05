import pandas as pd
import os

file_path = os.path.join("cities_convert.csv")

df = pd.DataFrame(file_path)

output_path = os.path.join("..", "assets", )

df.to_html()