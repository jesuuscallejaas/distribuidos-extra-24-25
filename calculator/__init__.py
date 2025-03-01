"""Package for the calculator distribution."""

import importlib.util
import logging
import sys
from pathlib import Path

import Ice


if not importlib.util.find_spec("remotecalculator"):
    slice_path = Path(__file__).parent.absolute() / "remotecalculator.ice"
    if not slice_path.exists():
        raise ImportError("cannot import remotecalculator")
    
    Ice.loadSlice(str(slice_path))
    remotecalculator = importlib.import_module("remotecalculator")


def calculator() -> None:
    """Entrypoint for the command line handler of the server."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(sys.argv[0])
    logger.setLevel(logging.DEBUG)
    logger.info("Starting calculator Ice server...")
    
    # TODO: Instance a Calculator servant and add it to the Object adapter
    sys.exit(0)