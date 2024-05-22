import os
from box.exceptions import BoxValueError
import yaml
from Red_Wine import logger  # Assuming `Red_Wine` is a local module
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''Reads the YAML file and returns 
    
    Args:
        path_to_yaml (Path): path like input
    
    Raises:
        ValueError: if ymal file is empty 
        e: empty file
    
    Returns:
        configBox: ConfigBox type

    '''
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file:{path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e

@ensure_annotations
def create_directiories(path_to_direcotries: list, verbose=True):
    '''create list of directories
    Args: 
        path to directories(lsit):  list of paths to directories
        ignore_log (bool, optional): ignore if multiple directories to be created.
    '''

    for path in path_to_direcotries:
        os.mkdir(path, exist_ok = True)
        if verbose:
            logger.info(f'directory {path} created')


@ensure_annotations
def save_json(path: Path, data: dict):
    """ save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved
    """

    with open(path, 'w') as f:
        json.dump(data, f, indent= 4)
    
    logger.info(f'json file {path} saved successfully')

@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """ load json data
    Args:
        path (Path): path to json file

    Returns:
         ConfigBox: ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from:" {path})
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path):
    '''save binary file
    Aggs:
        data(Any): data to be saved as binary
        path(Path): path to binary file 
    '''
    joblib.dump(value = data, filename=path)
    logger.info(f'binary file {path} saved successfully')

@ensure_annotations
def load_bin(path : Path)->Any:
    '''load binary data
    Args: 
        path(Path): path to binary file
    Returns:
    Any: object stored in the fil
    '''
    data = joblib.load(path)
    logger.info(f'binary file {path} loaded successfully')
    return data

@ensure_annotations
def get_size(path: Path)->str:
    '''get size in kb
    Args:
        path(Path): path of the file
    Returns:
        str: size in kb
    '''
    size_in_kb = round(os.path.getsize(path)/1024)
    return f'~{size_in_kb} KB'