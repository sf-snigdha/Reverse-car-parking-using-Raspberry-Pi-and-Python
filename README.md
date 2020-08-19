# Reverse-car-parking-using-Raspberry-Pi-and-Python

The aim of this project is to design a Reverse Car Parking System commanded by a Raspberry Pi that enables cars to be parked on the designated parking area. My system aims to reduce the human intervention to the minimal by making process smart of car parking.


Project Idea
To develop a reverse car parking system using Raspberry Pi which will
• Detect free parking spot with ultrasonic
• take a 90 degree turn
• Reverse park itself



Equipments
• Raspberry pi board,
• HC-SR04 Ultrasonic Distance Sensor,
• D.C. Motors (X2),
• Wheels (X2),
• Caster wheel / Omni wheel ,
• Led (X3),
• Some Resistors,
• Jumper Wires,
• Breadboard / Explorer-hat,
• Mu / PyCharm,
• Buzzer.



### Empty Slot Detection
Empty Slot Detection is done using Ultrasound Sensor if there is any slot empty in the parking system . Ultrasonic sensors transmit sound waves between 25 kHz and 50 kHz. They use the reflected energy to analyze and detect the status of a parking space. Ultrasonic waves are emitted from the head of an ultrasonic vehicle detection sensor every 60 milliseconds, and the presence or absence of vehicles is determined by time differences between the emitted and received signals. When ultrasonic waves are incident on the object, diffused reflection of the energy takes place over a wide solid angle which might be as high as 180 degrees. Thus some fraction of the incident energy is reflected back to the transducer in the form of echoes and is detected.

Hardware needed: Ultrasound Sensor, toy car, Raspberry Pi
Skills: Programming in Python



### Take a 90 degree turn
As soon as empty slot is detected, the car will stop .Then it will take a 90 degree turn in the reverse direction towards the spotted area. This is done using 1 steering motor and 2 driving motor.

Hardware needed: Steering motor, Driving motors, Toy Car, Breadboard, Jumper Cables, Potentiometer.
Skills: Programming in Python



### Reverse parking
After turning 90 degree the car will get a feedback from the ultrasound sensor to stop and it will park itself on the spotted area. Once the algorithm determines the parking space length is long enough, the car will take a 90 degree turn. We used DC motors to drive and turn the car. The basic principle of the DC motor is that the conductor experiences torque and mechanical motion in the presence of magnetic field. The direction of rotation is proportional to the direction of current as when the current is reversed, the direction of rotation would also be reversed. The speed of the motor is proportional to the force.
the car will get a feedback from the ultrasound sensor to stop . All the mototrs will stop and the car will park itself on the spotted area.
Hardware needed: Ultrasound Sensor ,Steering motor, Driving motors, Toy Car, Jumper cables
Skills: Programming in Python
