
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

buzzer_output = None
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

    def __init__(self, duration, output, level):
        threading.Thread.__init__(self)
        self.output = output
        self.duration = duration
        self.level = level
        self.runnig = True

    def shutdown(self):
        pass

    def stop(self):
        pass

    def run(self):
        pass



class Buzzer(CBPiExtension):

    def __init__(self,cbpi):
        self.cbpi = cbpi
        self._task = asyncio.create_task(self.run())


    async def run(self):
        self.duration = 0.1
        logger.info('Starting Buzzer background task')
        await self.buzzer_output()
        await self.buzzer_level()
        if buzzer_output is None or buzzer_output == "" or not buzzer_output:
            logger.warning('Check buzzer GPIO is set')
        if buzzer_level is None or buzzer_level == "" or not buzzer_level:
            logger.warning('Check buzzer level is set') 
        else:
            self.listener_ID = self.cbpi.notification.add_listener(self.buzzerEvent)
            logger.info("Buzzer Lisetener ID: {}".format(self.listener_ID))
            logging.info("Buzzer started")
            await self.start_buzz()
        pass

    async def buzzer_output(self):
        global buzzer_output
        buzzer_output = self.cbpi.config.get("buzzer_output", None)
        if buzzer_output is None:
            logger.info("INIT Buzzer GPIO")
            try:
                await self.cbpi.config.add("buzzer_output", ConfigType.SELECT, "Buzzer Output", [{"label": "digital_out0", "value": p.digital_out0},
                                                                                                {"label": "digital_out1", "value": p.digital_out1},
                                                                                                {"label": "digital_out2", "value": p.digital_out2},
                                                                                                {"label": "digital_out3", "value": p.digital_out3},
                                                                                                {"label": "digital_out4", "value": p.digital_out4},
                                                                                                {"label": "digital_out5", "value": p.digital_out5},
                                                                                                {"label": "digital_out6", "value": p.digital_out6},
                                                                                                {"label": "digital_out7", "value": p.digital_out7}])
                buzzer_output = self.cbpi.config.get("buzzer_output", None)
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

        self.buzzer = BuzzerThread(self.duration,buzzer_output,buzzer_level)
        self.buzzer.daemon = False
        self.buzzer.start()
        self.buzzer.stop()

    async def start_buzz(self):
        self.buzzer = BuzzerThread(self.duration,buzzer_output,buzzer_level)
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
