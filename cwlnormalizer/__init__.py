from ruamel.yaml import YAML
import json

__version__ = "0.1"


def normalize(doc):
    return doc


def normalize_stream(input_stream, output_stream):
    yaml = YAML(typ='safe')
    doc = yaml.load(input_stream)
    normalized = normalize(doc)
    json.dump(normalized, output_stream, indent=4)
