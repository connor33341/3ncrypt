# "method":"asymetric"
import rsa

class RSAEncrypt:
    def __init__(self,RSALength: int = 16,InputString: str = "") -> None:
        self.RSALength = RSALength
        self.InputString = InputString
        self.PrivateKey = ""
        self.PublicKey = ""
        self.Output = ""

    def Encrypt(self) -> None:
        self.PublicKey, self.PrivateKey = rsa.newkeys(self.RSALength)
        self.Output = rsa.encrypt(self.InputString.encode(),self.PublicKey)

    def Decrypt(self, Input) -> None:
        self.Output = rsa.decrypt(Input,self.PrivateKey).decode()

    def GetEncrypted(self) -> str:
        return self.Output