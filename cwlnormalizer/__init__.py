from ruamel.yaml import YAML
import json

__version__ = "0.1"


def dict_to_list(obj, key='id', value=None):
    if not isinstance(obj, dict):
        return obj

    ret = []
    for k, v in obj.items():
        if not isinstance(v, dict):
            if value is None:
                raise ValueError('dict values must be dicts')
            else:
                v = {value: v}
        v[key] = k
        ret.append(v)
    return ret


def wrap_to_list(obj):
    if isinstance(obj, list):
        return obj

    return [obj]


def expand_type(t):
    if not isinstance(t, str):
        return t

    if t.endswith('?'):
        t = [expand_type(t[:-1]), 'null']
    elif t.endswith('[]'):
        t = {
            'type': 'array',
            'items': expand_type(t[:-2])
        }
    return t


def normalize_lists(doc):
    for k in 'inputs', 'outputs':
        if k in doc:
            doc[k] = dict_to_list(doc[k], value='type')

    if 'steps' in doc:
        doc['steps'] = dict_to_list(doc['steps'])

    for k in 'hints', 'requirements':
        if k in doc:
            doc[k] = dict_to_list(doc[k], key='class')

    for step in doc.get('steps', []):
        for k in 'in', 'out':
            if k in step:
                doc[k] = dict_to_list(doc[k], value='source')
        for k in 'hints', 'requirements':
            if k in step:
                doc[k] = dict_to_list(doc[k], key='class')


def normalize_arguments(doc):
    if 'arguments' not in doc:
        return

    doc['arguments'] = [{'valueFrom': arg} if isinstance(arg, str) else arg for arg in doc['arguments']]


def normalize_base_command(doc):
    if 'baseCommand' not in doc:
        return

    doc['baseCommand'] = wrap_to_list(doc['baseCommand'])


def normalize_steps(doc):
    for step in doc.get('steps', []):
        step['scatter'] = wrap_to_list(step['scatter'])

        for inp in step.get('in', []):
            inp['source'] = wrap_to_list(inp['source'])


def descend(doc, normalizers):
    for step in doc.get('steps', []):
        run = step.get('run', '')
        if isinstance(run, dict):
            normalize(run, normalizers)

    for subgraph in doc.get('$graph', []):
        normalize(subgraph, normalizers)


def normalize(doc, normalizers=None):
    if normalizers is None:
        normalizers = [
            normalize_lists, normalize_arguments,
            normalize_base_command, normalize_steps
        ]

    for n in normalizers:
        n(doc)

    descend(doc, normalizers)

    return doc


def normalize_stream(input_stream, output_stream):
    yaml = YAML(typ='safe')
    doc = yaml.load(input_stream)
    normalized = normalize(doc)
    json.dump(normalized, output_stream, indent=4)
