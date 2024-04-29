from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl, QTime
import test_interface
import sys

class AudioPlayer(Ui_MainWindow):
    def __init__(self):
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl("Dajjte_Tank_-_Utro_49163450.mp3")))

        play_button = QPushButton("Play")
        play_button.clicked.connect(self.play)
        pause_button = QPushButton("Pause")
        pause_button.clicked.connect(self.pause)

        self.player.positionChanged.connect(self.on_position_changed)

        # layout.addWidget(play_button)
        # layout.addWidget(pause_button)

    def play(self):
        if self.player.state() == QMediaPlayer.StoppedState:
            self.player.setPosition(0)
        self.player.play()

    def pause(self):
        self.player.pause()

    def on_position_changed(self, position):
        if position == self.player.duration():
            self.player.setPosition(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = AudioPlayer()
    player.show()
    sys.exit(app.exec_())
