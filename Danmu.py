import datetime
import random, sys
import time
import threading
import os

from PyQt5.QtWidgets import QLabel, QDesktopWidget, QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation, Qt, QPoint, QEasingCurve, QByteArray
from PyQt5.QtGui import QFontMetrics, QPaintEvent, QPalette, QColor, QPainter, QPainterPath, QPen, QBrush, QFont


class Danmu(QLabel):

    def setPosX(self, posx):
        self.__PosX = posx
        return

    def getPosX(self):
        return self.__PosX

    def setPosY(self, posy):
        self.__PosY = posy
        return

    def getPosY(self):
        return self.__PosY

    def setColor(self, color):
        self.__color = color
        return

    def getColor(self):
        return self.__color

    def setQColor(self, qcolor):
        self.__qcolor = qcolor
        return

    def getQColor(self):
        return self.__qcolor

    def setType(self, type):
        self.__type = type
        return

    def getType(self):
        return self.__type

    def setQFont(self, danmuFont):
        self.__font = danmuFont
        return

    def getQFont(self):
        return self.__font

    def setTransparency(self, Transparency):
        self.__transparency = Transparency

    def getTransparency(self):
        return self.__transparency

    def setScreenRect(self, rect):
        self.__rect = rect

    def getScreenRect(self):
        return self.__rect

    def setRunTime(self, runTime):
        self.__runTime = runTime

    def getRunTime(self):
        return self.__runTime

    def getanimation(self):
        return self.__anim2

    def __init__(self, parent=None, text='', color='White', rect=None, danmuFont=QFont("SimHei", 15), type=20,
                 runTime=10000, Transparency=1.0):
        super().__init__(parent)
        self.__Dtext = text
        self.setColor(color)
        self.setType(type)
        self.setQFont(danmuFont)
        self.setTransparency(Transparency)
        self.setRunTime(runTime)
        self.setScreenRect(rect)
        metrics = QFontMetrics(self.getQFont())
        palll = QPalette()
        DColor = self.getColor()
        self.__anim2 = None

        if DColor == 'White':
            palll.setColor(QPalette.WindowText, QColor(255, 255, 246, 255))
            self.setQColor(QColor(255, 255, 246, 255))
        elif DColor == 'Red':
            palll.setColor(QPalette.WindowText, QColor(231, 0, 18, 255))
            self.setQColor(QColor(231, 0, 18, 255))
        elif DColor == 'Yellow':
            palll.setColor(QPalette.WindowText, QColor(254, 241, 2, 255))
            self.setQColor(QColor(254, 241, 2, 255))
        elif DColor == 'Green':
            palll.setColor(QPalette.WindowText, QColor(0, 152, 67, 255))
            self.setQColor(QColor(0, 152, 67, 255))
        elif DColor == 'Blue':
            palll.setColor(QPalette.WindowText, QColor(0, 160, 234, 255))
            self.setQColor(QColor(0, 160, 234, 255))
        elif DColor == 'Pink':
            palll.setColor(QPalette.WindowText, QColor(226, 2, 127, 255))
            self.setQColor(QColor(226, 2, 127, 255))
        elif DColor == 'Grass':
            palll.setColor(QPalette.WindowText, QColor(144, 195, 32, 255))
            self.setQColor(QColor(144, 195, 32, 255))
        elif DColor == 'DBlue':
            palll.setColor(QPalette.WindowText, QColor(0, 46, 114, 255))
            self.setQColor(QColor(0, 46, 114, 255))
        elif DColor == 'DYellow':
            palll.setColor(QPalette.WindowText, QColor(240, 171, 42, 255))
            self.setQColor(QColor(240, 171, 42, 255))
        elif DColor == 'DPurple':
            palll.setColor(QPalette.WindowText, QColor(104, 58, 123, 255))
            self.setQColor(QColor(104, 58, 123, 255))
        elif DColor == 'LBlue':
            palll.setColor(QPalette.WindowText, QColor(129, 193, 205, 255))
            self.setQColor(QColor(129, 193, 205, 255))
        elif DColor == 'Brown':
            palll.setColor(QPalette.WindowText, QColor(149, 119, 57, 255))
            self.setQColor(QColor(149, 119, 57, 255))
        else:
            palll.setColor(QPalette.WindowText, QColor(255, 255, 246, 255))
            self.setQColor(QColor(255, 255, 246, 255))

        self.setPalette(palll)
        self.setFixedHeight(metrics.height() + 5)
        self.setFixedWidth(metrics.width(text) + 4)
        yy = random.randint(0, rect.height())
        y = min(yy, rect.height() - metrics.height() - 5)
        xx = rect.width() + random.randint(0, 500)
        self.setPosX(xx)
        self.setPosY(y)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setFocusPolicy(Qt.NoFocus)
        self.hide()
        self.__anim2 = QPropertyAnimation(self, b'pos')
        self.__anim2.setDuration(self.getRunTime())
        self.__anim2.setStartValue(QPoint(self.getPosX(), self.getPosY()))
        self.__anim2.setEndValue(QPoint(-self.width()-random.randint(0, 500), self.getPosY()))
        self.__anim2.setEasingCurve(QEasingCurve.Linear)
        self.setWindowOpacity(self.getTransparency())
        self.show()
        self.repaint()
        self.__anim2.start()



    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.save()
        metrics = QFontMetrics(self.getQFont())
        path = QPainterPath()
        pen = QPen(QColor(0, 0, 0, 230))
        painter.setRenderHint(QPainter.Antialiasing)
        penwidth = 4
        pen.setWidth(penwidth)
        len = metrics.width(self.__Dtext)
        w = self.width()
        px = (len - w) / 2
        if px < 0:
            px = -px
        py = (self.height() - metrics.height()) / 2 + metrics.ascent()
        if py < 0:
            py = -py
        path.addText(px + 2, py + 2, self.getQFont(), self.__Dtext)
        painter.strokePath(path, pen)
        painter.drawPath(path)
        painter.fillPath(path, QBrush(self.getQColor()))
        painter.restore()

def main(str):
    app = QApplication(sys.argv)
    desktopWidget = QApplication.desktop()
    screenRect = desktopWidget.screenGeometry()
    cnt=str.split('\n')
    for s in cnt:
        danmu = Danmu(None, s, "White", screenRect)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main('a\na\na\na\na\na')

