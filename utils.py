import json
import importlib
from pathlib import Path
from caracal.execution import Node


def generate_declarations_in_module_from_implementations(module_directory=".", namespace=None):
    module_directory = Path(module_directory)
    cfg = json.load(open(module_directory / "cara.json"))  # GET repository/cara.json
    module_name, node_names = cfg["module_name"], cfg["exported_nodes"]
    nodes = importlib.import_module(f"{module_directory.name}.implementation")
    declarations = [Node.get_declaration(nodes.__getattribute__(node_name)) for node_name in node_names]
    for declaration in declarations:
        declaration.namespace = namespace or module_name
    for node_name, declaration in zip(node_names, declarations):
        node_declaration_directory = module_directory / "declaration"
        node_declaration_directory.mkdir(parents=True, exist_ok=True)
        with open(node_declaration_directory / f"{node_name}.cara", "w") as f:
            f.write(str(declaration))


def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = importlib.import_module(package)


if __name__ == '__main__':
    module_name = "cara_sample_module"
    # install_and_import(module_name)
    cara_module_implementations = importlib.import_module(f"{module_name}.implementation")
    node_type_declarations = [str(Node.get_declaration(node)) for node in cara_module_implementations]
    node_instances = [node() for node in cara_module_implementations]


    generate_declarations_in_module_from_implementations(module_name)
