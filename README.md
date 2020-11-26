# Parameter_Monitoring

## Libary Installation for MCP3008:

 The MCP3008 is a low cost 8-channel 10-bit analog to digital converter. This chip is a great option if you just need to read simple analog signals
 The MCP3008 connects to the Raspberry Pi using a SPI serial connection. You can use either the hardware SPI bus, or any four GPIO pins and software 
 SPI to talk to the MCP3008.  Software SPI is a little more flexible since it can work with any pins on the Pi, whereas hardware SPI is slightly 
 faster but less flexible because it only works with specific pins.  If you aren't sure which to use I recommend software SPI as it's easier to setup.
 
To install the library from source (recommended) run the following commands on a Raspberry Pi or other Debian-based OS system:
```
sudo apt-get install git build-essential python-dev
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
cd Adafruit_Python_MCP3008
sudo python3 setup.py install
```
Alternatively you can install from pip with:
>sudo pip install adafruit-mcp3008

 ## Enable SPI Interface:
 The default Raspbian image disables SPI by default so before you can use it the interface must be enabled.
 use the graphical tool “Raspberry Pi Configuration”. This is found under **Menu > Preferences > Raspberry Pi Configuration**
 ![Rpi Configuration](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/rpi_config.jpg)
 
 Then you simply need to select the “Interfaces” tab and set SPI to “Enabled” :
 ![Enable](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/enable.png)
 
 Click the “OK” button. If prompted to reboot select “Yes” so that the changes will take effect.
 
 The Raspberry Pi will reboot and the SPI interface will be enabled.
 
## Ultrasonic Sensor:
The HC-SR04 ultrasonic sensor uses SONAR to determine the distance of an object just like the bats do. It offers excellent non-contact range detection with high accuracy and stable readings in an easy-to-use package from 2 cm to 400 cm or 1” to 13 feet.

The operation is not affected by sunlight or black material, although acoustically, soft materials like cloth can be difficult to detect. It comes complete with ultrasonic transmitter and receiver module.

![Ultrasonic Sensor](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/ultrasonic_sensor.jpg)

### Technical Specifications:
* Power Supply − +5V DC
* Quiescent Current − <2mA
* Working Current − 15mA
* Effectual Angle − <15°
* Ranging Distance − 2cm – 400 cm/1″ – 13ft
* Resolution − 0.3 cm
* Measuring Angle − 30 degree

## ACS712 Current Sensor:
![ACS712](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/ACS712-Current-Sensor-Module.jpg)

* Pinout:
![ACS712 Pinout](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/ACS712-Current-Sensor-Pinout.png)

### Specifications:
* Measures both AC and DC current
* Available as 5A, 20A and 30A module
* Provides isolation from the load
* Easy to integrate with MCU, since it outputs analog voltage
* Scale Factor
| 5A module | 20A module | 30A module |
|-- |--|--|
|185mV/Amp | 100mV/Amp | 66mV per Amp |



## Connections:
1. **Ultrasonic Sensor:**

  | Ultrasonic sensor Pin| Raspberry Pi Pin| Variable Name used in program|
  |----------------------|-----------------|-----------------------------|
  | Trig | GPIO14|GPIO_TRIGGER|
  | Echo | GPIO15|GPIO_TRIGGER|
  | Vcc | 5V | |
  | GND | GND | |
  
2. **IR Sensor:**
  
  | IR sensor pin | Raspberry Pi pin | Variable Name used in program|
  |------------|-------|-----------|
  | OUT | GPIO16 | ir |
  
3. **MCP3008 (ADC):**

![mcp3008](https://github.com/RahulP5/Parameter_Monitoring/blob/main/resourse/mcp3008pin.gif)

  | MCP3008 pin | Raspberry Pi pin | Variable Name used in program|
  |--|--|--|
  | VDD | 5V | |
  | Vref | 5V | |
  |AGND | GND | |
  | CLK | GPIO11 | CLK |
  | Dout | GPIO9 | MISO |
  | Din | GPIO10 | MOSI |
  | CS | GPIO8 | CS |
  
  **MCP3008 input pin:**
  
  | MCP3008 pin | ACS712 (Current Sensors) pin |
  |----|---|
  | CH0 | OUT |
  | CH1 | OUT |
 
 
