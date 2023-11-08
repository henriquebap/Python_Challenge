from roboflow import Roboflow
import os


def cv_api():
    # Initialize the Roboflow object with your API key
    rf = Roboflow(api_key="fFzjCpFlDM2cN1D0XgOj")

    # Specify the Roboflow project and model
    project = rf.workspace().project("bike-only")
    model = project.version(2).model

    # Get the image path from user input
    image_path = input("Coloque o caminho da imagem: ")

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
                            print("a foto da bicicleta foi aprovada!")
                        else:
                            print("Infelizmente a foto da sua bicicleta foi recusada.")
                    else:
                        print("Error: Incomplete prediction data.")
            else:
                print("Error: 'predictions' key not found in the JSON response.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    original_image_path = os.path.join(output_folder, "original_image.jpg")
    os.rename(image_path, original_image_path)

    prediction_image_path = os.path.join(output_folder, "prediction.jpg")
    model.predict(image_path, confidence=50, overlap=50).save(prediction_image_path)

    # Specify the folder where you want to save the prediction image
    output_folder = "received_images"

    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_path = image_path
    prediction_image_path = image_path
    predicted_class = predicted_class
    confidence = confidence

    return (
        image_path,
        prediction_image_path,
        predicted_class,
        confidence,
    )

    # Save the prediction image
    prediction_image_path = os.path.join(output_folder, "prediction.jpg")
    model.predict(image_path, confidence=50, overlap=50).save(prediction_image_path)
    print(f"Prediction image saved as {prediction_image_path}")
