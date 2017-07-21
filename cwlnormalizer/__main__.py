import sys
from cwlnormalizer import normalize_stream, __version__


def usage():
    print("CWL Normalizer v" + __version__)
    print("Usage:")
    print("  cwlnormalizer < input.cwl > output.json")
    exit(1)


if len(sys.argv) > 1:
    usage()
else:
    normalize_stream(sys.stdin, sys.stdout)
