from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from lib import aes
import clipboard


class MainClass(QMainWindow):
    
    def __init__(self):
        super(MainClass, self).__init__()
        uic.loadUi('ui/main.ui', self)
        
        # Global
        self.AESAlgo = aes.AESEncryption()
        self.key = ""
        self.Encrypt_iv = ""
        self.Encrypt_Text = ""
        self.EncryptTabLog = ""
        
        self.DecryptedText = ""
        # End Global
        
        # Initial Events
        self.generateky_btn.clicked.connect(self.generateKey)
        self.copyKey_btn.clicked.connect(self.copyKeyButton)
        self.encrypt_btn.clicked.connect(self.encryptText)
        self.copyEncrypted_btn.clicked.connect(self.copyEncryptedBtn)
        self.copyIv_btn.clicked.connect(self.copyIVbtn)
        
        self.decrypt_btn.clicked.connect(self.decryptText)
        self.copyDecrypted_btn.clicked.connect(self.copyDecryptedbtn)
        # End Initial Events
        
        self.show()

    def generateKey(self):
        self.key = self.AESAlgo.GenerateKey()
        self.encrypt_key_text.setText(self.key)
    
    def copyKeyButton(self):
        clipboard.copy(self.key)
    
    def copyEncryptedBtn(self):
        clipboard.copy(self.Encrypt_Text)
        
    def copyIVbtn(self):
        clipboard.copy(self.Encrypt_iv)
        
    def copyDecryptedbtn(self):
        clipboard.copy(self.DecryptedText)
    
    def HandleEncryptTabLog(self, message):
        self.EncryptTabLog += self.EncryptTabLog + message + "\n"
        self.log_encrypt_txt.setText(self.EncryptTabLog)
        
    def encryptText(self):
        if(self.key != "" and self.inputText_txt.toPlainText() != ""):
            self.outputText_txt.setText("")
            self.iv_output_txt.setText("")
            self.HandleEncryptTabLog("Encrypting ... Please Wait ...")
            self.Encrypt_iv, self.Encrypt_Text = self.AESAlgo.encypt(self.inputText_txt.toPlainText(), self.key)
            self.outputText_txt.setText(self.Encrypt_Text)
            self.iv_output_txt.setText(self.Encrypt_iv)
            self.HandleEncryptTabLog("Encrypted Successfully.")
            
    def decryptText(self):
        try:
            self.DecryptedText = self.AESAlgo.decrypt(self.inputDecIv_txt.toPlainText(), self.inputDecText_txt.toPlainText(), self.inputDecKey_txt.toPlainText())
            self.outputDecrypt_txt.setText(self.DecryptedText)
        except:
            self.HandleEncryptTabLog("There is an error in Decryption.")

app = QApplication(sys.argv)
window = MainClass()
app.exec()