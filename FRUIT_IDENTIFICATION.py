


class fruitidentification:
    def __init__(self):
        pass




    def data_dir_from_training_zip(self, zip_path: str, extract_root: str) -> str:
        from pathlib import Path
        import zipfile

        zip_path_p = Path(zip_path).expanduser().resolve()
        extract_root_p = Path(extract_root).expanduser().resolve()
        extract_root_p.mkdir(parents=True, exist_ok=True)

        # Extract only if we can't already find a Training folder
        existing_training = list(extract_root_p.rglob("Training"))
        if not existing_training:
            with zipfile.ZipFile(zip_path_p, "r") as zf:
                zf.extractall(extract_root_p)

        training_dirs = list(extract_root_p.rglob("Training"))
        if not training_dirs:
            raise FileNotFoundError(
                f"No `Training` directory found after extracting into: {extract_root_p}"
            )

        # Prefer the shallowest Training folder (usually the correct dataset root)
        training_dir = sorted(training_dirs, key=lambda p: len(p.parts))[0]
        return str(training_dir)


    # ZIP_FILE = "/content/Training.zip"
    # EXTRACT_TO = "/content/Training"

    # DATA_DIR = data_dir_from_training_zip(ZIP_FILE, EXTRACT_TO)
    # print("DATA_DIR:", DATA_DIR)

    # Then plug `DATA_DIR` into your ImageDataGenerator.flow_from_directory(DATA_DIR, ...)

    def fruitiden(self):
        import os
        import numpy as np
        import matplotlib.pyplot as plt
        from tensorflow.keras.preprocessing.image import ImageDataGenerator
        from tensorflow.keras import layers, models
        from tensorflow.keras.optimizers import RMSprop
        from sklearn.metrics import confusion_matrix, classification_report
        # Example usage (macOS)
        ZIP_FILE = "/content/Training.zip"
        EXTRACT_TO = "/content/Training"

        DATA_DIR = self.data_dir_from_training_zip(ZIP_FILE, EXTRACT_TO)
        # DATA_DIR = r"/content/Training"
        IMG_SIZE = 100
        BATCH_SIZE = 32
        EPOCHS = 30
        TEST_SPLIT = 0.3
        MODEL_PATH = "models/fruits_cnn.keras"

        # Rescale pixel values to [0,1] and split into train/test via validation_split
        datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=TEST_SPLIT)
        # Training generator (70%)
        train_generator = datagen.flow_from_directory(DATA_DIR, target_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
                                                      class_mode='categorical', subset='training', shuffle=True)
        # Testing generator (30%)
        test_generator = datagen.flow_from_directory(DATA_DIR, target_size=(IMG_SIZE, IMG_SIZE), batch_size=BATCH_SIZE,
                                                     class_mode='categorical', subset='validation', shuffle=False)
        num_classes = train_generator.num_classes
        print("Number of classes (output units):", num_classes)
        print("Class indices:", train_generator.class_indices)

        model = models.Sequential()
        # Input layer: Conv2D
        model.add(layers.Conv2D(filters=16, kernel_size=(2, 2), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        # Second Conv block
        model.add(layers.Conv2D(filters=32, kernel_size=(2, 2), activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        # Two Conv layers with 64 filters + pooling
        model.add(layers.Conv2D(filters=64, kernel_size=(2, 2), activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        model.add(layers.Conv2D(filters=64, kernel_size=(2, 2), activation='relu'))
        model.add(layers.MaxPooling2D(pool_size=(2, 2)))
        # Dropout 0.3
        model.add(layers.Dropout(0.3))
        # Flatten
        model.add(layers.Flatten())
        # Fully connected layer
        model.add(layers.Dense(150, activation='relu'))
        model.add(layers.Dropout(0.4))
        # Output layer: softmax over num_classes
        model.add(layers.Dense(num_classes, activation='softmax'))
        model.summary()

        model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', metrics=['accuracy'])
        history = model.fit(train_generator, epochs=EPOCHS, validation_data=test_generator)
        model.save(MODEL_PATH)
        print(f"Model saved to {MODEL_PATH}")

        test_loss, test_acc = model.evaluate(test_generator, verbose=0)
        print(f"\nTest accuracy: {test_acc:.4f}")

        y_true = test_generator.classes  # integer class indices
        # Predicted probabilities
        y_pred_prob = model.predict(test_generator)
        y_pred = np.argmax(y_pred_prob, axis=1)
        # Confusion matrix
        cm = confusion_matrix(y_true, y_pred)
        print("\nConfusion Matrix:")
        print(cm)
        # classification report (precision/recall/F1)
        target_names = list(test_generator.class_indices.keys())
        print("\nClassification Report:")
        print(classification_report(y_true, y_pred, target_names=target_names))

        plt.figure()
        plt.plot(history.history['accuracy'], label='train acc')
        plt.plot(history.history['val_accuracy'], label='test acc')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title('Training vs Test Accuracy')
        plt.figure()
        plt.plot(history.history['loss'], label='train loss')
        plt.plot(history.history['val_loss'], label='test loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.legend()
        plt.title('Training vs Test Loss')
        plt.show()


bc = fruitidentification()
print(bc.fruitiden())
