import importlib
import json
import logging

from caracal.execution import Session
from caracal.execution import Node

# import nodes

with Session() as session:
    cfg = json.load(open("cara_sample_module/cara.json"))  # GET repository/cara.json
    module_name, node_names = cfg["module_name"], cfg["nodes"]

    nodes = importlib.import_module(f"{module_name}.nodes")

    declaration = '\n'.join([str(Node.get_declaration(nodes.__getattribute__(node_name))) for node_name in node_names])

    logging.critical(declaration)

    exit(0)

    gen_node = nodes.__getattribute__("Generator")()
    exp_node = nodes.__getattribute__("Exp")()
    exp_node.input_value.connect(gen_node.value)
    # exp_node.input_value(0.5)
    session.run()
