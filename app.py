import pandas as pd
import streamlit as st
#from models.recommender import recommend_product



def camera_preferences():
    budget = st.sidebar.number_input("Budget (USD)", min_value=100, max_value=10000, value=1000, step=100,key="camera_budget")
    usage = st.sidebar.selectbox("Usage", ["Photography", "Vlogging", "Video Editing", "Gaming", "Other"],key="camera_usage")
    camera_type = st.sidebar.selectbox("Camera Type", ["DSLR", "Mirrorless", "Action Camera", "Point & Shoot"])
    sensor_size = st.sidebar.selectbox("Sensor Size", ["1/2.3", "1/2.5", "1/1.7", "1/1.5", "1/1.3", "1/1.0"])
    resolution = st.sidebar.selectbox("Resolution", ["1080p", "4K", "8K"])
    lens_type = st.sidebar.selectbox("Lens Type", ["Prime", "Zoom", "Telephoto", "Wide Angle"])
    lens_focal_length = st.sidebar.number_input("Focal Length (mm)", min_value=20, max_value=1000, value=50, step=10)
    lens_aperture = st.sidebar.number_input("Aperture (f/)", min_value=1.8, max_value=16.0, value=4.0, step=0.1)
    battery_capacity = st.sidebar.number_input("Battery Capacity (mAh)", min_value=2000, max_value=10000, value=3000, step=100,key="camera_battery_capacity")
    return budget, usage, camera_type, sensor_size, resolution, lens_type, lens_focal_length, lens_aperture, battery_capacity

def laptop_preferences():
    budget = st.sidebar.number_input("Budget (USD)", min_value=500, max_value=10000, value=1000, step=100,key="laptop_budget")
    usage = st.sidebar.selectbox("Usage", ["Work", "Gaming", "Design", "Other"],key="laptop_usage")
    processor = st.sidebar.selectbox("Processor", ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9", "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9"])
    memory = st.sidebar.selectbox("Memory (GB)", [4, 8, 16, 32, 64])
    storage = st.sidebar.selectbox("Storage (GB)", [256, 512, 1024, 2048, 4096])
    screen_size = st.sidebar.number_input("Screen Size (inches)", min_value=13.0, max_value=17.0, value=15.0, step=0.5,key="laptop_screen_size")
    screen_resolution = st.sidebar.selectbox("Screen Resolution", ["1920x1080", "2560x1440", "3840x2160"])
    battery_capacity = st.sidebar.number_input("Battery Capacity (mAh)", min_value=2000, max_value=10000, value=3000, step=100,key="laptop_battery_capacity")
    return budget, usage, processor, memory, storage, screen_size, screen_resolution, battery_capacity

def phone_preferences():
    budget = st.sidebar.number_input("Budget (USD)", min_value=200, max_value=10000, value=500, step=100,key="phone_budget")
    usage = st.sidebar.selectbox("Usage", ["Work", "Gaming", "Design", "Other"],key="phone_usage")
    screen_size = st.sidebar.number_input("Screen Size (inches)", min_value=5.0, max_value=7.0, value=6.0, step=0.5,key="phone_screen_size")
    screen_resolution = st.sidebar.selectbox("Screen Resolution", ["1080x1920", "1440x2560", "2160x3840"])
    storage = st.sidebar.selectbox("Storage (GB)", [128, 256, 512, 1024])
    camera_quality = st.sidebar.selectbox("Camera Quality", ["12MP", "16MP", "24MP", "48MP"])
    battery_capacity = st.sidebar.number_input("Battery Capacity (mAh)", min_value=2000, max_value=10000, value=3000, step=100,key="phone_battery_capacity") 
    return budget, usage, screen_size, screen_resolution, storage, camera_quality, battery_capacity

def recommend_product(device_type, budget, usage, camera_type, sensor_size, resolution, lens_type, lens_focal_length, lens_aperture, processor, memory, storage, screen_size, screen_resolution, camera_quality, battery_capacity):
    if device_type == "Camera":
        recommended_product = camera_preferences(budget, usage, camera_type, sensor_size, resolution, lens_type, lens_focal_length, lens_aperture, battery_capacity)
    elif device_type == "Laptop":
        recommended_product = laptop_preferences(budget, usage, processor, memory, storage, screen_size, screen_resolution, battery_capacity)
    elif device_type == "Phone":
        recommended_product = phone_preferences(budget, usage, screen_size, screen_resolution, storage, camera_quality, battery_capacity)
    return recommended_product
 
def main():
    st.set_page_config(page_title="AI Electronics Purchase Advisor", page_icon=":camera:",layout='wide')
    st.title("📷 AI Electronics Purchase Advisor")

    st.markdown("""
    Welcome to the **AI-Powered Electronics Recommendation Assistant**!

    This tool helps customers choose the best product based on:
    - Budget
    - Usage purpose
    - Technical preferences
    - Market trends
    - Product reviews

    Fill in your preferences to get recommendations
    """)

    st.sidebar.header("User Preferences")
    


    device_type = st.sidebar.selectbox("Device Type", ["Camera", "Laptop", "Phone"],key="device_type")

    # Call preferences ONCE(this renders the sidebar widgets once)
    camera_type = sensor_size = resolution = lens_type = lens_focal_length = lens_aperture = None
    processor = memory = storage = screen_size = screen_resolution = camera_quality = battery_capacity = None
    camera_quality = None
    
    if device_type == "Camera":
        budget, usage, camera_type, sensor_size, resolution, lens_type, lens_focal_length, lens_aperture, battery_capacity = camera_preferences()
        storage = screen_size = screen_resolution = None
    elif device_type == "Laptop":
        budget, usage, processor, memory, storage, screen_size, screen_resolution, battery_capacity = laptop_preferences()
        camera_type = sensor_size = resolution = lens_type = lens_focal_length = lens_aperture = None
        camera_quality = None
    elif device_type == "Phone":
        budget, usage, screen_size, screen_resolution, storage, camera_quality, battery_capacity = phone_preferences()     
        camera_type = sensor_size = resolution = lens_type = lens_focal_length = lens_aperture = None
        processor = memory = None
    if st.button('Generate Recommendation'):
        with st.spinner('Analyzing product datasets.....'):
            recommended_product = recommend_product(
                device_type, 
                budget, usage, camera_type, 
                sensor_size, resolution,
                lens_type, lens_focal_length, 
                lens_aperture, processor, memory, 
                storage, screen_size, screen_resolution,
                camera_quality, battery_capacity
            )
            st.success('Recommendation generated successfully!')
            st.write(f"Recommended Product: {recommended_product}")

if __name__=="__main__":
    main()