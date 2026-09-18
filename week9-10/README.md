# Weeks 9-10: Building an AI Trash Sorter

You're going to train your own image-recognition model with **zero code**, then use an
AI coding tool to write the Python app that runs it live on your webcam.
Like week 7-8, you'll build in **small steps** — each step is a short prompt, not one
giant one. At each step you'll see what the AI commonly gets wrong and how to catch it.

## The 2-week build

| Week | You build | New idea |
|------|-----------|----------|
| 9 | Train an image-recognition model in Teachable Machine (zero code) | What training actually means — and how bad data breaks a model |
| 10 | A Python app that classifies your webcam feed live | Loading a model you trained; iterative prompting when AI gets it wrong |

---

## Before You Start

```bash
pip install opencv-python tensorflow numpy
```

> ⚠️ TensorFlow is ~500 MB. Start the install now if you're on a slow connection.
> ⚠️ Python 3.8–3.11 works best. On 3.12+ ask your instructor if you hit install errors.

---

## Week 9: Train Your Model (no coding)

Go to **[teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/)** — no account needed.

**Steps:**
1. Click **Get Started** → **Image Project** → **Standard Image Model**
2. Create 4 classes: `Paper`, `Plastic`, `Compost`, `Trash`
3. For each class, capture **30–50 photos** using your webcam — different angles, backgrounds, lighting
4. Click **Train Model**
5. Test it in the browser — hold up objects and see what it predicts
6. **Export Model** → TensorFlow tab → Keras → Download
7. Unzip — you'll have `keras_Model.h5` and `labels.txt`

> ⚠️ **Common training mistakes — and why they matter:**
>
> | Mistake | What goes wrong |
> |---------|----------------|
> | Fewer than 20 photos per class | Model is always "Uncertain" — not enough examples to learn from |
> | All photos against the same wall | Model learns the wall colour, not the object — fails anywhere else |
> | Unbalanced classes (50 Paper, 10 Plastic) | Model favours Paper — it learned "when in doubt, say Paper" |
> | Blurry or far-away photos | Model can't see the details that distinguish the classes |
>
> This is the same idea as test data in code: garbage in, garbage out.
> If your model is wrong in the browser, fix the training data — not the Python code.

**Do this — don't just click Train once and move on:**
1. Train with ~15 photos per class. Test in the browser. Write down which class confuses it most.
2. Add 20 more photos for that class: different backgrounds, different lighting, different angles.
3. Re-train. Did it improve? Ask yourself: *why* did more varied photos help?

**Checkpoint before Week 10:**
- [ ] You have `keras_Model.h5` and `labels.txt` in a project folder
- [ ] The browser test correctly identifies at least 3 of your 4 classes
- [ ] You know which class it struggles with most, and why
- [ ] You can explain in one sentence what "training" did to the model

---

## Week 10: Build the App — 4 Steps

Put `keras_Model.h5`, `labels.txt`, and your Python script in the **same folder**.

> **Rule:** finish and verify each step before moving to the next.
> Don't paste all 4 prompts at once.

---

### Step 1 — Load the model and classify one image

**Prompt:**
> "Write a Python script that loads a Teachable Machine Keras model from keras_Model.h5
> using `tf.keras.models.load_model('keras_Model.h5', compile=False)`.
> Read class labels from labels.txt (each line is '0 ClassName' — strip the number).
> Take one frame from the webcam, close the webcam immediately, and print
> the predicted class and confidence for that single frame. Don't open any window yet."

**When you get the code:**
- Run it. Does it print a class name and a number between 0 and 1?
- Hold up a piece of paper when it captures. Does the prediction seem right?

> ⚠️ **Common AI mistakes at this step:**
>
> **Mistake 1 — wrong import:**
> The AI often writes `from keras.models import load_model` (standalone Keras).
> This may not be installed. The correct import for Teachable Machine models is:
> `from tensorflow.keras.models import load_model` or `import tensorflow as tf` then `tf.keras.models.load_model(...)`.
>
> **Mistake 2 — missing `compile=False`:**
> Without it you'll get a warning or error about the optimiser config.
> If the AI forgets it, add `compile=False` to the `load_model` call yourself.

**Move to Step 2 when:** you see a class name printed without errors.

---

### Step 2 — Open a live webcam loop

**Prompt:**
> "Update the script to open a webcam loop with `cv2.VideoCapture(0)`.
> For each frame, display it in a window using `cv2.imshow`.
> Press ESC to quit. After the loop, release the webcam and destroy all windows.
> Don't add classification yet — just confirm the live feed works."

**When you get the code:**
- Run it. Does your webcam feed appear in a window?
- Press ESC. Does the window close cleanly?

> ⚠️ **Common AI mistakes at this step:**
>
> **Mistake 1 — not checking the return value of `cap.read()`:**
> `cap.read()` returns `(ret, frame)`. If `ret` is False, the webcam dropped a frame.
> If the AI ignores `ret` and uses `frame` directly, the app will crash randomly.
> Check: does the code have `if not ret: break` (or similar)?
>
> **Mistake 2 — forgetting `cap.release()` and `cv2.destroyAllWindows()`:**
> Without these, the webcam light stays on after you press ESC and the window may freeze.
> Check that both are called after the loop ends.

