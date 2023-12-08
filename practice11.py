'''class Vehicle():
    def __init__(self , brand , model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14

vehicle_object = Vehicle('Honda','truck', 'Mini')
print(vehicle_object.type)'''
""" class Parent():
    def First():
        print("First")

class Child(Parent):
    def Second():
        print("Second")

obj = Child()
obj.First()
obj.Second() """
'''import mysql.connector
mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Rahul@0603"
        )
mycursor = mydb.cursor()
#mycursor.execute("create database practise")
mycursor.execute("use train_jarvis")
mycursor.execute("select * from robo_commands")
output = mycursor.fetchall()
for x in output:
    print(x[1])'''
'''import keyboard


if keyboard.read_key()=='b':
    print("Ola")
elif keyboard.read_key()=='n':
    exit(0)
'''
'''from tensorflow import keras
from keras.applications.mobilenet_v2 import preprocess_input
'''
'''import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
  '''
