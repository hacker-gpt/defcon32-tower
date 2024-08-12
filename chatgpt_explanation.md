Understanding the Script and How the Devices Interact

Overview:

The script is designed to control a set of towers, each equipped with lights (NeoPixels), keypads, OLED displays, and a LoRa module for communication. The towers can display different light patterns (“shows”) based on user input via the keypads or commands received from other towers through the LoRa network. Each tower can operate independently or be controlled remotely by another tower, depending on certain codes and sequences entered by the user.

Key Components:

	•	NeoPixels: Addressable RGB LEDs that can display various light patterns and colors.
	•	Keypad: A numeric keypad used to input commands or select different modes/shows.
	•	OLED Display: A small screen that displays text, graphics, and feedback to the user.
	•	LoRa Module (RYLR896): A communication module that allows towers to send and receive messages over a wireless network.

Modes and Interactions:

	1.	Tower Number Setup:
	•	Upon startup, the tower asks the user to set a tower number via the keypad. This number identifies the tower within the network.
	•	The number is displayed on the OLED screen.
	2.	Control Mode:
	•	Towers can be in two states: In Control or Not in Control.
	•	The “In Control” tower can change the current light show, send commands to other towers, and control their displays.
	•	A “take over code” can be entered on any tower not in control to seize control from the current controlling tower.
	3.	Admin Mode:
	•	An administrator can enter a special sequence on the keypad to access advanced settings:
	•	Change Tower Number: Allows the admin to reset the tower number.
	•	Set LoRa Parameters: Lets the admin change the communication settings for the LoRa module.
	•	Toggle Control: Enables or disables the tower’s control mode.
	4.	Show Selection:
	•	Users can select different light shows using the keypad. The show selection is influenced by whether the tower is in control or following commands from another tower.
	•	If the tower is in control, it can set its own show and send the command to others.
	5.	LoRa Communication:
	•	Towers communicate with each other using the LoRa module. A controlling tower can send the current show and control status to other towers.
	•	When a message is received, the tower will update its show or control status accordingly.

Simple User Manual

1. Setting Up the Tower

	•	Power On: Once the tower is powered on, the OLED screen will prompt you to set the tower number.
	•	Setting Tower Number:
	•	Use the keypad to enter the tower number (1-9). Press * for 10, 0 for 11, and # for 12.
	•	The selected number will be displayed on the OLED screen.

2. Operating the Tower

	•	In Control Mode:
	•	The tower in control can change the light show by pressing the corresponding number on the keypad.
	•	The tower will display the current sequence and show on the OLED screen.
	•	The chosen show will be sent to all other towers via the LoRa network.
	•	Not in Control Mode:
	•	If the tower is not in control, it will follow the commands sent from the controlling tower.
	•	The OLED will display the incoming command or show name.
	•	Users can attempt to take control by entering the “take over code” (a sequence displayed when control is first established).

3. Admin Mode

	•	Entering Admin Mode:
	•	Press a special sequence on the keypad to access admin functions (sequence not explicitly provided in the script; assumed to be stored in the take_over_code variable).
	•	Admin Options:
	•	1: Set a new tower number.
	•	2: Adjust LoRa communication parameters.
	•	3: Toggle the control mode (gain or relinquish control).

4. Light Shows

	•	Each number on the keypad corresponds to a different light show or display pattern.
	•	Available shows may include effects like shimmering, twinkling, or special animations (exact shows are not listed in detail).

5. Communication with Other Towers

	•	Towers communicate automatically using the LoRa module.
	•	When a show is selected, the current tower broadcasts the command to others.
	•	If a tower receives a command from another, it will update its display and lighting accordingly.

Troubleshooting

	•	OLED Not Displaying: Ensure the device is properly connected and powered. Check the I2C address if the OLED does not initialize.
	•	Keypad Input Not Registering: Confirm that the keypad is correctly wired and try pressing the keys firmly. If issues persist, check for hardware faults.
	•	LoRa Communication Issues: Verify that the LoRa parameters are correctly set in admin mode. Ensure that the towers are within range (up to 50 feet).

This manual provides basic instructions for using and interacting with the towers. For more complex setups or additional features, refer to the script or contact the system administrator.
Apollo
