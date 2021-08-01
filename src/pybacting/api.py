# -*- coding: utf-8 -*-

"""Java components via :mod:`scyjava`."""

from scyjava import config, jimport, start_jvm

__all__ = [
    "cdk",
    "opsin",
    "inchi",
    "pubchem",
]

WORKSPACE = "."

config.add_endpoints(
    # "io.github.egonw.bacting:managers-semweb:0.0.20",
    "io.github.egonw.bacting:managers-inchi:0.0.21",
    "io.github.egonw.bacting:managers-pubchem:0.0.21",
    # "io.github.egonw.bacting:managers-xml:0.0.20",
    # "io.github.egonw.bacting:managers-rdf:0.0.20",
    # "io.github.egonw.bacting:managers-bioinfo:0.0.20",
    # "io.github.egonw.bacting:managers-oscar:0.0.20",
    # "io.github.egonw.bacting:managers-cheminfo:0.0.20",
    # "io.github.egonw.bacting:managers-ui:0.0.20",
    # "io.github.egonw.bacting:managers-excel:0.0.20",
    "io.github.egonw.bacting:managers-opsin:0.0.21",
    "io.github.egonw.bacting:managers-cdk:0.0.21",
    # "io.github.egonw.bacting:managers-biojava:0.0.20",
    # "io.github.egonw.bacting:managers-bridgedb:0.0.20",
    # "io.github.egonw.bacting:bacting-core:0.0.20",
)

# Connecting to the JVM is usually done implicitly, but since spreading
# the endpoints and instantiation across many classes causes a problem,
# it's better to consolidate them here and make instantiation explicit
start_jvm()

# FIXME
#  Scyjava takes the entire list of endpoints that go in config.add_endpoints(...)
#  above and does a string join on them with "+" as the delimiter, then writes
#  a file with this name. If the list of endpoints are too long, then the OS
#  will send an error for trying to write a file with a name that's too long. This
#  needs some serious re-working in scyjava. Potential solution is to sort the
#  dependencies, create a hash to use as the filename, then store the list itself
#  inside the file/directory based on that hash.
#  See: https://github.com/scijava/scyjava/issues/30

cdk_class = jimport("net.bioclipse.managers.CDKManager")
cdk = cdk_class(WORKSPACE)

inchi_cls = jimport("net.bioclipse.managers.InChIManager")
inchi = inchi_cls(WORKSPACE)

opsin_class = jimport("net.bioclipse.managers.OpsinManager")
opsin = opsin_class(WORKSPACE)

pubchem_cls = jimport("net.bioclipse.managers.PubChemManager")
pubchem = pubchem_cls(WORKSPACE)
