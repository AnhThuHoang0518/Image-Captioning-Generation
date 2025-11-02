# SUGGEST FOR IMPROVEMENT
## 🧪 DATA AUGMENTATION (Train Only)

- Objective: Improve generalization and reduce overfitting without introducing data leakage.
- When: After the train/test split; applied only to training images.
- Augmentation factor: 1–3 augmented variants per original training image (keep the original as well).
- Transforms (recommended):
  - Horizontal flip (p=0.5)
  - Rotation: ±10–20°
  - Width/height shift: up to 10%
  - Shear: 0.1–0.2
  - Zoom: 0.9–1.1
  - Brightness: [0.8, 1.2] (optional)
  - Channel shift: 0–20 (optional)
  - Random crop + resize back to input size (optional)
- Reproducibility: Set and log a random seed.
- Captions: Reuse the same captions for augmented images; do not alter text.
- Storage & mapping:
  - Save augmented images to a separate folder (e.g., data/train_aug/).
  - Naming convention: <image_id>__aug<N>.jpg (e.g., 12345__aug1.jpg).
  - Maintain a JSON/CSV mapping file linking augmented filenames to their original image_id.
- Feature extraction: Extract CNN features for train(original + aug) and test(original only).
- Notes: Avoid vertical flips if they distort scene semantics; keep augmentation moderate to preserve caption relevance.

Example (Keras ImageDataGenerator):

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, array_to_img, load_img
import numpy as np
import os, json, random

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    brightness_range=(0.8, 1.2),
    channel_shift_range=20,
    fill_mode="nearest"
)

in_dir = "data/train"
out_dir = "data/train_aug"
os.makedirs(out_dir, exist_ok=True)

augmentation_factor = 2  # 1–3 recommended
mapping = {}

for fname in os.listdir(in_dir):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    img_path = os.path.join(in_dir, fname)
    img = load_img(img_path)
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)

    base_id = os.path.splitext(fname)[0]
    # Always keep the original image
    mapping[fname] = {"original_id": base_id, "aug": 0}

    i = 0
    for batch in datagen.flow(x, batch_size=1, seed=SEED):
        i += 1
        out_name = f"{base_id}__aug{i}.jpg"
        array_to_img(batch[0]).save(os.path.join(out_dir, out_name))
        mapping[out_name] = {"original_id": base_id, "aug": i}
        if i >= augmentation_factor:
            break

with open(os.path.join(out_dir, "aug_mapping.json"), "w") as f:
    json.dump(mapping, f, indent=2)
```

---

## 📋 **NEW PIPELINE WORKFLOW**

| Step | Description | Status | Changes & Rationale |
|------|-------------|--------|---------------------|
| 1 | **Train/Test Split** | 🔄 In Progress | **MOVED TO EARLY** - Split image IDs before augmentation to prevent data leakage |
| 2 | **Load Captions** | ✅ No Change | Read captions.txt → image_to_captions_mapping (40,455 captions / 8,091 images) |
| 3 | **Preprocessing Captions** | ✅ No Change | Clean text + add startseq/endseq tokens |
| 4 | **Tokenization & Vocabulary** | 🔄 To Update | **FIT ONLY ON TRAINING** captions to avoid data leakage |
| 5 | **Data Augmentation (Train Only)** | 🔄 To Update | **TRAIN SET ONLY** - Use ImageDataGenerator for augmentation_factor=1-3 |
| 6 | **Feature Extraction** | 🔄 To Update | **MOVED AFTER AUGMENTATION** - Extract features for train(original+aug) + test(original) |
| 7 | **Data Generator** | ✅ No Change | Generate batches (image_feature, in_seq) → out_seq |
| 8 | **Model Training (GRU)** | 🔄 To Update | Switched from BiLSTM to GRU to reduce parameters and speed up training with comparable performance |
| 9 | **Evaluation (BLEU)** | ✅ No Change | BLEU-1, BLEU-2 on test set |



## 🧠 **ARCHITECTURE UPDATE DETAILS (BiLSTM → GRU)**

- Rationale:
  - Fewer parameters than BiLSTM for the same hidden size.
  - Faster training and lower memory usage.
  - Maintains comparable captioning quality in practice.

- Key changes in decoder:
  - Replace Bidirectional LSTM layers with single-direction GRU.
  - Keep attention mechanism unchanged.


## 📊 **DATA FLOW COMPARISON**

### 🔴 **ORIGINAL FLOW (Has Data Leakage)**
```
1. Load Images → Extract Features (ALL)
2. Load Captions → Process ALL captions  
3. Augment ALL images → Mixed train/test
4. Tokenize ALL captions → Data leakage
5. Split → Too late, leakage already occurred
6. Train → Contaminated data
```

### ✅ **NEW FLOW (No Data Leakage)**
```
1. Load Captions → Split Image IDs (train_ids/test_ids)
2. Tokenize ONLY training captions → No leakage  
3. Augment ONLY train_ids → Clean separation
4. Extract Features: train(orig+aug) + test(orig only)
5. Train (GRU) → Clean training data
6. Evaluate → Unbiased test results
```