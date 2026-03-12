import pandas as pd

def compare_products(
    product1,
    product2,
    dataset
    ):

  df = pd.read_csv(dataset)

  p1 = df[df['model'] == product1]
  p2 = df[df['model'] == product2]

  comparison = pd.concat([p1,p2])

  return comparison.T