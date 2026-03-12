import pandas as pd

def recommend_product(category, budget, usage, brand):

    if category == 'Camera':
        df = pd.read_csv('dataset/camera.csv')

    elif category == 'Laptop':
        df = pd.read_csv('dataset/laptop.csv')

    else:
        df = pd.read_csv('dataset/phones.csv')

    # Budget filtering
    df = df[df['price'] <= budget]

    if brand:
        df = df[df['brand'].str.contains(brand,case=False)]

    recommendations = df.sort_values(by='rating',ascending=False)
    return recommendations.head(5)