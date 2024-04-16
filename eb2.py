from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from PIL import ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES=True
import keras.backend as K


def get_f1(y_true, y_pred): #taken from old keras source code
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    f1_val = 2*(precision*recall)/(precision+recall+K.epsilon())
    return f1_val




im_shape=(200,200)
traindata ='D:\\st\\eyebrow\\train'    
testdata ='D:\\st\\eyebrow\\test'       
seed = 10
BATCH_SIZE=32


data_generator = ImageDataGenerator(rescale=1./255, validation_split=0.2)
val_data_generator = ImageDataGenerator( rescale=1./255, validation_split=0.2)


#Generator data train
train_generator=data_generator.flow_from_directory(traindata, target_size=im_shape, shuffle=True, seed=seed,class_mode="categorical",batch_size=BATCH_SIZE,subset="training")
#Generator data validation
validation_generator=val_data_generator.flow_from_directory(traindata,target_size=im_shape,shuffle=False,seed=seed,class_mode='categorical',batch_size=BATCH_SIZE,subset="validation")
              
#Generator data test
test_generator=ImageDataGenerator(rescale=1./255)
test_generator=test_generator.flow_from_directory(testdata,target_size=im_shape,shuffle=False,seed=seed,class_mode="categorical",batch_size=BATCH_SIZE)
nb_train_samples=train_generator.samples
nb_validation_samples=validation_generator.samples 
nb_test_samples=test_generator.samples
classes=list(train_generator.class_indices.keys())
print(str(classes))
num_classes=len(classes)



eb_model=Sequential()
eb_model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=(im_shape[0],im_shape[1],3)))
eb_model.add(MaxPooling2D(pool_size=(2,2)))
eb_model.add(Conv2D(64,kernel_size=(3,3),activation='relu'))
eb_model.add(MaxPooling2D(pool_size=(2,2)))
eb_model.add(Conv2D(128,kernel_size=(3,3),activation='relu'))
eb_model.add(MaxPooling2D(pool_size=(2,2)))
eb_model.add(Flatten())
eb_model.add(Dense(256,activation='relu'))
eb_model.add(Dropout(0.2))
eb_model.add(Dense(num_classes,activation='sigmoid'))
eb_model.compile(loss=['binary_crossentropy', 'mae'], optimizer='adam', metrics=[get_f1])
eb_model.summary()



history_eb=eb_model.fit(train_generator,steps_per_epoch=nb_train_samples // BATCH_SIZE,epochs=5,validation_data=validation_generator,verbose=1,validation_steps=nb_validation_samples // BATCH_SIZE)

eb_model.save("eb-30e.h5")