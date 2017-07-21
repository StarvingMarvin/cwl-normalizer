# CWL Normalizer

This is a *very* simple tool to transform a CWL document into a normalized (desugared) form.
It applies transformations on per-document basis, so it won't combine multiple documents into one.

## Install

Checkout source code, and install with pip:

    $ git clone https://github.com/StarvingMarvin/cwl-normalizer.git
    $ cd cwl-normalizer
    $ pip install .

## Usage
    
When used from command line it will read from standard input and output to standard output:

    $ python -m cwlnormalizer < SRC > DST

You can also use it as a lib:

    from cwlnormalizer import normalize_stream
    normalize_stream(input_stream, output_stream)
   
or if you are already have document structure loaded into python dict:

    from cwlnormalizer import normalize
    normalize(doc)
