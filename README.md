# CBPi4 PiXtendV2S Plugin

## Adds support for the PiXtendV2S extension board to CraftBeerPi 4

The PiXtend extension board adds IEC 61131-2 compliant PLC inputs and outputs to a Raspberry Pi.  
Requires the 'PiXtend Python Library V2', or PPLV2, for short.

## Currently adds the following to CBPi4:

### Sensors:
- **Analog Input (PiXtendV2S)**  
  Returns the raw value (0...5 or 0...10 V) of the selected analog input as float 
  
- **Digital Input (PiXtendV2S)**  
  Returns the state of the selected digital input as int, where 0 = False/OFF and 1 = True/ON
  
- **PT100 (PiXtendV2S)**  
  Allows an analog input to be configured for a PT resistance thermometer (not just PT100)  
  Requires a hardware signal converter that sends a 0...5 or 0...10 V signal to one of the analog inputs  
  Input = analog input to use  
  Voltage = voltage range the input is set to  
  t_min = lowest temperature the signal converter is set to  
  t_max = highest temperature the signal converter is set to  
  Sensor output is a temperature in °C with 1 decimal
  
  
### Actors:
- **Digital Output (PiXtendV2S)**  
  Allows the selected digital output to be toggled on and off  
- **Relay (PiXtendV2S)**  
  Allows the selected relay to be toggled on and off
  
  
### Other Extensions:
- **PixBuzzer**  
  A custom buzzer that uses one of the digital outputs of the board  
  Go to the settings and select one of the digital_outs ("pixbuzzer_do") and the duration of the buzzing noise ("pixbuzzer_duration") 
  The buzzer is triggered every time a notification is sent by the system

## ToDo:

- Add analog outputs
- Add PWMs
- Add GPIOs
- Add DHT11 and DHT22 sensors


For more info on the required library and the hardware itself see here:

English: https://www.pixtend.de/downloads/pixtend-v2-downloads-english/  
German: https://www.pixtend.de/downloads/pixtend-v2-downloads/
