from keras.models import Sequential
from keras.layers import Dense
import numpy
# fix random seed for reproducibility
numpy.random.seed(4)
# load pima indians dataset
# getting data from snake game 
datasetx1 = numpy.loadtxt("snakeDataX+.txt", delimiter=",")
datasetx1 = numpy.split("snakeDataX+.txt")
datasetx2 = numpy.loadtxt("snakeDataX-.txt", delimiter=",")
datasetx2 = numpy.split("snakeDataX-.txt")
datasety1 = numpy.loadtxt("snakeDataY+.txt", delimiter=",")
datasety1 = nupmy.split("snakeDataY+.txt")
datasety2 = numpy.loadtxt("snakeDataY-.txt", delimiter=",")
datasety2 = nupmy.split("snakeDataY-.txt")
# split into input (X) and output (Y) variables
X = datasetx1, datasetx2
Y = datasety1, datasety2

# create model
model = Sequential()
model.add(Dense(4, input_dim=4, activation='linear'))
model.add(Dense(25, activation='relu'))
model.add(Dense(1, activation='linear'))
'''
def model(self):
    #sets up neural network
    network = input_data(shape=[None, 4, 1], name='input')
    network = fully_connected(network, 1, activation='linear')
    #network = regression(network, optimizer='adam', learning_rate=self.lr, loss='mean_square', name='target')
    model = tflearn.DNN(network, tensorboard_dir='log')
    return model
'''
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=500, batch_size=25)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))