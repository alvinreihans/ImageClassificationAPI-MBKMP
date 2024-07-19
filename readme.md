# Machine Learning Model API

A Flask API for a machine learning model developed using Convolutional Neural Networks (CNN) and stored in HDF5 format.

## Features

- Convolutional Neural Network (CNN) model for predictions
- Flask API for easy interaction with the model
- Example usage with Postman

## Requirements

- Python 3.x
- All necessary libraries listed in `requirements.txt`

## Installation

1. Clone the repository:

   git clone https://github.com/alvinreihans/smart-grow-backend.git

2. Navigate to the project directory:

   cd your-repo-name

3. Install the required libraries::

   pip install -r requirements.txt

Note: The model could not be uploaded to GitHub due to the file size being too large.

## Usage
1. Run the Flask application:

    python app.py

2. Open Postman and create a new request.
3. Set the request method to POST.
4. Set the request URL to http://127.0.0.1:5000/predict (or the appropriate endpoint).
5. Go to the Body tab, select form-data, and add a key file with type file. Choose the image file you want to upload for prediction.
6. Send the request and view the response.

## Example
Below is an example of how to use the API with Postman:
<img src="Screenshot 2024-07-19 155316.png">


## File Structure
- app.py: Main application file
- model.h5: Trained CNN model
- requirements.txt: List of required libraries

## Contributing
Feel free to open issues or submit pull requests if you have any suggestions for improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
