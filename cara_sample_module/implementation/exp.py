import logging
import time
from math import exp

import caracal.declaration.datatypes as caratypes
from caracal.execution import (
    Event,
    handler,
    Node,
)


class Exp(Node):
    result = Event("result", caratypes.Tuple(caratypes.Float()))

    @handler("input_value", caratypes.Tuple(caratypes.Float()))
    def input_value(self, msg):
        logging.critical(exp(msg.value))
