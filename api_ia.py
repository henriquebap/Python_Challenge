from roboflow import Roboflow
import os
#import json

#print("Current working directory:", os.getcwd())
def cv_api():
    # Initialize the Roboflow object with your API key
    rf = Roboflow(api_key="fFzjCpFlDM2cN1D0XgOj")

    # Specify the Roboflow project and model
    project = rf.workspace().project("bike-only")
    model = project.version(2).model

    # Get the image path from user input
    image_path = input("Enter the path to the image: ")

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print("Image file not found.")
    else:
        # Make predictions
        prediction_result = model.predict(image_path, confidence=40, overlap=30).json()

        # Define a function to explore the JSON response
    def explore_json(obj, prefix=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                explore_json(value, prefix + key + ".")
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                explore_json(item, prefix + str(index) + ".")
        else:
            print(f"Campo: {prefix[:-1]}, Valor: {obj}")

        # Explore the JSON response
    explore_json(prediction_result)

    # Specify the folder where you want to save the prediction image
    output_folder = "received_images"

    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Save the prediction image
    prediction_image_path = os.path.join(output_folder, "prediction.jpg")
    model.predict(image_path, confidence=40, overlap=30).save(prediction_image_path)
    print(f"Prediction image saved as {prediction_image_path}")
