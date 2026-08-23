# Weeks 9-10: Building an AI Trash Sorter

Project: https://github.com/mathandcodingacademy/ai-trash-sorter

You're going to train your own AI model with no code at all, then use an AI
coding tool to write the Python program that runs it live on your webcam.

## The 2-week build

| Week | You build | New idea |
|---|---|---|
| 9 | Train an image-recognition model in Teachable Machine (zero code) | What "training a model" actually means: examples in, patterns learned |
| 10 | A Python app that loads your model and classifies your webcam feed live | Using AI to write code around something YOU trained, not something the AI made up |

---

## Week 9: Train your model (no coding)

Go to **[teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/)**: no account needed.

**Steps:**
1. Click **Get Started** → **Image Project** → **Standard Image Model**
2. Create 4 classes: `Paper`, `Plastic`, `Compost`, `Trash`
3. For each class, use your webcam to capture 30-50 photos of that kind of item: different angles, different backgrounds, different lighting
4. Click **Train Model** and watch it train
5. Test it right there in the browser: hold up an item and see if it guesses correctly
6. Click **Export Model** → **TensorFlow** tab → **Keras** → **Download my model**
7. You'll get a `.zip` with `keras_Model.h5` and `labels.txt`: these are YOUR trained model files, not code anyone wrote

**Think about this while you're capturing photos:**
- What happens if you only take photos of paper in bright light, but someone tests it in a dark room?
- What happens if two classes look really similar (like white paper and white plastic)?
- This is the same idea as a test in `unittest`: the model is only as good as the examples ("tests") you gave it. Bad or narrow examples = bad predictions later.

**Checkpoint before Week 10:**
- [ ] You have `keras_Model.h5` and `labels.txt` downloaded
- [ ] You tested your model in the browser and it correctly identified at least 3 of your 4 classes
- [ ] You can explain, in one sentence, what "training" did: it looked at your labeled photos and learned to tell them apart

---

## Week 10: Build the app with AI

**Setup first:**
1. Create a project folder, put `keras_Model.h5` and `labels.txt` in it
2. `pip install opencv-python tensorflow numpy`

**Prompt to give the AI:**
> "Write a Python script that loads a Teachable Machine Keras model
> (keras_Model.h5) and its labels.txt, opens the webcam with OpenCV, and for
> each frame: resizes it to 224x224, runs it through the model, and shows the
> predicted class and confidence percentage as text overlay on the video.
> Only show a prediction if confidence is above 70%. Press ESC to quit."

**Do this, don't just run it and walk away:**
1. Run it. Hold up real objects (or your captured photos) and check: does it match what you saw work in the Teachable Machine browser test?
2. Find the line that resizes the frame to `224x224`. Ask the AI: "why 224x224 specifically, and what breaks if I skip this step?" (Answer: the model was trained expecting that exact size: feed it a different size and the prediction is meaningless, even though the code won't crash.)
3. Find the confidence threshold (`0.70`). Change it to `0.30`, run it again, and watch what happens when the AI gets unsure. Put it back to `0.70` and explain to your instructor why a low threshold is a problem here.
4. Find where the code normalizes pixel values (`/ 127.5 - 1.0`). You don't need to know the math: but ask the AI in one sentence why raw camera pixels can't go straight into the model.

**Common issues (from the project's own troubleshooting table):**

| Problem | Likely cause |
|---|---|
| `Camera error: could not open webcam` | Webcam permissions, or wrong camera index: try changing `cv2.VideoCapture(0)` to `1` |
| `FileNotFoundError: keras_Model.h5` | Model files aren't in the same folder as the script |
| `ModuleNotFoundError` | Forgot `pip install -r requirements.txt` |

**Checkpoint: you should be able to say, honestly:**
- [ ] "I trained this model myself and I know what good vs. bad training data looks like"
- [ ] "I know why the image gets resized and normalized before the model sees it"
- [ ] "I tested what happens when confidence is low, on purpose"

---

## Push your work

```bash
git add .
git commit -m "Week 9/10 - trained model + webcam classifier"
git push
```

Don't push `keras_Model.h5` if it's large and your instructor hasn't set up
Git LFS: ask first if you're not sure.
