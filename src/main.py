import logging
from util.rsaEncrypt import RSAEncrypt

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
def log(Msg: str = "") -> None:
    print(f"[INFO]: {Msg}")
    logger.info(Msg)
if __name__ == "__main__":
    log("Initalizing")