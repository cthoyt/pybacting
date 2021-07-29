from .api import cdk


def from_smiles(smiles: str):
    """Load a molecule from SMILES."""
    return cdk.fromSMILES(smiles)
