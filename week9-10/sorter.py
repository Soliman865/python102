# sorter.py — Reference Implementation
# Weeks 9-10: AI Trash Sorter
#
# This is the reference — try building your own version with AI first (see README.md).
#
# Run:   python sorter.py
# Quit:  press ESC
#
# Requires:
#   pip install opencv-python tensorflow numpy
#   keras_Model.h5 and labels.txt in the same folder as this script

import os
import sys
import numpy as np
import cv2

# ── TensorFlow import ─────────────────────────────────────────────────────────
# We use tf.keras.models.load_model with compile=False.
# compile=False skips rebuilding the optimiser state, which is not needed for
# inference and avoids warnings on some TF versions.
try:
    import tensorflow as tf
    from tensorflow.keras.models import load_model
except ImportError:
    print("ERROR: TensorFlow is not installed.")
    print("Fix:   pip install tensorflow")
    sys.exit(1)

# ── Configuration ─────────────────────────────────────────────────────────────
MODEL_FILE          = "keras_Model.h5"
LABELS_FILE         = "labels.txt"
IMAGE_SIZE          = 224     # Teachable Machine trains on 224×224 images — must match exactly
CONFIDENCE_THRESHOLD = 0.70   # Only show a prediction if the model is this confident


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_labels(path):
    """
    Read labels.txt and return a list of class names.

    Teachable Machine labels.txt looks like:
        0 Paper
        1 Plastic
        2 Compost
        3 Trash

    We strip the leading number and whitespace.
    """
    with open(path, "r") as f:
        lines = f.readlines()
    return [line.strip().split(" ", 1)[1] for line in lines if line.strip()]


def preprocess_frame(frame):
    """
    Prepare a raw OpenCV frame for the model.

    Steps:
      1. Resize to IMAGE_SIZE × IMAGE_SIZE — the model was trained on this exact size.
         Feed it a different size and the prediction is meaningless (no crash, wrong answer).
      2. Convert BGR (OpenCV default) to RGB (what the model expects).
      3. Convert to float32 and normalise to [-1, 1].
         Raw pixel values are 0–255. The model was trained on [-1, 1], so we must match.
         Formula: pixel / 127.5 - 1.0
         (÷255 normalises to [0,1]; Teachable Machine uses [-1,1] specifically.)
      4. Add a batch dimension: model expects shape (1, 224, 224, 3), not (224, 224, 3).
    """
    resized  = cv2.resize(frame, (IMAGE_SIZE, IMAGE_SIZE))
    rgb      = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    normalised = (rgb.astype(np.float32) / 127.5) - 1.0
    return np.expand_dims(normalised, axis=0)   # shape: (1, 224, 224, 3)


def predict(model, frame, labels):
    """
    Run one frame through the model.

    Returns:
        (label, confidence) — e.g. ("Paper", 0.93)
        or ("Uncertain", 0.0) if no class exceeds CONFIDENCE_THRESHOLD.
    """
    input_data  = preprocess_frame(frame)
    predictions = model.predict(input_data, verbose=0)[0]   # shape: (num_classes,)

    best_index      = int(np.argmax(predictions))
    best_confidence = float(predictions[best_index])

    if best_confidence < CONFIDENCE_THRESHOLD:
        return "Uncertain", best_confidence

    return labels[best_index], best_confidence


def draw_overlay(frame, label, confidence):
    """
    Draw the prediction label and confidence bar onto the frame.
    """
    h, w = frame.shape[:2]

    # ── Background banner ────────────────────────────────────────────────────
    banner_h = 60
    cv2.rectangle(frame, (0, h - banner_h), (w, h), (0, 0, 0), thickness=-1)

    # ── Label text ───────────────────────────────────────────────────────────
    if label == "Uncertain":
        colour = (100, 100, 100)   # grey
        text   = f"Uncertain ({confidence:.0%})"
    else:
        colour = (0, 220, 100)     # green
        text   = f"{label}  {confidence:.0%}"

    cv2.putText(
        frame, text,
        org=(16, h - 18),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=1.2,
        color=colour,
        thickness=2,
        lineType=cv2.LINE_AA,
    )

    # ── Confidence bar ───────────────────────────────────────────────────────
    bar_width = int(w * confidence)
    cv2.rectangle(frame, (0, h - banner_h - 6), (bar_width, h - banner_h), colour, thickness=-1)

    return frame


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # 1. Check files exist before trying to load them
    for path in (MODEL_FILE, LABELS_FILE):
        if not os.path.exists(path):
            print(f"ERROR: '{path}' not found.")
            print(f"Make sure {MODEL_FILE} and {LABELS_FILE} are in the same folder as this script.")
            sys.exit(1)

    # 2. Load the model
    print("Loading model…")
    try:
        model = load_model(MODEL_FILE, compile=False)
    except Exception as e:
        print(f"ERROR: Could not load model: {e}")
        print("If you see a deprecation warning about .h5 format, it's safe to ignore.")
        sys.exit(1)

    # 3. Load labels
    labels = load_labels(LABELS_FILE)
    print(f"Classes: {labels}")

    # 4. Open webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("ERROR: Could not open webcam.")
        print("Try changing cv2.VideoCapture(0) to cv2.VideoCapture(1) in this script.")
        sys.exit(1)

    print("Webcam open. Press ESC to quit.")

    # 5. Main loop — read frames, classify, display
    while True:
        ret, frame = cap.read()
        if not ret:
            print("ERROR: Lost webcam feed.")
            break

        label, confidence = predict(model, frame, labels)
        frame = draw_overlay(frame, label, confidence)

        cv2.imshow("AI Trash Sorter  (ESC to quit)", frame)

        # ESC key = ASCII 27
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Done.")


if __name__ == "__main__":
    main()


# ══════════════════════════════════════════════════════════════════════════════
# STRETCH GOAL: Tkinter GUI wrapper
# ══════════════════════════════════════════════════════════════════════════════
#
# You built a Tkinter GUI in weeks 7-8. Try asking the AI:
#
# "Wrap this sorter.py in a Tkinter window. Show the webcam feed as a live image
#  label, and display the predicted class name and confidence in large text below.
#  Change the window background colour based on the class:
#  Paper=blue, Plastic=yellow, Compost=green, Trash=red, Uncertain=grey.
#  Use root.after() to update the frame every 30ms without blocking the UI."
#
# Things to read and understand in the AI's answer:
#   - How does it convert an OpenCV frame (numpy array, BGR) to a Tkinter PhotoImage?
#   - Why root.after(30, update) instead of a while loop?
#   - What happens if you forget to call root.after() again inside the update function?
#
# ══════════════════════════════════════════════════════════════════════════════
