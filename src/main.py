import logging
import uuid
from util.rsaEncrypt import RSAEncrypt
from lib.configReader import ReadJSON
from lib.loadFile import loadFile, saveFile

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(filename=f"logs/{str(uuid.uuid4())}.log")
def log(Msg: str = "") -> None:
    print(f"[INFO]: {Msg}")
    logger.info(Msg)

class Main:
    def __init__(self,ConfigFile: str = "config/config.json"):
        self.ConfigFile = ConfigFile
        self.EncryptionClass: RSAEncrypt
        self.Input = ""
        self.ModeRunning = True
    
    def LoadConfig(self):
        log("Loading Config")
        self.Config = ReadJSON(self.ConfigFile)
        self.Method = self.Config["method"]
        self.Mode = self.Config["mode"]
        log(f"Using Method: {self.Method}")

    def ExecuteMode(self):
        if self.Mode == "input":
            while self.ModeRunning:
                Action = input("[INPUT] ACTION [d/e]: ").lower()
                if Action == "d":
                    Message = bytes(input("[INPUT] RSA MESSAGE: "))
                    self.Input = loadFile(Message)
                    PrivateKey = loadFile(input("[INPUT] PRIVATE KEY:"))
                    self.Encrypt()
                    self.EncryptionClass.Decrypt(Message)
                    Output = self.EncryptionClass.Output
                    log(Output)
                elif Action == "e":
                    Message = input("[INPUT] MSG: ")
                    self.Input = loadFile(Message)
                    self.Encrypt()
                    self.EncryptionClass.Encrypt()
                    Output = self.EncryptionClass.Output
                    saveFile(Output,"files/output.bin")
                    PrivateKey = self.EncryptionClass.PrivateKey
                    saveFile(PrivateKey,"file/private.key")
                    log(f"ENCRYPTED: ")
                    log(Output)
                    print("Private Key:")
                    print(PrivateKey)


    def Encrypt(self):
        if self.Method == "asymetric":
            self.EncryptionClass = RSAEncrypt(int(self.Config["rsakey-length"]),self.Input)

if __name__ == "__main__":
    log("Initalizing")
    MainClass = Main()
    MainClass.LoadConfig()
    MainClass.ExecuteMode()