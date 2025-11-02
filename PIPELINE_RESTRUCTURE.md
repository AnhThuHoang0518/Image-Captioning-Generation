# SUGGEST FOR IMPROVEMENT
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



