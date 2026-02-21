class DigitIdentification:
    def __init__(self):
        pass

    def digitidentification(self):

        import tensorflow
        from tensorflow import keras
        from keras.layers import Dense,Conv2D,Flatten,MaxPooling2D
        from keras import Sequential
        from keras.datasets import mnist


        from keras.datasets import mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = x_train.reshape(60000, 28, 28, 1)/255
        x_test = x_test.reshape(10000, 28, 28, 1)/255

        model = Sequential()

        model.add(Conv2D(28, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 1)))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())

        model.add(Dense(128, activation='relu'))
        model.add(Dense(10, activation='softmax'))



        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=100, batch_size=128, verbose=0)





bc=DigitIdentification()
print(bc.digitidentification())