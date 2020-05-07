# Import Python standard libraries
import random
from hashlib import sha256

# Import 3rd party libraries
import numpy as np

# TODO: check for other types, lists, etc.
# TODO: decide what to do when seed is None
# TODO: check if there are faster ways to get the buffer
# TODO: make sure the python random seed is correct every time
def seed_rngs(seed=None):
    """
    Sets a seed to both Python and numpy's RNGs.

    The main purpose of this function is to guarantee reproducibility when
    mixing Python and numpy's RNGs, also allowing to use strings as seed
    (numpy only takes uint32 of arrays of uint32 as seed). This is done
    by converting non-integer seeds to a numpy array from a buffer
    build from a hash.
    """

    # Seed the Python RNGs
    random.seed(seed)

    # Build a seed adequate for numpy, if necessary, and use it
    if not seed:
        return
    elif isinstance(seed, str):
        _seed = np.frombuffer(
        sha256(seed.encode("utf-8")).digest(), dtype=np.uint32
        )
    else:
        _seed = seed

    np.random.seed(_seed)
