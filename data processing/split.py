import os
import shutil
import random

random.seed(42)

SRC_DIR = "frames"
DEST_DIR = "data"

splits = {
    "train": 0.7,
    "val": 0.2,
    "test": 0.1
}

classes = ["full", "empty"]

for split in splits:
    for cls in classes:
        os.makedirs(os.path.join(DEST_DIR, split, cls), exist_ok=True)

for cls in classes:
    class_dir = os.path.join(SRC_DIR, cls)
    images = [f for f in os.listdir(class_dir) if f.lower().endswith((".jpg", ".png"))]

    random.shuffle(images)

    n_total = len(images)
    n_train = int(n_total * splits["train"])
    n_val   = int(n_total * splits["val"])

    train_files = images[:n_train]
    val_files   = images[n_train:n_train+n_val]
    test_files  = images[n_train+n_val:]

    for fname in train_files:
        shutil.copy(
            os.path.join(class_dir, fname),
            os.path.join(DEST_DIR, "train", cls, fname)
        )

    for fname in val_files:
        shutil.copy(
            os.path.join(class_dir, fname),
            os.path.join(DEST_DIR, "val", cls, fname)
        )

    for fname in test_files:
        shutil.copy(
            os.path.join(class_dir, fname),
            os.path.join(DEST_DIR, "test", cls, fname)
        )

print("Dataset successfully split!")
