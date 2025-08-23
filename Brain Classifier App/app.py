from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
model = load_model('brain_tumor_classifier.h5')

# Update this based on your training data class order
classes = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    image_url = ""

    if request.method == 'POST':
        img = request.files['image']
        if img:
            upload_path = os.path.join('static/uploads', img.filename)
            img.save(upload_path)
            image_url = upload_path

            # Preprocess image
            img_data = image.load_img(upload_path, target_size=(64, 64))  # match your training size
            img_array = image.img_to_array(img_data)
            img_array = np.expand_dims(img_array, axis=0) / 255.0

            # Predict
            preds = model.predict(img_array)
            predicted_class = classes[np.argmax(preds)]
            prediction = f"{predicted_class.upper()} ({100 * np.max(preds):.2f}%)"

    return render_template('index.html', prediction=prediction, image_url=image_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os
# from PIL import Image

# app = Flask(__name__)
# model = load_model('brain_tumor_classifier.h5')

# # Update this based on your training data class order
# classes = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# # Create the upload folder if it doesn't exist
# os.makedirs('static/uploads', exist_ok=True)

# # === MRI Image Check Function ===
# def is_mri_image(image_path):
#     try:
#         img = Image.open(image_path).convert('L')  # Convert to grayscale
#         img_array = np.array(img)
#         mean_brightness = np.mean(img_array)
#         variance = np.var(img_array)
#         if 30 < mean_brightness < 200 and variance > 500:
#             return True
#         else:
#             return False
#     except Exception as e:
#         print("Error checking MRI image:", e)
#         return False

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = ""
#     image_url = ""

#     if request.method == 'POST':
#         img = request.files['image']
#         if img:
#             upload_path = os.path.join('static/uploads', img.filename)
#             img.save(upload_path)
#             image_url = upload_path

#             # Check if it's an MRI-like image
#             if not is_mri_image(upload_path):
#                 prediction = "The uploaded image does not appear to be a brain MRI. Please upload a valid image."
#             else:
#                 # Preprocess image
#                 img_data = image.load_img(upload_path, target_size=(64, 64))  # Adjust to your model's input size
#                 img_array = image.img_to_array(img_data)
#                 img_array = np.expand_dims(img_array, axis=0) / 255.0

#                 # Predict
#                 preds = model.predict(img_array)
#                 predicted_class = classes[np.argmax(preds)]
#                 prediction = f"{predicted_class.upper()} ({100 * np.max(preds):.2f}%)"

#     return render_template('index.html', prediction=prediction, image_url=image_url)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import os
# from PIL import Image

# app = Flask(__name__)
# model = load_model('brain_tumor_classifier.h5')

# # Class labels in your model's order
# classes = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# os.makedirs('static/uploads', exist_ok=True)

# def is_mri_image(image_path):
#     try:
#         img = Image.open(image_path)
#         width, height = img.size

#         # Accept grayscale or RGB, just check minimum size
#         if width >= 64 and height >= 64:
#             return True
#         return False
#     except:
#         return False

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = ""
#     image_url = ""

#     if request.method == 'POST':
#         img = request.files['image']
#         if img:
#             upload_path = os.path.join('static/uploads', img.filename)
#             img.save(upload_path)
#             image_url = upload_path

#             if not is_mri_image(upload_path):
#                 prediction = "⚠️ The uploaded image does not appear to be a brain MRI. Please upload a valid image."
#                 image_url = ""
#             else:
#                 img_data = image.load_img(upload_path, target_size=(64, 64))
#                 img_array = image.img_to_array(img_data)
#                 img_array = np.expand_dims(img_array, axis=0) / 255.0

#                 preds = model.predict(img_array)
#                 predicted_class = classes[np.argmax(preds)]
#                 confidence = 100 * np.max(preds)
#                 prediction = f"{predicted_class.upper()} ({confidence:.2f}%)"

#     return render_template('index.html', prediction=prediction, image_url=image_url)

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from PIL import Image
# import numpy as np
# import os

# app = Flask(__name__)
# model = load_model('brain_tumor_classifier.h5')
# classes = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# # MRI check function with debug prints
# def is_mri_image(image_path):
#     img = Image.open(image_path).convert('L')  # grayscale
#     img_array = np.array(img)
#     mean_brightness = np.mean(img_array)
#     variance = np.var(img_array)
#     print(f"Mean brightness: {mean_brightness}, Variance: {variance}")
#     return (30 < mean_brightness < 200) and (variance > 500)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = ""
#     image_url = ""
#     error_msg = ""

#     if request.method == 'POST':
#         img = request.files['image']
#         if img:
#             upload_folder = 'static/uploads'
#             os.makedirs(upload_folder, exist_ok=True)  # create folder if not exist
#             upload_path = os.path.join(upload_folder, img.filename)
#             img.save(upload_path)
#             print(f"Image saved at {upload_path}")
#             image_url = upload_path

#             # Check if image looks like MRI
#             if not is_mri_image(upload_path):
#                 error_msg = "The uploaded image does not appear to be an MRI scan. Please upload a valid MRI image."
#                 print(error_msg)
#             else:
#                 print("Image passed MRI check, predicting...")
#                 # Preprocess image
#                 img_data = image.load_img(upload_path, target_size=(64, 64))
#                 img_array = image.img_to_array(img_data)
#                 img_array = np.expand_dims(img_array, axis=0) / 255.0

#                 # Predict
#                 preds = model.predict(img_array)
#                 predicted_class = classes[np.argmax(preds)]
#                 prediction = f"{predicted_class.upper()} ({100 * np.max(preds):.2f}%)"
#                 print("Prediction:", prediction)

#     return render_template('index.html', prediction=prediction, image_url=image_url, error_msg=error_msg)

# if __name__ == '__main__':
#     app.run(debug=True)
