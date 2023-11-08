from roboflow import Roboflow
import os
import shutil
import time


def cv_api(image_path):
    # Initialize the Roboflow object with your API key
    rf = Roboflow(api_key="fFzjCpFlDM2cN1D0XgOj")

    # Specify the Roboflow project and model
    project = rf.workspace().project("bike-only")
    model = project.version(2).model

    # Initialize output_folder
    output_folder = "received_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    timestamp = int(time.time())
    original_image_path = os.path.join(output_folder, f"original_image_{timestamp}.jpg")

    # Copy the image to the "received_images" folder with the unique filename
    shutil.copy2(image_path, original_image_path)

    # Use the correct image path for prediction
    image_path = original_image_path

    # Check if the image file exists
    if not os.path.isfile(image_path):
        print("Image file not found.")
    else:
        # Make predictions
        prediction_result = model.predict(image_path, confidence=50, overlap=50).json()

        # Explore the JSON response
        try:
            # Check if 'predictions' key exists in the JSON response
            if "predictions" in prediction_result:
                predictions = prediction_result["predictions"]

                # Loop through predictions
                for index, prediction in enumerate(predictions):
                    print(f"Prediction {index + 1}:")
                    confidence = prediction.get("confidence", None)
                    predicted_class = prediction.get("class", None)

                    if confidence is not None and predicted_class is not None:
                        if confidence > 0.50 or predicted_class != "bike":
                            print("A foto da bicicleta foi aprovada!")
                        else:
                            print("Infelizmente a foto da sua bicicleta foi recusada.")
                    else:
                        print("Error: Incomplete prediction data.")
            else:
                print("Error: 'predictions' key not found in the JSON response.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    prediction_image_path = os.path.join(output_folder, "prediction.jpg")
    model.predict(image_path, confidence=50, overlap=50).save(prediction_image_path)

    return (
        image_path,
        prediction_image_path,
        predicted_class,
        confidence,
    )
