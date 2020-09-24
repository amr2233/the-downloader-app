from PyQt5.Qt import *
import urllib.request
import sys

class firstApp(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        btn_download = QPushButton("Download")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        self.url.setPlaceholderText("url")
        self.save_location.setPlaceholderText("file save location")

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(btn_download)

        self.setLayout(layout)
        self.setWindowTitle("file downloader")
        self.setFocus()

        btn_download.clicked.connect(self.download)


    def download(self):
        l_url = self.url.text()
        l_save_loaction = self.save_location.text()
        urllib.requests.urlretrieve(l_url , l_save_loaction , self.report)

    def report(self, blocknum , blocksize , totalsize):
        result = blocknum * blocksize
        if totalsize > 0 :
            percent = result * 100 / totalsize
            self.progress.setValue(int(percent))





app = QApplication(sys.argv)
dialog = firstApp()
dialog.show()
app.exec_()




