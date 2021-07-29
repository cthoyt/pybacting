# pybacting

Python wrapper around [bacting](https://github.com/egonw/bacting).

## Usage

Based on the example from the bacting page, you can do:

```python
from pybacting import cdk

print(cdk.fromSMILES("COC"))
```

Or you can use some of the more pythonic functions that wrap the functions
exposed through the `pybacting.cdk` object:

```python
import pybacting

print(pybacting.from_smiles("COC"))
```

## Installation

Before installing, you'll need to make sure Maven (`mvn`) is available on your
path. If you're on mac, use `brew install maven`.

Install from GitHub:

```shell
$ pip install git+https://github.com/cthoyt/pybacting
```

Install in development mode:

```shell
$ git clone https://github.com/cthoyt/pybacting
$ cd pybacting
$ pip install --editable .
```

