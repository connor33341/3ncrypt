import json
import logging


logger = logging.getLogger(__name__)
def log(Msg: str = "") -> None:
    print(f"[INFO]: {Msg}")
    logger.info(Msg)
def ReadJSON(FileDir: str = "") -> dict:
    log(f"Reading JSON: {FileDir}")
    Data = {}
    if FileDir == "":
        return {}
    try:
        with open(FileDir,"r") as File:
            FileContents = File.read()
            Data = json.loads(FileContents)
            File.close()
    except Exception as Error:
        logging.error(f"Error Occoured: {Error}")
    return Data