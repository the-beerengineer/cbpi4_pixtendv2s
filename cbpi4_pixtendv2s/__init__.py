
# -*- coding: utf-8 -*-
import os, threading, time
from aiohttp import web
import logging
import asyncio
import random
from cbpi.api import *
from cbpi.api.config import ConfigType
from cbpi.api.base import CBPiBase

from pixtendv2s import PiXtendV2S

logger = logging.getLogger(__name__)
p = PiXtendV2S()

buzzer_gpio = None
buzzer_level = None
buzzer = None

@parameters([Property.Select(label="Input", options=["analog_in0", "analog_in1"], description="Select PiXtend analog input to use.")])
class PixAnalogInputs(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(PixAnalogInputs, self).__init__(cbpi, id, props)
        self.input = self.props.get("Input", None)

    async def run(self):
        while self.running:
            if self.input == "analog_in0":
                self.value = p.analog_in0
            elif self.input == "analog_in1":
                self.value = p.analog_in1
            else:
                self.raw = None

            self.push_update(self.value)
            await asyncio.sleep(1)

    def get_state(self):
        return dict(value=self.value)


@parameters([Property.Select(label="Input", options=["digital_in0", "digital_in1", "digital_in2", "digital_in3", "digital_in4", "digital_in5", "digital_in6", "digital_in7"], description="Select PiXtend digital input to use.")])
class PixDigitalInputs(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(PixDigitalInputs, self).__init__(cbpi, id, props)
        self.input = self.props.get("Input", None)

    async def run(self):
        while self.running:
            if self.input == "digital_in0":
                self.value = p.digital_in0
            elif self.input == "digital_in1":
                self.value = p.digital_in1
            elif self.input == "digital_in2":
                self.value = p.digital_in2
            elif self.input == "digital_in3":
                self.value = p.digital_in3
            elif self.input == "digital_in4":
                self.value = p.digital_in4
            elif self.input == "digital_in5":
                self.value = p.digital_in5
            elif self.input == "digital_in6":
                self.value = p.digital_in6
            elif self.input == "digital_in7":
                self.value = p.digital_in7
            else:
                self.raw = None

            self.push_update(self.value)
            await asyncio.sleep(1)

    def get_state(self):
        return dict(value=self.value)


@parameters([Property.Select(label="Input", options=["analog_in0", "analog_in1"], description="Select PiXtend analog input to use."),
             Property.Select(label="Voltage", options=[5, 10], description="Is the input set to 5 or 10 V?"),
             Property.Number(label="t_min", description="Enter the lowest temperature the signal converter is set to."),
             Property.Number(label="t_max", description="Enter the highest temperature the signal converter is set to.")])
class PixPT100(CBPiSensor):

    def __init__(self, cbpi, id, props):
        super(PixPT100, self).__init__(cbpi, id, props)
        self.input = self.props.get("Input", None)
        self.volt = self.props.get("Voltage", 10)
        self.t_min = self.props.get("t_min", None)
        self.t_max = self.props.get("t_max", None)

    async def run(self):
        while self.running:
            if self.input == "analog_in0":
                self.raw = p.analog_in0
            elif self.input == "analog_in1":
                self.raw = p.analog_in1
            else:
                self.raw = None

            self.value = round((float(self.raw) * ((int(self.t_max) - int(self.t_min)) / int(self.volt))) + int(self.t_min), 1)
            self.push_update(self.value)
            await asyncio.sleep(1)

    def get_state(self):
        return dict(value=self.value)


@parameters([Property.Select(label="Output", options=["digital_out0", "digital_out1", "digital_out2", "digital_out3", "digital_out4", "digital_out5", "digital_out6", "digital_out7"], description="Select PiXtend digital output to use.")])
class PixDigitalOutputs(CBPiActor):

    async def on_start(self):
        self.power = None
        self.output = self.props.get("Output", None)
        self.state = False

    async def on(self, power = None):
        if self.output == "digital_out0":
            p.digital_out0 = True
        elif self.output == "digital_out1":
            p.digital_out1 = True
        elif self.output == "digital_out2":
            p.digital_out2 = True
        elif self.output == "digital_out3":
            p.digital_out3 = True
        elif self.output == "digital_out4":
            p.digital_out4 = True
        elif self.output == "digital_out5":
            p.digital_out5 = True
        elif self.output == "digital_out6":
            p.digital_out6 = True
        elif self.output == "digital_out7":
            p.digital_out7 = True
        else:
            self.state = None

        self.state = True

    async def off(self):
        if self.output == "digital_out0":
            p.digital_out0 = False
        elif self.output == "digital_out1":
            p.digital_out1 = False
        elif self.output == "digital_out2":
            p.digital_out2 = False
        elif self.output == "digital_out3":
            p.digital_out3 = False
        elif self.output == "digital_out4":
            p.digital_out4 = False
        elif self.output == "digital_out5":
            p.digital_out5 = False
        elif self.output == "digital_out6":
            p.digital_out6 = False
        elif self.output == "digital_out7":
            p.digital_out7 = False
        else:
            self.state = None

        self.state = False

    def get_state(self):
        return self.state

    async def run(self):
        while self.running:
            await asyncio.sleep(1)

    async def set_power(self, power):
        pass
        
@parameters([Property.Select(label="Output", options=["relay0", "relay1", "relay2", "relay3"], description="Select PiXtend relay to use.")])
class PixRelays(CBPiActor):

    async def on_start(self):
        self.power = None
        self.output = self.props.get("Output", None)
        self.state = False

    async def on(self, power = None):
        if self.output == "relay0":
            p.relay0 = True
        elif self.output == "relay1":
            p.relay1 = True
        elif self.output == "relay2":
            p.relay2 = True
        elif self.output == "relay3":
            p.relay3 = True
        else:
            self.state = None

        self.state = True

    async def off(self):
        if self.output == "relay0":
            p.relay0 = False
        elif self.output == "relay1":
            p.relay1 = False
        elif self.output == "relay2":
            p.relay2 = False
        elif self.output == "relay3":
            p.relay3 = False
        else:
            self.state = None

        self.state = False

    def get_state(self):
        return self.state

    async def run(self):
        while self.running:
            await asyncio.sleep(1)

    async def set_power(self, power):
        pass
        
class BuzzerThread (threading.Thread):

    def __init__(self, sound,gpio,level):
        threading.Thread.__init__(self)
        self.gpio = gpio
        self.sound = sound
        self.level = level
        self.runnig = True

    def shutdown(self):
        pass

    def stop(self):
        pass

    def run(self):
        try:
            for i in self.sound:
                if (isinstance(i, str)):
                    if i == "H" and self.level == "HIGH":
                        GPIO.output(int(self.gpio), GPIO.HIGH)
                    elif i == "H" and self.level != "HIGH":
                        GPIO.output(int(self.gpio), GPIO.LOW)
                    elif i == "L" and self.level == "HIGH":
                        GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        GPIO.output(int(self.gpio), GPIO.HIGH)
                else:
                    time.sleep(i)
        except Exception as e:
            pass
        finally:
            pass



class Buzzer(CBPiExtension):

    def __init__(self,cbpi):
        self.cbpi = cbpi
        self._task = asyncio.create_task(self.run())


    async def run(self):
        self.sound = {'standard':["H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L"],
                      'warning':["H", 0.2, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.2, "L"],
                      'error':["H", 0.3, "L", 0.1, "H", 0.3, "L", 0.1, "H", 0.3, "L"]}
        logger.info('Starting Buzzer background task')
        await self.buzzer_gpio()
        await self.buzzer_level()
        if buzzer_gpio is None or buzzer_gpio == "" or not buzzer_gpio:
            logger.warning('Check buzzer GPIO is set')
        if buzzer_level is None or buzzer_level == "" or not buzzer_level:
            logger.warning('Check buzzer level is set') 
        else:
            self.listener_ID = self.cbpi.notification.add_listener(self.buzzerEvent)
            logger.info("Buzzer Lisetener ID: {}".format(self.listener_ID))
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(buzzer_gpio, GPIO.OUT)
            p.gpio0_ctrl = 1
            logging.info("Buzzer started")
            await self.start_buzz()
        pass

    async def buzzer_gpio(self):
        global buzzer_gpio
        buzzer_gpio = self.cbpi.config.get("buzzer_gpio", None)
        if buzzer_gpio is None:
            logger.info("INIT Buzzer GPIO")
            try:
                await self.cbpi.config.add("buzzer_gpio", p.gpio0, ConfigType.SELECT, "Buzzer GPIO", [{"label": "0", "value": p.gpio0},
                                                                                                {"label": "1", "value": 1},
                                                                                                {"label": "2", "value": 2},
                                                                                                {"label": "3", "value": 3},
                                                                                                {"label": "4", "value": 4},
                                                                                                {"label": "5", "value": 5},
                                                                                                {"label": "6", "value": 6},
                                                                                                {"label": "7", "value": 7},
                                                                                                {"label": "8", "value": 8},
                                                                                                {"label": "9", "value": 9},
                                                                                                {"label": "10", "value": 10},
                                                                                                {"label": "11", "value": 11},
                                                                                                {"label": "12", "value": 12},
                                                                                                {"label": "13", "value": 13},
                                                                                                {"label": "14", "value": 14},
                                                                                                {"label": "15", "value": 15},
                                                                                                {"label": "16", "value": 16},
                                                                                                {"label": "17", "value": 17},
                                                                                                {"label": "18", "value": 18},
                                                                                                {"label": "19", "value": 19},
                                                                                                {"label": "20", "value": 20},
                                                                                                {"label": "21", "value": 21},
                                                                                                {"label": "22", "value": 22},
                                                                                                {"label": "23", "value": 23},
                                                                                                {"label": "24", "value": 24},
                                                                                                {"label": "25", "value": 25},
                                                                                                {"label": "26", "value": 26},
                                                                                                {"label": "27", "value": 27}])
                buzzer_gpio = self.cbpi.config.get("buzzer_gpio", None)
            except:
                logger.warning('Unable to update config')
                
    async def buzzer_level(self):
        global buzzer_level
        buzzer_level = self.cbpi.config.get("buzzer_level", None)
        if buzzer_level is None:
            logger.info("INIT Buzzer Beep Level")
            try:
                await self.cbpi.config.add("buzzer_level", "HIGH", ConfigType.SELECT, "Buzzer Beep Level", [{"label": "HIGH","value": "HIGH"},
                                                                                                            {"label": "LOW", "value": "LOW"}])
                buzzer_level = self.cbpi.config.get("buzzer_level", None)
            except:
                logger.warning('Unable to update database')

    async def buzzerEvent(self, cbpi, title, message, type, action):
        if str(type) == "info" or str(type) == "success":
            type = "standard"
        else:
            type = str(type)

        self.buzzer = BuzzerThread(self.sound[type],buzzer_gpio,buzzer_level)
        self.buzzer.daemon = False
        self.buzzer.start()
        self.buzzer.stop()

    async def start_buzz(self):
        self.buzzer = BuzzerThread(self.sound['standard'],buzzer_gpio,buzzer_level)
        self.buzzer.daemon = False
        self.buzzer.start()
        self.buzzer.stop()


def setup(cbpi):
    cbpi.plugin.register("PT100 (PiXtendV2S)", PixPT100)
    cbpi.plugin.register("Analog Input (PiXtendV2S)", PixAnalogInputs)
    cbpi.plugin.register("Digital Input (PiXtendV2S)", PixDigitalInputs)
    cbpi.plugin.register("Digital Output (PiXtendV2S)", PixDigitalOutputs)
    cbpi.plugin.register("Relay (PiXtendV2S)", PixRelays)
    cbpi.plugin.register("Buzzer", Buzzer)
    pass
