from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):  # noqa: PLR0915
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.district = QVBoxLayout()
        self.district.setObjectName("district")
        self.district_word = QLabel(self.centralwidget)
        self.district_word.setObjectName("district_word")
        self.district_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 18pt "Microsoft YaHei UI";')
        self.district_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.district.addWidget(self.district_word)

        self.district_combobox = QComboBox(self.centralwidget)
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.addItem("")
        self.district_combobox.setObjectName("district_combobox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.district_combobox.sizePolicy().hasHeightForWidth())
        self.district_combobox.setSizePolicy(sizePolicy)
        self.district_combobox.setStyleSheet('font: 10pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.district.addWidget(self.district_combobox)

        self.horizontalLayout.addLayout(self.district)

        self.age = QVBoxLayout()
        self.age.setObjectName("age")
        self.age_word = QLabel(self.centralwidget)
        self.age_word.setObjectName("age_word")
        self.age_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 18pt "Microsoft YaHei UI";')
        self.age_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.age.addWidget(self.age_word)

        self.age_combobox = QComboBox(self.centralwidget)
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.addItem("")
        self.age_combobox.setObjectName("age_combobox")
        self.age_combobox.setStyleSheet('font: 10pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.age.addWidget(self.age_combobox)

        self.horizontalLayout.addLayout(self.age)

        self.majapp = QVBoxLayout()
        self.majapp.setObjectName("majapp")
        self.majapp_word = QLabel(self.centralwidget)
        self.majapp_word.setObjectName("majapp_word")
        self.majapp_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 18pt "Microsoft YaHei UI";')
        self.majapp_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.majapp.addWidget(self.majapp_word)

        self.majapp_combobox = QComboBox(self.centralwidget)
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.addItem("")
        self.majapp_combobox.setObjectName("majapp_combobox")
        self.majapp_combobox.setStyleSheet('font: 10pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.majapp.addWidget(self.majapp_combobox)

        self.horizontalLayout.addLayout(self.majapp)

        self.position = QVBoxLayout()
        self.position.setObjectName("position")
        self.position_word = QLabel(self.centralwidget)
        self.position_word.setObjectName("position_word")
        self.position_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 18pt "Microsoft YaHei UI";')
        self.position_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.position.addWidget(self.position_word)

        self.position_combobox = QComboBox(self.centralwidget)
        self.position_combobox.addItem("")
        self.position_combobox.addItem("")
        self.position_combobox.addItem("")
        self.position_combobox.setObjectName("position_combobox")
        self.position_combobox.setStyleSheet('font: 10pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.position.addWidget(self.position_combobox)

        self.horizontalLayout.addLayout(self.position)

        self.mode = QVBoxLayout()
        self.mode.setObjectName("mode")
        self.mode_word = QLabel(self.centralwidget)
        self.mode_word.setObjectName("mode_word")
        self.mode_word.setStyleSheet('color: rgb(0, 0, 0);\nfont: 18pt "Microsoft YaHei UI";')
        self.mode_word.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.mode.addWidget(self.mode_word)

        self.mode_combobox = QComboBox(self.centralwidget)
        self.mode_combobox.addItem("")
        self.mode_combobox.addItem("")
        self.mode_combobox.setObjectName("mode_combobox")
        self.mode_combobox.setStyleSheet('font: 10pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.mode.addWidget(self.mode_combobox)

        self.horizontalLayout.addLayout(self.mode)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.enter_btn = QPushButton(self.centralwidget)
        self.enter_btn.setObjectName("enter_btn")
        font = QFont()
        font.setFamilies(["Microsoft YaHei UI"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.enter_btn.setFont(font)
        self.enter_btn.setStyleSheet('font: 16pt "Microsoft YaHei UI";\ncolor: rgb(0, 0, 0);')

        self.horizontalLayout_2.addWidget(self.enter_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.showbroad = QScrollArea(self.centralwidget)
        self.showbroad.setObjectName("showbroad")
        self.showbroad.setStyleSheet(
            'color: rgb(0, 0, 0);\nbackground-color: rgb(255, 255, 255);\nfont: 12pt "Microsoft YaHei UI";'
        )
        self.showbroad.setWidgetResizable(True)
        self.showbroad.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop
        )
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 778, 463))
        self.showbroad.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.showbroad)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):  # noqa: PLR0915
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "弗一把", None))
        self.district_word.setText(QCoreApplication.translate("MainWindow", "\u8d5b\u533a", None))
        self.district_combobox.setItemText(0, QCoreApplication.translate("MainWindow", "\u672a\u77e5", None))
        self.district_combobox.setItemText(1, QCoreApplication.translate("MainWindow", "\u6b27\u6d32", None))
        self.district_combobox.setItemText(2, QCoreApplication.translate("MainWindow", "\u5317\u7f8e", None))
        self.district_combobox.setItemText(3, QCoreApplication.translate("MainWindow", "\u5357\u7f8e", None))
        self.district_combobox.setItemText(4, QCoreApplication.translate("MainWindow", "\u4e9a\u6d32", None))
        self.district_combobox.setItemText(5, QCoreApplication.translate("MainWindow", "\u5927\u6d0b\u6d32", None))
        self.district_combobox.setItemText(6, QCoreApplication.translate("MainWindow", "\u72ec\u8054\u4f53", None))
        self.district_combobox.setItemText(7, QCoreApplication.translate("MainWindow", "\u4e1c\u5357\u4e9a", None))

        self.age_word.setText(QCoreApplication.translate("MainWindow", "\u5e74\u9f84", None))
        self.age_combobox.setItemText(0, QCoreApplication.translate("MainWindow", "\u672a\u77e5", None))
        self.age_combobox.setItemText(1, QCoreApplication.translate("MainWindow", "18", None))
        self.age_combobox.setItemText(2, QCoreApplication.translate("MainWindow", "19", None))
        self.age_combobox.setItemText(3, QCoreApplication.translate("MainWindow", "20", None))
        self.age_combobox.setItemText(4, QCoreApplication.translate("MainWindow", "21", None))
        self.age_combobox.setItemText(5, QCoreApplication.translate("MainWindow", "22", None))
        self.age_combobox.setItemText(6, QCoreApplication.translate("MainWindow", "23", None))
        self.age_combobox.setItemText(7, QCoreApplication.translate("MainWindow", "24", None))
        self.age_combobox.setItemText(8, QCoreApplication.translate("MainWindow", "25", None))
        self.age_combobox.setItemText(9, QCoreApplication.translate("MainWindow", "26", None))
        self.age_combobox.setItemText(10, QCoreApplication.translate("MainWindow", "27", None))
        self.age_combobox.setItemText(11, QCoreApplication.translate("MainWindow", "28", None))
        self.age_combobox.setItemText(12, QCoreApplication.translate("MainWindow", "29", None))
        self.age_combobox.setItemText(13, QCoreApplication.translate("MainWindow", "30", None))
        self.age_combobox.setItemText(14, QCoreApplication.translate("MainWindow", "31", None))
        self.age_combobox.setItemText(15, QCoreApplication.translate("MainWindow", "32", None))
        self.age_combobox.setItemText(16, QCoreApplication.translate("MainWindow", "33", None))
        self.age_combobox.setItemText(17, QCoreApplication.translate("MainWindow", "34", None))
        self.age_combobox.setItemText(18, QCoreApplication.translate("MainWindow", "35", None))
        self.age_combobox.setItemText(19, QCoreApplication.translate("MainWindow", "36", None))
        self.age_combobox.setItemText(20, QCoreApplication.translate("MainWindow", "37", None))
        self.age_combobox.setItemText(21, QCoreApplication.translate("MainWindow", "38", None))

        self.majapp_word.setText(QCoreApplication.translate("MainWindow", "major\u6b21\u6570", None))
        self.majapp_combobox.setItemText(0, QCoreApplication.translate("MainWindow", "\u672a\u77e5", None))
        self.majapp_combobox.setItemText(1, QCoreApplication.translate("MainWindow", "1", None))
        self.majapp_combobox.setItemText(2, QCoreApplication.translate("MainWindow", "2", None))
        self.majapp_combobox.setItemText(3, QCoreApplication.translate("MainWindow", "3", None))
        self.majapp_combobox.setItemText(4, QCoreApplication.translate("MainWindow", "4", None))
        self.majapp_combobox.setItemText(5, QCoreApplication.translate("MainWindow", "5", None))
        self.majapp_combobox.setItemText(6, QCoreApplication.translate("MainWindow", "6", None))
        self.majapp_combobox.setItemText(7, QCoreApplication.translate("MainWindow", "7", None))
        self.majapp_combobox.setItemText(8, QCoreApplication.translate("MainWindow", "8", None))
        self.majapp_combobox.setItemText(9, QCoreApplication.translate("MainWindow", "9", None))
        self.majapp_combobox.setItemText(10, QCoreApplication.translate("MainWindow", "10", None))
        self.majapp_combobox.setItemText(11, QCoreApplication.translate("MainWindow", "11", None))
        self.majapp_combobox.setItemText(12, QCoreApplication.translate("MainWindow", "12", None))
        self.majapp_combobox.setItemText(13, QCoreApplication.translate("MainWindow", "13", None))
        self.majapp_combobox.setItemText(14, QCoreApplication.translate("MainWindow", "14", None))
        self.majapp_combobox.setItemText(15, QCoreApplication.translate("MainWindow", "15", None))
        self.majapp_combobox.setItemText(16, QCoreApplication.translate("MainWindow", "16", None))
        self.majapp_combobox.setItemText(17, QCoreApplication.translate("MainWindow", "17", None))
        self.majapp_combobox.setItemText(18, QCoreApplication.translate("MainWindow", "18", None))
        self.majapp_combobox.setItemText(19, QCoreApplication.translate("MainWindow", "19", None))

        self.position_word.setText(QCoreApplication.translate("MainWindow", "\u4f4d\u7f6e", None))
        self.position_combobox.setItemText(0, QCoreApplication.translate("MainWindow", "\u672a\u77e5", None))
        self.position_combobox.setItemText(
            1, QCoreApplication.translate("MainWindow", "\u6b65\u67aa\u624b", None)
        )  # 步枪手
        self.position_combobox.setItemText(
            2, QCoreApplication.translate("MainWindow", "\u72d9\u51fb\u624b", None)
        )  # 狙击手

        self.mode_word.setText(QCoreApplication.translate("MainWindow", "\u6a21\u5f0f", None))
        self.mode_combobox.setItemText(0, QCoreApplication.translate("MainWindow", "Pro", None))
        self.mode_combobox.setItemText(1, QCoreApplication.translate("MainWindow", "Noob", None))

        self.enter_btn.setText(QCoreApplication.translate("MainWindow", "\u63d0\u4ea4", None))

    # retranslateUi
