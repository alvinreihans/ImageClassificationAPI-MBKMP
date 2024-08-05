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

3. Install the required libraries:

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

## Deployment on GCE
1. Create new static IP Address with the following configuration:
   - Name: `<ip-name>`
   - Tier: Premium
   - IP Version: IPV4
   - Type: Regional
   - Region: `<region>`
2. Create new firewall rule with the following configuration:
   - Name: <strong>allow-http</strong>
   - Network: default
   - Direction: ingress
   - Target tags: `<vm-name>`
   - IP ranges: 0.0.0.0/0
   - TCP: 8080
   - Enforcement: enabled
3. Create new instance with the following configuration:
   - Name: `<vm-name>`
   - Region: `<region>`
   - Machine type: n1-standard-1
   - Image: Ubuntu 20.04 LTS
   - Network interface:
      -External IPv4 address: `<ip-name>`
   - Firewall:
      - Allow HTTP traffic
      - Allow HTTPS traffic
   - Network tags: http-server, https-server, <strong>allow-http</strong>
4. SSH to the VM
5. Update and Install Required Packages:
   ```sh
   sudo apt update
   sudo apt upgrade -y
   sudo apt install python3-pip python3-venv -y
   ```
6. Upload main.py, requirements.txt, and model.h5 to VM
7. create new directory
   ```sh
   mkdir /static
   ```
   This directory used to reserve temporary images

8. Run this command to see the Working Directory Path
   ```sh
   pwd
   ```
9. Install libraries
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
10. Set up automatic service using gunicorn
   ```sh
   sudo nano /etc/systemd/system/myapp.service
   ```
11. Copy this code to myapp.service:
   ```sh
   [Unit]
   Description=Gunicorn instance to serve my Flask application
   After=network.target

   [Service]
   User=your-username
   Group=www-data
   WorkingDirectory=/path/to/your/application
   Environment="PATH=/path/to/your/application/venv/bin"
   ExecStart=/path/to/your/application/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:8080 main:app

   [Install]
   WantedBy=multi-user.target
   ```
   Replace <strong>/path/to/your/application</strong> with the actual path to your app that you get from step 8, and your-username with your username. Save the file.

12. Start and enable the service:
   ```sh
   sudo systemctl daemon-reload
   sudo systemctl restart myapp.service
   sudo systemctl status myapp.service

   ```
13. Use the external IP address of your VM to access your Flask app. For example, if your external IP is X.X.X.X, visit http://X.X.X.X:8080 in your browser.