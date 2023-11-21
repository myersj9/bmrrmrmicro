import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# User inputs
gender = input("Enter your gender (M/F): ")
weight_lbs = input("Enter your weight in pounds: ")
height_cm = input("Enter your height in cm: ")
age_years = input("Enter your age in years: ")

# Sending data to server
socket.send(gender.encode('utf-8'))
socket.recv()  # Wait for acknowledgment

socket.send(weight_lbs.encode('utf-8'))
socket.recv()  # Wait for acknowledgment

socket.send(height_cm.encode('utf-8'))
socket.recv()  # Wait for acknowledgment

socket.send(age_years.encode('utf-8'))

# Receiving response from server
response = socket.recv()
print("Response from server:", response.decode('utf-8'))