**Move to Step 3 when:** the webcam feed opens, runs smoothly, and closes cleanly with ESC.

---

### Step 3 — Classify each frame

**Prompt:**
> "Now add classification to each frame:
> Resize the frame to 224×224, convert BGR to RGB, normalise pixel values with
> `(image / 127.5) - 1.0` (NOT / 255), add a batch dimension with np.expand_dims,
> run it through the model with model.predict(), and find the class with the
> highest confidence using np.argmax."

**When you get the code:**
- Run it. Hold up a piece of paper — what does it predict?
- Check the terminal for any shape errors.

> ⚠️ **This is the most common mistake in this whole project:**
>
> **Mistake — wrong normalisation:**
> Almost every AI will write `image / 255.0` — that normalises to [0, 1].
> Teachable Machine models expect [-1, 1], which requires `(image / 127.5) - 1.0`.
> The code won't crash with the wrong normalisation, but predictions will be wrong.
> The model will seem confident but output the same class for everything.
> How to catch it: try different objects — if it always predicts the same class, normalisation is the bug.
> Fix: change `/ 255.0` to `/ 127.5 - 1.0` (or `/ 127.5) - 1.0` with correct brackets).
>
> **Also check:** does the AI call `np.expand_dims(image, axis=0)`?
> The model expects shape `(1, 224, 224, 3)` — the `1` is the batch dimension.
> Without it you'll get a shape error immediately.

**Move to Step 4 when:** different objects give different predictions in the terminal.

---

### Step 4 — Show the result on screen

**Prompt:**
> "Overlay the predicted class and confidence percentage on the video frame using
> `cv2.putText`. Only show the prediction if confidence is above 70% — otherwise
> show 'Uncertain'. Display in the bottom-left corner of the frame with a dark
> background banner behind the text so it's readable against any background.
> If the webcam can't open, print a clear error message and exit.
> If keras_Model.h5 or labels.txt can't be found, print a clear error message and exit."

**When you get the code:**
- Run it. Is the text readable on different backgrounds?
- Cover the webcam — does it say "Uncertain"?
- Test all 4 classes.

> ⚠️ **Common AI mistakes at this step:**
>
> **Mistake 1 — text placed at (0, 0):**
> OpenCV text position is the *bottom-left* of the text. Position (0, 0) puts text off the top of the frame.
> If text is invisible, try changing the y-coordinate to something like `frame.shape[0] - 20` (near the bottom).
>
> **Mistake 2 — no handling for the "Uncertain" case:**
> The AI sometimes writes the confidence check but still passes an index to `labels[]`
> even when confidence is low, meaning you get a low-confidence label displayed as if it's confident.
> Check: when confidence < 0.70, does the code show "Uncertain" — or does it still show a label?

**Week 10 checkpoint — you're done when:**
- [ ] All 4 classes are correctly identified when held up clearly
- [ ] Low-confidence objects show "Uncertain" — not a wrong label confidently stated
- [ ] You can explain why `(image / 127.5) - 1.0` and not `/ 255.0`
- [ ] You can trace one frame from webcam capture to text on screen

---

### Stretch Goal — Tkinter GUI

You built a Tkinter GUI in weeks 7–8. Ask the AI:

> "Wrap this in a Tkinter window. Show the webcam feed as a live image label using PIL/Pillow.
> Display the predicted class in large text below it.
> Change the window background colour based on class:
> Paper=blue, Plastic=yellow, Compost=green, Trash=red, Uncertain=grey.
> Use `root.after(30, update)` to update the frame every 30ms."

Things to understand in the AI's answer:
- How does it convert an OpenCV frame (numpy BGR) to a Tkinter image? (Hint: PIL)
- Why `root.after(30, update)` instead of a `while` loop?
- What happens if `update()` forgets to call `root.after()` again at the end?

---

## Reference File

`sorter.py` in this folder is a reference implementation.
Build your own with the prompts above first.
Compare line by line if you're stuck — don't just copy it.

---

## Common Issues

| Problem | Likely cause | Fix |
|---------|-------------|-----|
| `ModuleNotFoundError: tensorflow` | Not installed | `pip install tensorflow` |
| `ModuleNotFoundError: cv2` | Not installed | `pip install opencv-python` |
| TF install fails on Python 3.12+ | Limited support | Use Python 3.10 or 3.11 |
| `FileNotFoundError: keras_Model.h5` | Wrong folder | Put model files in the same folder as your script |
| Camera won't open | Permissions or wrong index | Try `cv2.VideoCapture(1)`; check System Settings → Privacy → Camera |
| Always predicts same class | Wrong normalisation | Change to `(image / 127.5) - 1.0` |
| `.h5 deprecation warning` | TF 2.12+ warns about old format | Safe to ignore |

---

## Push Your Work

```bash
git add .
git commit -m "Week 9/10 - trained model + webcam classifier"
git push
```

> Don't push `keras_Model.h5` — it can be 50–200 MB.
> Add it to `.gitignore`:
> ```
> echo "keras_Model.h5" >> .gitignore
> ```
