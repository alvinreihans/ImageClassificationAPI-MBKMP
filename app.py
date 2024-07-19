from flask import Flask, request, jsonify
from tensorflow.keras.utils import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import os

model = load_model("model-micromelum.h5")

class_names = [
    "Micromelum Minutum - Batang",
    "Micromelum Minutum - Daun",
    "Micromelum Minutum - Ranting",
]


def predict_img(file):
    if file.endswith(("jpg", "jpeg", "png")):
        img = load_img(file, target_size=(224, 224))
        x = img_to_array(img)
        x /= 255.0
        x = np.expand_dims(x, axis=0)

        predictions = model.predict(x)
        predicted_class = np.argmax(predictions, axis=1)[0]

        print(f"File: {file}")
        if predicted_class < len(class_names):
            return str(class_names[predicted_class])
        else:
            return "error: unknown class"


# aplikasi
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict_endpoint():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file:
        # Simpan file yang diunggah
        filename = file.filename
        filepath = os.path.join("./tmp", filename)
        file.save(filepath)
        result = predict_img(filepath)
        os.remove(filepath)

        return jsonify({"prediction": result})


if __name__ == "__main__":
    app.run(debug=True)
