# Xvibe: Music Vibe Classification Model

## Overview
This project is part of Xvibe, an offline music player. The classification model is used to automatically assign labels to songs, enabling Xvibe to organize music into categories and generate a randomized list of songs for recommendation.

## Vibe Categories
```text
The model predicts one of five vibe labels:

| Vibe      | Associated Genres                 |
| --------- | --------------------------------- |
| Acoustic  | Acoustic                          |
| Chaotic   | Rock, Metal                       |
| Chill     | Hip-Hop, Reggae, R&B              |
| Energetic | Country, Disco, Pop               |
| Relaxing  | Blues, Jazz                       |
```

## Pipeline Flow
```text
Songs (Audio Files)
        ↓
Audio Preprocessing
        ↓
YAMNet Model (1024 Embeddings)
        ↓
Music Vibe Neural Network Classifier
        ↓
Vibe Prediction (Acoustic | Chaotic | Chill | Energetic | Relaxing)
        ↓
Database Storage (Path + Song metadata + predicted vibe label)
        ↓
Randomized Song List Recommendation + Music Organization
```

### Classification Report
```text
| Vibe      | Precision | Recall | F1-score | Support |
| --------- | --------- | ------ | -------- | ------- |
| Relaxing  | 0.84      | 0.92   | 0.88     | 959     |
| Chaotic   | 0.83      | 0.79   | 0.81     | 640     |
| Chill     | 0.82      | 0.79   | 0.80     | 936     |
| Energetic | 0.77      | 0.73   | 0.75     | 959     |
| Acoustic  | 0.77      | 0.81   | 0.79     | 600     |
```

### Overall Performance
```text
| Metric          | Value |
| --------------- | ----- |
| Accuracy        | 0.81  |
| Macro Avg F1    | 0.81  |
| Weighted Avg F1 | 0.81  |
| Total Samples   | 4094  |

```

### Confusion Matrix
```text
| Actual \ Predicted | Relaxing | Chaotic | Chill | Energetic | Acoustic |
| ------------------ | -------- | ------- | ----- | --------- | -------- |
| Relaxing           | 885      | 32      | 17    | 6         | 19       |
| Chaotic            | 27       | 506     | 25    | 55        | 27       |
| Chill              | 37       | 12      | 735   | 98        | 54       |
| Energetic          | 59       | 52      | 107   | 699       | 42       |
| Acoustic           | 40       | 10      | 17    | 45        | 488      |
```

### Technologies & Tools Used:
Python, TensorFlow Keras, YAMNet, NumPy, Pandas, Scikit-Learn, Librosa, yt_dlp, and TFLite.

### Techniques Used:
Supervised Learning, Audio Segmentation, Transfer Learning, Dropout Regularization, and Batch Normalization.

### Activation Function:
ReLU, Softmax.

### Dataset
GTZAN(1000) + R&B and Acoustic Songs from YouTube(Imbalanced)
