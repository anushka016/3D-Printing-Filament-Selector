import pandas as pd
import os
import sqlite3

basedir = os.path.abspath(os.path.dirname(__name__))
file = os.path.join(basedir, 'items.xlsx')

cols = ['item_name', 'recommended_build_surfaces', 'ultimate_strength', 'stiffness', 'durability', 'printability',
        'density', 'min_price', 'max_price',
        'heated_bed', 'flexible', 'impact_resistant', 'uv_resistant',
        'water_resistant', 'dissolvable',
        'chemically_resistant']
data = pd.read_excel(file)
df = data[cols]
