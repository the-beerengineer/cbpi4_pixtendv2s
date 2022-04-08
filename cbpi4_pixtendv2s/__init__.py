
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *

from pixtendv2s import PiXtendV2S

logger = logging.getLogger(__name__)
p = PiXtendV2S()


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


@parameters([Property.Select(label="Output", options=["digital_out0", "digital_out1"], description="Select PiXtend digital output to use.")])
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
        else:
            self.state = None

        self.state = True

    async def off(self):
        if self.output == "digital_out0":
            p.digital_out0 = False
        elif self.output == "digital_out1":
            p.digital_out1 = False
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
        


def setup(cbpi):
    cbpi.plugin.register("PT100 (PiXtendV2S)", PixPT100)
    cbpi.plugin.register("Analog Input (PiXtendV2S)", PixAnalogInputs)
    cbpi.plugin.register("Digital Input (PiXtendV2S)", PixDigitalInputs)
    cbpi.plugin.register("Digital Output (PiXtendV2S)", PixDigitalOutputs)
    pass
