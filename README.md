# bmrrmrmicro

Description
This microservice calculates the Basal Metabolic Rate (BMR) and Resting Metabolic Rate (RMR) based on the user's gender, weight, height, and age.

Endpoints
TCP Socket: tcp://*:5555 (Server), tcp://localhost:5555 (Client)
Protocol
ZeroMQ (ZMQ) with REQ/REP pattern
Request Format
Gender

Type: String
Accepted Values: "M", "m", "F", "f"
Description: User's gender. "M" or "m" for male, "F" or "f" for female.
Weight

Type: String (to be converted to float)
Unit: Pounds (lbs)
Description: User's weight. The server will convert this value to kilograms.
Height

Type: String (to be converted to float)
Unit: Centimeters (cm)
Description: User's height in centimeters.
Age

Type: String (to be converted to float)
Unit: Years
Description: User's age in years.
Response Format
Success Response:

Type: String
Content: "Your RMR is [RMR_VALUE], Your BMR is [BMR_VALUE]"
Description: The calculated Resting Metabolic Rate (RMR) and Basal Metabolic Rate (BMR) are returned in the response.
Error Response:

Type: String
Content: "Oops! Please enter M or F"
Description: This response is sent if the gender input is not one of the accepted values.
Error Handling
If the gender input is not "M", "m", "F", or "f", the server responds with an error message and does not proceed with further calculations.
Notes
The client must send each piece of data (gender, weight, height, age) sequentially and wait for an acknowledgment after each send before proceeding to the next piece of data.
The server expects data in the specific order: gender, weight, height, and then age.
Weight is converted from pounds to kilograms on the server side.
The client and server communicate using the ZeroMQ (ZMQ) library, which requires the client to send a request (REQ) and the server to reply (REP) in a synchronous request-reply pattern.
Version
Microservice Version: 1.0
Last Updated: [11/20/2023]

<img width="758" alt="Screenshot 2023-11-20 at 8 05 00 PM" src="https://github.com/myersj9/bmrrmrmicro/assets/114433777/6bd7235e-0bf5-403c-aff3-24b4efabb73e">
