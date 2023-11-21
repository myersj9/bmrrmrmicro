import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    male_v_female = socket.recv().decode('utf-8')
    # Validate input
    if male_v_female in ['M', 'm', 'F', 'f']:
        print(f"User Entered {male_v_female}")
        socket.send(b"ACK")  # Acknowledge the gender reception

        weight = float(socket.recv()) / 2.205  # Convert weight from lbs to kg
        socket.send(b"ACK")  # Acknowledge the weight reception

        height = float(socket.recv())  # Height in cm
        socket.send(b"ACK")  # Acknowledge the height reception

        age = float(socket.recv())     # Age in years

        # Calculate BMR & RMR for Male or Female
        if male_v_female.upper() == 'M':
            RMR = (weight * 9.99) + (height * 6.25) - (age * 4.92) + 5
            BMR = 88.632 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            RMR = (weight * 9.99) + (height * 6.25) - (age * 4.92) - 161
            BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

        response = f"Your RMR is {RMR}, Your BMR is {BMR}".encode('utf-8')
        socket.send(response)
    else: 
        socket.send(b"Oops! Please enter M or F")
