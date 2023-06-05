# Yeelight Ambient Light Control

This program allows you to control Yeelight bulbs based on the average color of your screen. It provides an ambient awareness effect by adjusting the light color to match the dominant color on your screen.

Razer Synapse, a popular lighting control software, may have issues connecting to Yeelight devices correctly. This program provides an alternative solution for controlling Yeelight bulbs and circumvents the connection problems experienced with Razer Synapse.

## Installation

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone this repository to your local machine:

```git clone https://github.com/pxtrez/yeelight-control.git```

3. Navigate to the project directory:
   ```cd yeelight-control```

4. Install the required Python packages using pip:
   ```pip install -r requirements.txt```

## Usage

1. Ensure that your Yeelight bulbs are connected to the same network as your computer.

2. Run the program by executing the following command:
   ```python ambient.py```

3. The program will continuously monitor your screen and adjust the Yeelight bulbs' color based on the dominant color. The bulb will update its color if the color difference exceeds the specified threshold.

4. To stop the program, press Ctrl+C in the terminal.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please create an issue or submit a pull request to this repository.

## License

This project is licensed under the MIT License.
