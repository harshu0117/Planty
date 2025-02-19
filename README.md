# Planty: Potato Disease Detection Using Machine Learning

Planty is a machine learning project designed to identify diseases in potato plants through image analysis. By leveraging advanced deep learning techniques, Planty aims to assist farmers and agricultural professionals in early detection and management of potato diseases, thereby enhancing crop yield and quality.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Potato crops are susceptible to various diseases that can significantly impact yield and quality. Early and accurate detection is crucial for effective management. Planty utilizes convolutional neural networks (CNNs) to analyze images of potato leaves, identifying common diseases such as early blight and late blight.

## Features

- **Image Classification**: Accurately classifies images of potato leaves into healthy or diseased categories.
- **User-Friendly Interface**: Provides an intuitive frontend for users to upload images and receive instant results.
- **API Integration**: Offers a RESTful API for seamless integration with other applications.

## Dataset

The model is trained on the [Potato Disease Leaf Dataset (PLD)](https://www.kaggle.com/datasets/rizwan123456789/potato-disease-leaf-datasetpld), which includes images of healthy and diseased potato leaves. The dataset encompasses various conditions, enabling the model to learn and generalize effectively.

## Model Architecture

Planty employs a pre-trained Convolutional Neural Network (CNN) model, fine-tuned on the PLD dataset. This approach leverages transfer learning to achieve high accuracy in disease classification. The model architecture includes multiple convolutional layers, pooling layers, and fully connected layers, optimized for image recognition tasks.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```bash
   git clone https://github.com/harshu0117/Planty.git
   cd Planty
   ```


2. **Set up a virtual environment**:
    ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```


3. **Install dependencies**:
    ```bash
   pip install -r requirements.txt
   ```


## Usage

1. **Start the API server**:
    ```bash
   cd api
   python app.py
   ```


2. **Launch the frontend**:
    ```bash
   cd ../frontend
   open index.html  # Open the HTML file in your preferred browser
   ```


3. **Classify an image**:
   - Upload an image of a potato leaf through the frontend interface.
   - The model will process the image and display the classification result.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This README provides a general overview of the Planty project. For detailed information, please refer to the project's documentation and source code.* 
