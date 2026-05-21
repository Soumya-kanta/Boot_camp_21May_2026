# StratLytics Coding Test

These files for the practical coding assessment.

Input files:
- input_data/customers.csv
- input_data/orders.csv
- input_data/products.json

I have created solution in a repository structure similar to:

src/pipeline.py
output/
logs/
requirements.txt
Dockerfile
README.md

The main overview of the project is 
It reads all the input files successfully. Then It will validate the records. After validateing it will transfer and aggregate the data. It will give the Revenue(quantity * unit_price), it joins all the valid orders with product name and catagory.
After that it will create one output file where where all the cleaned and rejected orders, customer and products file present.

