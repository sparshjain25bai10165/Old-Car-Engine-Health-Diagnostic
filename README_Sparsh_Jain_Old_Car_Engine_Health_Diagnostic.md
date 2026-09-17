# 🚗 Old Car Engine Health Diagnostic via Audio

A simple AI and Machine Learning project that uses the sound of an old car engine to identify whether the engine audio appears normal or shows an abnormal pattern. The project takes an engine audio recording, extracts useful sound features, and uses a machine learning model to classify the sound.

The project is designed as a beginner-friendly **Fundamental of AI & ML** project. It is meant for learning and early screening, and it does not replace a professional mechanic or a complete vehicle inspection.

## 👨‍💻 Project Information

- **Student Name:** Sparsh Jain
- **Course Name:** Fundamental of AI & ML
- **Project Topic:** Old Car Engine Health Diagnostic via Audio
- **Project Type:** AI & ML Mini Project
- **Language:** Python
- **Main File:** `engine_health_diagnostic.py`

## 📖 Table of Contents

- [Overview](#overview)
- [Objectives](#objectives)
- [Key Features](#key-features)
- [How the System Works](#how-the-system-works)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Audio Features](#audio-features)
- [Machine Learning Model](#machine-learning-model)
- [Sample Input](#sample-input)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Advantages](#advantages)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)
- [Author](#author)

## 🔎 Overview

Old cars can sometimes produce unusual sounds when there is a mechanical problem. For a normal person, it may be difficult to understand whether a sound is normal or something that needs to be checked.

The **Old Car Engine Health Diagnostic via Audio** project uses AI and Machine Learning to analyse an engine recording. The audio is converted into numerical features, and a trained classification model learns patterns from labelled engine sounds.

The system can give a simple result such as:

- **Normal Engine Sound**
- **Possible Abnormal Engine Sound**

The result should be treated as an early indication only. It cannot confirm a particular mechanical fault.

## 🎯 Objectives

The main objectives of this project are:

1. To create a simple AI/ML system for analysing old car engine sounds.
2. To use audio as the main input for engine-condition screening.
3. To extract useful numerical features from engine audio.
4. To train a machine learning classification model using labelled audio samples.
5. To predict the condition of a new engine recording.
6. To understand the basic AI/ML workflow from data collection to prediction.

## 🚀 Key Features

### 🎙️ Audio Input

The system accepts a short recording of a running car engine.

Example:

```text
engine_01.wav
```

### 🔊 Audio Feature Extraction

The raw audio is converted into useful numerical information. Features can include:

- MFCC
- RMS Energy
- Zero Crossing Rate
- Spectral Centroid
- Spectral Bandwidth

### 🤖 Machine Learning Classification

The extracted features are given to a machine learning model. A model such as Random Forest can be used for a beginner-level implementation.

### 🧾 Simple Human-Language Result

Instead of showing only a technical prediction number, the program can display a simple message:

```text
The engine sound appears similar to the normal samples.
```

or

```text
The engine sound has an abnormal pattern.
Further mechanical checking is recommended.
```

## ⚙️ How the System Works

The system works in a few simple stages:

1. **Record Audio:** Record the sound of the old car engine.
2. **Load Audio:** The Python program loads the audio file.
3. **Pre-processing:** The audio is prepared for analysis.
4. **Feature Extraction:** Important sound features are calculated.
5. **Model Training:** The machine learning model learns from labelled examples.
6. **Prediction:** Features from a new recording are given to the trained model.
7. **Output:** The system displays the predicted engine sound condition.

The complete basic flow is:

```text
Engine Audio
     ↓
Audio Pre-processing
     ↓
Feature Extraction
     ↓
Machine Learning Model
     ↓
Prediction
     ↓
Normal / Possible Abnormal
```

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Python Version:** Python 3.x
- **Audio Processing:** Librosa
- **Numerical Processing:** NumPy
- **Data Handling:** Pandas
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib
- **IDE/Editor:** VS Code / PyCharm / Jupyter Notebook
- **Operating System:** Windows / macOS / Linux

## 📋 Requirements

Before running the project, make sure Python is installed.

You can check the installation by running:

```bash
python --version
```

Install the required libraries:

```bash
pip install numpy pandas librosa scikit-learn matplotlib
```

A microphone or mobile phone can be used to record engine audio.

## 💻 Installation

### 1. Get the Project

Download or clone the project repository.

```bash
git clone <your-repository-link>
```

Then open the project folder:

```bash
cd old-car-engine-health-diagnostic
```

### 2. Install Libraries

Run:

```bash
pip install numpy pandas librosa scikit-learn matplotlib
```

### 3. Add Audio Dataset

Create folders for the labelled audio samples:

```text
dataset/
├── normal/
└── abnormal/
```

Place the relevant `.wav` audio recordings inside the appropriate folder.

### 4. Run the Program

Run:

```bash
python engine_health_diagnostic.py
```

The program will process the audio and display the predicted result.

## ▶️ Usage

A simple usage example is:

```text
Audio File: engine_test.wav

Processing audio...
Extracting features...
Running machine learning model...

Result:
Possible Abnormal Engine Sound
Further mechanical checking is recommended.
```

The exact prediction depends on the training dataset and the quality of the recording.

## 🎵 Audio Features

The project can use different audio features to describe the engine sound.

### MFCC

MFCC stands for **Mel-Frequency Cepstral Coefficients**. It represents important characteristics of an audio signal in numerical form and is commonly used in audio classification tasks.

### RMS Energy

RMS energy gives an idea of the strength or energy level of the audio signal.

### Zero Crossing Rate

Zero Crossing Rate measures how frequently the audio signal changes from positive to negative or negative to positive.

### Spectral Centroid

Spectral centroid gives information about where the centre of the sound's frequency content is located.

### Spectral Bandwidth

Spectral bandwidth describes the spread of the frequencies around the spectral centre.

These features together can provide useful information for a machine learning classifier.

## 🧠 Machine Learning Model

For a simple implementation, **Random Forest Classifier** can be used.

The basic process is:

```text
Training Audio
      ↓
Feature Extraction
      ↓
Training Dataset
      ↓
Random Forest Model
      ↓
Trained Model
```

For a new recording:

```text
New Engine Audio
      ↓
Feature Extraction
      ↓
Trained Model
      ↓
Prediction
```

The project can also be extended later with other models such as:

- Support Vector Machine
- Logistic Regression
- K-Nearest Neighbours
- Neural Networks
- CNN-based audio classification

## 📝 Sample Input

| Field | Sample Value |
|---|---|
| Audio File | `engine_test.wav` |
| Recording Length | 10 seconds |
| Audio Format | WAV |
| Engine Type | Old Car |
| Recording Condition | Engine Running |
| Label for Training | Normal / Abnormal |

## 📊 Sample Output

```text
----------------------------------
Old Car Engine Health Diagnostic
----------------------------------

Audio file: engine_test.wav

Loading audio...
Extracting audio features...
Running prediction...

Predicted Condition:
NORMAL ENGINE SOUND

The audio pattern is similar to the normal training samples.
```

Another possible output:

```text
----------------------------------
Old Car Engine Health Diagnostic
----------------------------------

Audio file: engine_test.wav

Loading audio...
Extracting audio features...
Running prediction...

Predicted Condition:
POSSIBLE ABNORMAL ENGINE SOUND

The audio pattern is different from the normal samples.
Further mechanical checking is recommended.
```

## 📂 Project Structure

```text
old-car-engine-health-diagnostic/
│
├── dataset/
│   ├── normal/
│   │   ├── engine_01.wav
│   │   └── engine_02.wav
│   │
│   └── abnormal/
│       ├── engine_03.wav
│       └── engine_04.wav
│
├── engine_health_diagnostic.py
├── requirements.txt
├── README.md
└── trained_model.pkl
```

## 🧩 Main Functions

A simple implementation can be divided into functions such as:

```text
load_audio()
```

Loads the engine recording.

```text
extract_features()
```

Extracts MFCC and other audio features.

```text
prepare_dataset()
```

Creates the feature dataset and labels.

```text
train_model()
```

Trains the machine learning classifier.

```text
predict_condition()
```

Predicts the condition of a new audio recording.

```text
main()
```

Runs the complete program.

## 📈 Model Evaluation

The model should be tested using audio recordings that were not used during training.

Useful evaluation measures include:

- Accuracy
- Precision
- Recall
- Confusion Matrix

Example project testing values:

```text
Training Samples: 80
Testing Samples: 20
Correct Predictions: 17
Incorrect Predictions: 3
Example Accuracy: 85%
```

These numbers are only example values for demonstrating the project. They are not claimed real-world performance. Actual accuracy must be calculated from the project's real dataset.

## ✅ Advantages

- Uses a simple audio recording as input.
- Demonstrates a practical application of AI and ML.
- Can be developed using commonly available Python libraries.
- Gives a quick first-level screening result.
- Can be improved by adding more labelled engine recordings.
- Helps students understand audio classification and machine learning.

## ⚠️ Limitations

The current project has some limitations:

- Background noise can affect the prediction.
- Different car models can have different normal engine sounds.
- A small dataset may not give reliable results.
- Recording position and microphone quality can change the audio.
- The model may not identify the exact damaged engine part.
- A predicted abnormal sound does not prove that a mechanical fault exists.
- The system should not replace a professional mechanical inspection.

## 🔮 Future Enhancements

The project can be improved in the future by adding:

- A larger and more diverse engine audio dataset.
- A mobile application for recording engine sounds.
- Real-time engine sound analysis.
- Better noise reduction.
- Multiple fault categories instead of only normal/abnormal.
- Deep learning models such as CNNs for audio classification.
- A confidence value with the prediction.
- Vehicle information such as car model and engine type.
- A history feature to compare repeated engine sound checks.
- A simple graphical user interface.

## 🏁 Conclusion

The **Old Car Engine Health Diagnostic via Audio** is a simple AI and Machine Learning project that shows how sound can be used as data for classification.

The project follows a basic AI/ML process: collect engine audio, prepare the data, extract useful features, train a machine learning model, test it, and use the model to predict the condition of a new recording.

The project is mainly useful for learning the practical application of AI and ML. Since engine sounds can change because of many factors, the output should be considered an early screening result and not a final diagnosis.

## 📚 References

1. Librosa documentation – audio loading and feature extraction.
2. Scikit-learn documentation – machine learning algorithms and evaluation.
3. NumPy documentation – numerical processing in Python.
4. Pandas documentation – data handling in Python.
5. General concepts of audio signal processing and machine learning classification.

## 👨‍💻 Author

**Sparsh Jain**

**Course:** Fundamental of AI & ML

**Project:** Old Car Engine Health Diagnostic via Audio
