import logging
import time
from math import exp

import caracal.declaration.datatypes as caratypes
from caracal.execution import (
    Event,
    handler,
    Node,
)


class Generator(Node):
    value = Event("value", caratypes.Tuple(caratypes.Float()))

    def run(self):
        index = 0
        while not self.stopped:
            time.sleep(1)
            self.fire(self.value, index)
            index += 1
