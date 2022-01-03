# -*- coding: utf-8 -*-

"""Java components via :mod:`scyjava`."""

from scyjava import config, jimport, start_jvm

__all__ = [
    "biojava",
    "bridgedb",
    "cdk",
    "excel",
    "inchi",
    "opsin",
    "oscar",
    "pubchem",
    "qudt",
    "rdf",
    "xml",
]

WORKSPACE = "."
VERSION = "0.0.30"

# The ones marked with "no" can't be loaded because they are POM-only
# artifacts. See the excellent explanation given by @ctrueden why at:
# https://github.com/scijava/scyjava/issues/30#issuecomment-892061823
endpoints = (
    # f"io.github.egonw.bacting:managers-semweb:{VERSION}", # no
    f"io.github.egonw.bacting:managers-inchi:{VERSION}",
    f"io.github.egonw.bacting:managers-pubchem:{VERSION}",
    f"io.github.egonw.bacting:managers-xml:{VERSION}",
    f"io.github.egonw.bacting:managers-rdf:{VERSION}",
    # f"io.github.egonw.bacting:managers-bioinfo:{VERSION}", # no
    f"io.github.egonw.bacting:managers-oscar:{VERSION}",
    # f"io.github.egonw.bacting:managers-cheminfo:{VERSION}",# no
    f"io.github.egonw.bacting:managers-ui:{VERSION}",
    f"io.github.egonw.bacting:managers-excel:{VERSION}",
    f"io.github.egonw.bacting:managers-opsin:{VERSION}",
    f"io.github.egonw.bacting:managers-cdk:{VERSION}",
    f"io.github.egonw.bacting:managers-biojava:{VERSION}",
    f"io.github.egonw.bacting:managers-bridgedb:{VERSION}",
    f"io.github.egonw.bacting:bacting-core:{VERSION}",
)
config.endpoints.extend(endpoints)

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
"""The CDK manager from Bacting."""

inchi_cls = jimport("net.bioclipse.managers.InChIManager")
inchi = inchi_cls(WORKSPACE)
"""The InChI manager from Bacting."""

opsin_class = jimport("net.bioclipse.managers.OpsinManager")
opsin = opsin_class(WORKSPACE)
"""The Opsin manager from Bacting."""

pubchem_cls = jimport("net.bioclipse.managers.PubChemManager")
pubchem = pubchem_cls(WORKSPACE)
"""The PubChem manager from Bacting."""

xml_cls = jimport("net.bioclipse.managers.XMLManager")
xml = xml_cls(WORKSPACE)
"""The XML manager from Bacting."""

rdf_cls = jimport("net.bioclipse.managers.RDFManager")
rdf = rdf_cls(WORKSPACE)
"""The RDF manager from Bacting."""

oscar_cls = jimport("net.bioclipse.managers.OscarManager")
oscar = oscar_cls(WORKSPACE)
"""The Oscar manager from Bacting."""

bridgedb_cls = jimport("net.bioclipse.managers.BridgedbManager")
bridgedb = bridgedb_cls(WORKSPACE)
"""The BridgeDB manager from Bacting."""

excel_cls = jimport("net.bioclipse.managers.ExcelManager")
excel = excel_cls(WORKSPACE)
"""The Excel manager from Bacting."""

biojava_cls = jimport("net.bioclipse.managers.BiojavaManager")
biojava = biojava_cls(WORKSPACE)
"""The BioJava manager from Bacting."""

qudt_cls = jimport("net.bioclipse.managers.QUDTManager")
qudt = qudt_cls(WORKSPACE)
"""The quantity conversion manager from Bacting."""
