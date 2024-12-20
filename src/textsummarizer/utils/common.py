import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_ymal(path_to_ymal: Path) -> ConfigBox:
    """reads ymal file and returns

    Args:
        path_to_ymal (str): path like input

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_ymal) as ymal_file:
            content = yaml.safe_load(ymal_filefile)
            logger.info(f"ymal file: {path_to_ymal} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("ymal file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of paths like directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
        """
for path in path_to_directories:
    os.makedirs(path, exit_ok=True)
    if verbose:
        logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: path) -> str:
    """get size in kb
    
    Args:
        path (path): path of the file
        
    Returns:
        str: size of the file in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"











