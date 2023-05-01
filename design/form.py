# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QProgressBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextBrowser, QToolButton, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(782, 598)
        self.gridLayout_8 = QGridLayout(Widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_6 = QWidget(Widget)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_6 = QGridLayout(self.widget_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(11, 2, 11, 2)
        self.toolButton = QToolButton(self.widget_6)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_6.addWidget(self.toolButton, 1, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget_6)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_6.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_6, 0, 0, 1, 1)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(False)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(1, -1, 1, -1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_7.addWidget(self.tableWidget, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 1, 2, 1)

        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(False)
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 4, 0, 10)
        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_txt = QPushButton(self.widget_4)
        self.pushButton_txt.setObjectName(u"pushButton_txt")
        self.pushButton_txt.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButton_txt, 0, 1, 1, 1)

        self.pushButton_excel = QPushButton(self.widget_4)
        self.pushButton_excel.setObjectName(u"pushButton_excel")
        self.pushButton_excel.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButton_excel, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.widget_4, 4, 0, 1, 2)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(1)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.textBrowser_url = QTextBrowser(self.widget_5)
        self.textBrowser_url.setObjectName(u"textBrowser_url")

        self.gridLayout_3.addWidget(self.textBrowser_url, 2, 0, 1, 1)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_5, 3, 1, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.textBrowser_name = QTextBrowser(self.widget_2)
        self.textBrowser_name.setObjectName(u"textBrowser_name")

        self.gridLayout.addWidget(self.textBrowser_name, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.widget_2, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_5.addWidget(self.progressBar, 5, 0, 1, 2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 0)

        self.gridLayout_5.addWidget(self.widget_3, 2, 0, 1, 2)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.listWidget = QListWidget(self.widget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_5.addWidget(self.listWidget, 1, 0, 1, 2)


        self.gridLayout_8.addWidget(self.widget, 1, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0432 Google Drive", None))
        self.toolButton.setText(QCoreApplication.translate("Widget", u"...", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u041f\u0443\u0442\u044c \u0434\u043e \u0444\u0430\u0439\u043b\u0430 json", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a : 0", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.pushButton_txt.setText(QCoreApplication.translate("Widget", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0432 txt", None))
        self.pushButton_excel.setText(QCoreApplication.translate("Widget", u"\u0418\u043c\u043f\u043e\u0440\u0442 \u0432 excel", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u0421\u0441\u044b\u043b\u043a\u0430 \u043d\u0430 \u0444\u0430\u0439\u043b", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u043f\u043a\u0438 \u043d\u0430 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0435", None))
    # retranslateUi

