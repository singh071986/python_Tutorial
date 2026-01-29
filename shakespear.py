class Shakespeare:
    def __init__(self):
        pass

    def shakesperewordpredict(self):
            ############### Sentiment Analysis using LSTM #################
        from tensorflow.keras import layers, models
        import matplotlib.pyplot as plt

        CSV_PATH="data.txt"
        TEXT_COLUMN = "content"
        LABEL_COLUMN = "sentiment"
        BATCH_SIZE = 256
        EPOCHS = 10

        #df = pd.read_csv(CSV_PATH)

            # Read the text file as separate lines of text
        with open('data.txt', 'r') as file:
                text = file.read()
                lines = text.lower().split('\n')
                # Define words, vocabulary size and sequences of words as lines
        #print(lines)
        from tensorflow.keras.preprocessing.text import text_to_word_sequence, Tokenizer
        words = text_to_word_sequence(text)
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(words)
        vocabulary_size = len(tokenizer.word_index) + 1
        sequences = tokenizer.texts_to_sequences(lines)
            # Find subsequences
        subsequences = []
        for sequence in sequences:
            for i in range(1, len(sequence)):
                subsequence = sequence[:i + 1]
                subsequences.append(subsequence)

        from tensorflow.keras.preprocessing.sequence import pad_sequences
        sequence_length = max([len(sequence) for sequence in sequences])
        print("sequence_length:",sequence_length)
        sequences = pad_sequences(subsequences, maxlen=sequence_length, padding='pre')

        from tensorflow.keras.utils import to_categorical
        x, y = sequences[:, :-1], sequences[:, -1]
        y = to_categorical(y, num_classes=vocabulary_size)

        print("x shape:", x.shape)
        print("y shape:", y.shape)

        model = models.Sequential()
        model.add(layers.Embedding(input_dim=vocabulary_size, output_dim=100, input_length=sequence_length - 1))
        model.add(layers.LSTM(100))
        model.add(layers.Dropout(0.1))
        model.add(layers.Dense(vocabulary_size, activation='softmax'))

        model.summary()
            #
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'] )



        history=model.fit(x, y, epochs=500, verbose=1)
        print(history)
        return history

           # history = model.fit(x, y, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(X_val, y_val))


bc=Shakespeare()
print(bc.shakesperewordpredict())
