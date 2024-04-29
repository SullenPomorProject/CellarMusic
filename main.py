from PyQt5 import QtCore, QtWidgets, QtMultimedia
import interface1
import os
from os import path
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl, QTime


class Player(QtWidgets.QMainWindow, interface1.Ui_MainWindow):
    def __init__(self):
        super(Player, self).__init__()
        self.setupUi(self)


        self.current_index = 0
        self.current_index_user = 0
        self.current_song = 0
        # global is_base_load
        self.button_start_pause.clicked.connect(self.play_pause)
        self.listWidget_base.itemDoubleClicked.connect(self.play_pause)
        self.listWidget_user.itemDoubleClicked.connect(self.play_pause)
        self.button_download.clicked.connect(self.base_load)
        self.button_download.clicked.connect(self.load)
        self.horizontalSlider.sliderMoved[int].connect(self.timecode)

        self.control_tab = 0

        self.button_next.clicked.connect(self.play_next)
        self.button_back.clicked.connect(self.play_previous)
        # self.button_loop.clicked.connect(self.base_load)
        # if not is_base_load:
        #     print("base_load")
        #     is_base_load = True

        self.tabWidget.currentChanged.connect(self.handle_tab_change)


        self.app_dir = ""
        self.usr_dir = ""
        self.is_play = False

        self.setFixedSize(self.size())


    def handle_tab_change(self, index):
        if index == 0:
            self.control_tab = 0
            print(self.control_tab)
        elif index == 1:
            self.control_tab = index
            print(self.control_tab)

    # def status_play(self, status):
    #     if status == QtMultimedia.QMediaPlayer.EndOfMedia:
    #         print("END!!!")

    def play(self):
        self.is_play = True
        self.button_start_pause.setIcon(QIcon("res\\pause128.png"))
        self.button_start_pause.setIconSize(self.button_start_pause.size())
        if self.control_tab == 0:
            if hasattr(self, 'media_player') and self.media_player.state() == QtMultimedia.QMediaPlayer.PausedState and self.current_song == self.current_index:
                self.media_player.play()
            else:
                item = self.listWidget_base.currentItem()

                if item:
                    file_name = os.path.join(self.app_dir, item.text())
                    content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(os.path.join(file_name)))
                    self.media_player = QtMultimedia.QMediaPlayer()
                    self.media_player.setMedia(content)
                    self.media_player.play()
                    # self.media_player.setPosition(self.media_player.position())
                    self.media_player.durationChanged.connect(self.set_duration)
                    self.media_player.positionChanged.connect(self.set_play_pos)
                    self.label.setText(path.splitext(os.path.join(item.text()))[0])
                    self.current_index = self.listWidget_base.currentRow()
                    self.media_player.setMedia(content)
                    self.media_player.play()
                    self.current_song = self.current_index
                else:
                    self.listWidget_base.setCurrentRow(0)
                    self.play()
        elif self.control_tab == 1:
            if hasattr(self, 'media_player') and self.media_player.state() == QtMultimedia.QMediaPlayer.PausedState and self.current_song == self.current_index_user:
                self.media_player.play()
            else:
                item = self.listWidget_user.currentItem()

                if item:
                    file_name = os.path.join(self.usr_dir, item.text())
                    content = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(file_name))
                    self.media_player = QtMultimedia.QMediaPlayer()
                    self.media_player.setMedia(content)
                    self.media_player.durationChanged.connect(self.set_duration)
                    self.media_player.positionChanged.connect(self.set_play_pos)
                    self.label.setText(path.splitext(os.path.join(item.text()))[0])
                    self.current_index_user = self.listWidget_user.currentRow()
                    self.media_player.setMedia(content)
                    self.media_player.play()
                    self.current_song = self.current_index_user
                else:
                    self.listWidget_user.setCurrentRow(0)
                    self.play()


    def pause(self):
        self.is_play = False
        self.button_start_pause.setIcon(QIcon("res\\play-button-arrowhead128.png"))
        self.button_start_pause.setIconSize(self.button_start_pause.size())
        if hasattr(self, 'media_player') and self.media_player:
            self.media_player.pause()

    def play_pause(self):
        if not self.is_play:
            self.play()
        else:
            self.pause()

    def play_next(self):
        if self.control_tab == 0:
            self.current_index += 1
            if self.current_index < self.listWidget_base.count():
                self.listWidget_base.setCurrentRow(self.current_index)
                self.play()
        elif self.control_tab == 1:
            self.current_index_user += 1
            if self.current_index_user < self.listWidget_user.count():
                self.listWidget_user.setCurrentRow(self.current_index_user)
                self.play()

    def play_previous(self):
        if self.control_tab == 0:
            self.current_index -= 1
            if self.current_index >= 0:
                self.listWidget_base.setCurrentRow(self.current_index)
                self.play()
        elif self.control_tab == 1:
            self.current_index_user -= 1
            if self.current_index_user >= 0:
                self.listWidget_user.setCurrentRow(self.current_index_user)
                self.play()

    def timecode(self, position):
        self.media_player.setPosition(position)

    def set_duration(self, duration):
        self.horizontalSlider.setMaximum(duration)
        self.label_all.setText(QTime(0, 0).addMSecs(duration).toString())

    def set_play_pos(self, pos):
        self.horizontalSlider.setValue(pos)
        self.label_now.setText(QTime(0, 0).addMSecs(pos).toString())

    def base_load(self):
        self.listWidget_base.clear()

        dir = "Music"

        if dir:
            for f_name in os.listdir(dir):
                if f_name.endswith(".mp3"):
                    self.listWidget_base.addItem(os.path.join(f_name))
            self.app_dir = dir



    def load(self):
        self.listWidget_user.clear()

        dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку с вашей музыкой")

        if dir:
            for f_name in os.listdir(dir):
                if f_name.endswith(".mp3"):
                    self.listWidget_user.addItem(os.path.join(f_name))
            self.usr_dir = dir


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    player = Player()
    player.show()
    app.exec()