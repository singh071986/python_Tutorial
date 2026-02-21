


class catogioricalidenti:
    def __init__(self):
        pass

    def catgident(self):

        import tensorflow
        from tensorflow import keras
        from keras.layers import Dense,Conv2D,Flatten,MaxPooling2D,Dropout
        from keras import Sequential
        from keras.datasets import mnist

        from keras.datasets import cifar100
        (x_train, y_train), (x_test, y_test) = cifar100.load_data()

        x_train = x_train.astype('float32') / 255
        x_test = x_test.astype('float32') / 255

        from keras.utils import to_categorical
        y_train = to_categorical(y_train, 100)
        y_test = to_categorical(y_test, 100)

        model = Sequential()

        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)))
        model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # A Dropout layer with 0.25 rate
        model.add(Dropout(0.25))
        model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # A Dropout layer with 0.25 rate
        model.add(Dropout(0.25))

        model.add(Flatten())

        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.25))
        model.add(Dense(100, activation='softmax'))

        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=100, batch_size=32)

        loss, accuracy = model.evaluate(x_test, y_test)


        return loss, accuracy




bc=catogioricalidenti()
print(bc.catgident())
