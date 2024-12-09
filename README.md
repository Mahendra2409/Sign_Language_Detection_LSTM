# Hand Gesture Recognition with LSTM

This project uses Mediapipe for detecting hand gestures, facial landmarks, and body poses in real-time video and then utilizes a trained LSTM (Long Short-Term Memory) model to recognize specific actions (e.g., "hello," "thanks," "I love you") based on hand and body movements.

## Table of Contents

- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Model Training](#model-training)
- [License](#license)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/hand-gesture-recognition.git
    cd hand-gesture-recognition
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Dependencies

- `mediapipe`: For detecting landmarks in hands, face, and body pose.
- `opencv-python`: For capturing webcam feed and displaying results.
- `tensorflow`: For training and using the LSTM model for action recognition.
- `numpy`: For data manipulation and storing keypoints.
- `scikit-learn`: For data preprocessing.
- `matplotlib`: For plotting and visualizations.
- `keras`: For building and training the LSTM model.

Ensure you have the following libraries installed before running the project.

    ```bash
    pip install opencv-python mediapipe tensorflow numpy scikit-learn matplotlib
    ```

## Usage

### 1. Run the Real-Time Gesture Recognition

To use the real-time gesture recognition with your webcam:

    ```bash
    python gesture_recognition.py
    ```

This will open a video feed using your webcam and start recognizing actions based on hand gestures. The model will predict actions such as "hello," "thanks," and "I love you" based on detected gestures.

- **Press `q` to exit** the webcam feed.

### 2. Output

The recognized action will be displayed at the top of the video feed, and a colored bar will indicate the model’s confidence level for each action. The actions recognized will also appear as a sentence at the top of the frame.

## Model Training

If you want to train the model with your own gestures or data, follow these steps:

1. **Prepare the Dataset**:
   - Create a folder `MP_Data` with subfolders for each action (e.g., `hello`, `thanks`, `iloveyou`).
   - Each action folder should contain multiple sequences (videos) of that action, and each video should be split into 30 frames of keypoints in `.npy` format.

2. **Train the Model**:
   - Once the dataset is prepared, the script `train_model.py` can be used to train the model.
   - The model will be saved as `action2.h5`, which can later be used for real-time prediction in `gesture_recognition.py`.

    ```bash
    python train_model.py
    ```

3. **Model Structure**:
   The LSTM model consists of:
   - Three LSTM layers.
   - Dense layers for classification.
   - Softmax output for multi-class classification.

## Files

- `gesture_recognition.py`: The main script for real-time gesture recognition using webcam feed and a trained LSTM model.
- `train_model.py`: The script for training the model on the prepared dataset.
- `MP_Data/`: Directory where dataset and `.npy` files for keypoints are stored.
- `action2.h5`: Pre-trained model file for gesture recognition.
- `requirements.txt`: List of required dependencies for the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
