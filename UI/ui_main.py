# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjZTkQE.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(90, 0))
        self.frame.setMaximumSize(QSize(90, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 70))
        self.label_3.setMaximumSize(QSize(60, 60))
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setPixmap(QPixmap(u"UI/icons/opencv.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.left_pushButton_1 = QPushButton(self.frame)
        self.left_pushButton_1.setObjectName(u"left_pushButton_1")
        self.left_pushButton_1.setMinimumSize(QSize(80, 30))
        self.left_pushButton_1.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_1)

        self.left_pushButton_2 = QPushButton(self.frame)
        self.left_pushButton_2.setObjectName(u"left_pushButton_2")
        self.left_pushButton_2.setMinimumSize(QSize(80, 30))
        self.left_pushButton_2.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_2)

        self.left_pushButton_3 = QPushButton(self.frame)
        self.left_pushButton_3.setObjectName(u"left_pushButton_3")
        self.left_pushButton_3.setMinimumSize(QSize(80, 30))
        self.left_pushButton_3.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_3)

        self.left_pushButton_4 = QPushButton(self.frame)
        self.left_pushButton_4.setObjectName(u"left_pushButton_4")
        self.left_pushButton_4.setMinimumSize(QSize(80, 30))
        self.left_pushButton_4.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_4)

        self.left_pushButton_5 = QPushButton(self.frame)
        self.left_pushButton_5.setObjectName(u"left_pushButton_5")
        self.left_pushButton_5.setMinimumSize(QSize(80, 30))
        self.left_pushButton_5.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_5)

        self.left_pushButton_6 = QPushButton(self.frame)
        self.left_pushButton_6.setObjectName(u"left_pushButton_6")
        self.left_pushButton_6.setMinimumSize(QSize(80, 30))
        self.left_pushButton_6.setMaximumSize(QSize(90, 40))

        self.verticalLayout_7.addWidget(self.left_pushButton_6)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.layer_lineEdit = QLineEdit(self.frame)
        self.layer_lineEdit.setObjectName(u"layer_lineEdit")
        self.layer_lineEdit.setMaximumSize(QSize(80, 30))

        self.verticalLayout_2.addWidget(self.layer_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.width_lineEdit = QLineEdit(self.frame)
        self.width_lineEdit.setObjectName(u"width_lineEdit")
        self.width_lineEdit.setMaximumSize(QSize(80, 30))

        self.verticalLayout_4.addWidget(self.width_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.high_lineEdit = QLineEdit(self.frame)
        self.high_lineEdit.setObjectName(u"high_lineEdit")
        self.high_lineEdit.setMaximumSize(QSize(80, 30))

        self.verticalLayout_5.addWidget(self.high_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.type_lineEdit = QLineEdit(self.frame)
        self.type_lineEdit.setObjectName(u"type_lineEdit")
        self.type_lineEdit.setMaximumSize(QSize(80, 30))

        self.verticalLayout_6.addWidget(self.type_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(8)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_32 = QLabel(self.frame_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(68, 0))
        font = QFont()
        font.setPointSize(9)
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_32)

        self.file_path_lineEdit = QLineEdit(self.frame_2)
        self.file_path_lineEdit.setObjectName(u"file_path_lineEdit")

        self.horizontalLayout.addWidget(self.file_path_lineEdit)

        self.file_determine_pushButton = QPushButton(self.frame_2)
        self.file_determine_pushButton.setObjectName(u"file_determine_pushButton")

        self.horizontalLayout.addWidget(self.file_determine_pushButton)

        self.file_path_pushButton = QPushButton(self.frame_2)
        self.file_path_pushButton.setObjectName(u"file_path_pushButton")
        self.file_path_pushButton.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout.addWidget(self.file_path_pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.input = QLabel(self.groupBox)
        self.input.setObjectName(u"input")
        self.input.setMinimumSize(QSize(300, 300))
        self.input.setSizeIncrement(QSize(1, 1))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.input.setFont(font1)
        self.input.setFrameShape(QFrame.NoFrame)
        self.input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.input)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.output = QLabel(self.groupBox)
        self.output.setObjectName(u"output")
        self.output.setMinimumSize(QSize(300, 300))
        self.output.setSizeIncrement(QSize(1, 1))
        self.output.setFont(font1)
        self.output.setFrameShape(QFrame.NoFrame)
        self.output.setFrameShadow(QFrame.Plain)
        self.output.setScaledContents(False)
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_2.addWidget(self.output)


        self.verticalLayout.addWidget(self.groupBox)

        self.parameter_stackedWidget = QStackedWidget(self.frame_2)
        self.parameter_stackedWidget.setObjectName(u"parameter_stackedWidget")
        self.parameter_stackedWidget.setMaximumSize(QSize(16777215, 150))
        self.parameter_page_1 = QWidget()
        self.parameter_page_1.setObjectName(u"parameter_page_1")
        self.horizontalLayout_3 = QHBoxLayout(self.parameter_page_1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.parameter_page_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_27 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.checkBox_brightness = QCheckBox(self.frame_6)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.checkBox_brightness)
        self.checkBox_brightness.setObjectName(u"checkBox_brightness")

        self.verticalLayout_19.addWidget(self.checkBox_brightness)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.doubleSpinBox = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(-127.000000000000000)
        self.doubleSpinBox.setMaximum(127.000000000000000)

        self.horizontalLayout_18.addWidget(self.doubleSpinBox)


        self.verticalLayout_19.addLayout(self.horizontalLayout_18)

        self.horizontalSlider = QSlider(self.frame_6)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(-127)
        self.horizontalSlider.setMaximum(127)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_19.addWidget(self.horizontalSlider)


        self.horizontalLayout_21.addLayout(self.verticalLayout_19)

        self.line_2 = QFrame(self.frame_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line_2)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.checkBox_contrast = QCheckBox(self.frame_6)
        self.buttonGroup.addButton(self.checkBox_contrast)
        self.checkBox_contrast.setObjectName(u"checkBox_contrast")

        self.verticalLayout_20.addWidget(self.checkBox_contrast)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMaximum(20.000000000000000)
        self.doubleSpinBox_2.setSingleStep(0.100000000000000)
        self.doubleSpinBox_2.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.doubleSpinBox_2.setValue(1.000000000000000)

        self.horizontalLayout_19.addWidget(self.doubleSpinBox_2)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalSlider_2 = QSlider(self.frame_6)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMaximum(200)
        self.horizontalSlider_2.setValue(1)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_20.addWidget(self.horizontalSlider_2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_20)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_21.addWidget(self.line_3)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.checkBox_saturation = QCheckBox(self.frame_6)
        self.buttonGroup.addButton(self.checkBox_saturation)
        self.checkBox_saturation.setObjectName(u"checkBox_saturation")

        self.verticalLayout_21.addWidget(self.checkBox_saturation)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame_6)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setSingleStep(0.100000000000000)
        self.doubleSpinBox_3.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_20.addWidget(self.doubleSpinBox_3)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.horizontalSlider_3 = QSlider(self.frame_6)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_21.addWidget(self.horizontalSlider_3)


        self.horizontalLayout_21.addLayout(self.verticalLayout_21)


        self.verticalLayout_27.addWidget(self.frame_6, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.parameter_stackedWidget.addWidget(self.parameter_page_1)
        self.parameter_page_2 = QWidget()
        self.parameter_page_2.setObjectName(u"parameter_page_2")
        self.verticalLayout_28 = QVBoxLayout(self.parameter_page_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.groupBox_9 = QGroupBox(self.parameter_page_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_30 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.groupBox_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_53 = QLabel(self.frame_7)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_27.addWidget(self.label_53)

        self.label_56 = QLabel(self.frame_7)
        self.label_56.setObjectName(u"label_56")

        self.horizontalLayout_27.addWidget(self.label_56, 0, Qt.AlignLeft)


        self.verticalLayout_29.addLayout(self.horizontalLayout_27)


        self.horizontalLayout_31.addLayout(self.verticalLayout_29)

        self.line_6 = QFrame(self.frame_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_31.addWidget(self.line_6)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_55 = QLabel(self.frame_7)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_28.addWidget(self.label_55)

        self.spinBox_min = QSpinBox(self.frame_7)
        self.spinBox_min.setObjectName(u"spinBox_min")
        self.spinBox_min.setMinimumSize(QSize(80, 0))
        self.spinBox_min.setMaximumSize(QSize(80, 16777215))
        self.spinBox_min.setMaximum(255)
        self.spinBox_min.setValue(50)

        self.horizontalLayout_28.addWidget(self.spinBox_min)

        self.horizontalSlider_min = QSlider(self.frame_7)
        self.horizontalSlider_min.setObjectName(u"horizontalSlider_min")
        self.horizontalSlider_min.setMaximum(255)
        self.horizontalSlider_min.setValue(50)
        self.horizontalSlider_min.setOrientation(Qt.Horizontal)

        self.horizontalLayout_28.addWidget(self.horizontalSlider_min)


        self.verticalLayout_30.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_54 = QLabel(self.frame_7)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_29.addWidget(self.label_54)

        self.spinBox_max = QSpinBox(self.frame_7)
        self.spinBox_max.setObjectName(u"spinBox_max")
        self.spinBox_max.setMinimumSize(QSize(80, 0))
        self.spinBox_max.setMaximumSize(QSize(80, 16777215))
        self.spinBox_max.setMaximum(255)
        self.spinBox_max.setValue(255)

        self.horizontalLayout_29.addWidget(self.spinBox_max)

        self.horizontalSlider_max = QSlider(self.frame_7)
        self.horizontalSlider_max.setObjectName(u"horizontalSlider_max")
        self.horizontalSlider_max.setMaximum(255)
        self.horizontalSlider_max.setValue(255)
        self.horizontalSlider_max.setOrientation(Qt.Horizontal)

        self.horizontalLayout_29.addWidget(self.horizontalSlider_max)


        self.verticalLayout_30.addLayout(self.horizontalLayout_29)


        self.horizontalLayout_31.addLayout(self.verticalLayout_30)

        self.horizontalLayout_31.setStretch(0, 1)
        self.horizontalLayout_31.setStretch(2, 3)

        self.horizontalLayout_30.addWidget(self.frame_7, 0, Qt.AlignVCenter)


        self.verticalLayout_28.addWidget(self.groupBox_9)

        self.parameter_stackedWidget.addWidget(self.parameter_page_2)
        self.parameter_page_3 = QWidget()
        self.parameter_page_3.setObjectName(u"parameter_page_3")
        self.horizontalLayout_5 = QHBoxLayout(self.parameter_page_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.parameter_page_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_26 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SetMaximumSize)
        self.radioButton_Gaussian = QRadioButton(self.frame_5)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButton_Gaussian)
        self.radioButton_Gaussian.setObjectName(u"radioButton_Gaussian")

        self.verticalLayout_25.addWidget(self.radioButton_Gaussian)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(6)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_36 = QLabel(self.frame_5)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_22.addWidget(self.label_36, 0, Qt.AlignTop)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMaximum(1.000000000000000)
        self.doubleSpinBox_6.setSingleStep(0.010000000000000)

        self.horizontalLayout_22.addWidget(self.doubleSpinBox_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_52 = QLabel(self.frame_5)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_23.addWidget(self.label_52, 0, Qt.AlignTop)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMaximum(1.000000000000000)
        self.doubleSpinBox_7.setSingleStep(0.010000000000000)

        self.horizontalLayout_23.addWidget(self.doubleSpinBox_7)


        self.verticalLayout_22.addLayout(self.horizontalLayout_23)


        self.verticalLayout_25.addLayout(self.verticalLayout_22)


        self.horizontalLayout_26.addLayout(self.verticalLayout_25)

        self.line_4 = QFrame(self.frame_5)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_4)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.radioButton_Salt = QRadioButton(self.frame_5)
        self.buttonGroup_2.addButton(self.radioButton_Salt)
        self.radioButton_Salt.setObjectName(u"radioButton_Salt")

        self.verticalLayout_23.addWidget(self.radioButton_Salt)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.doubleSpinBox_4 = QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMaximum(1.000000000000000)
        self.doubleSpinBox_4.setSingleStep(0.010000000000000)

        self.horizontalLayout_24.addWidget(self.doubleSpinBox_4)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_24.addWidget(self.pushButton_4)


        self.verticalLayout_23.addLayout(self.horizontalLayout_24)


        self.horizontalLayout_26.addLayout(self.verticalLayout_23)

        self.line_5 = QFrame(self.frame_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_26.addWidget(self.line_5)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.radioButton_random = QRadioButton(self.frame_5)
        self.buttonGroup_2.addButton(self.radioButton_random)
        self.radioButton_random.setObjectName(u"radioButton_random")

        self.verticalLayout_24.addWidget(self.radioButton_random)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.frame_5)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMaximum(1.000000000000000)
        self.doubleSpinBox_5.setSingleStep(0.010000000000000)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_5)

        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_25.addWidget(self.pushButton_5)


        self.verticalLayout_24.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_26.addLayout(self.verticalLayout_24)

        self.horizontalLayout_26.setStretch(0, 1)
        self.horizontalLayout_26.setStretch(2, 1)
        self.horizontalLayout_26.setStretch(4, 1)

        self.verticalLayout_26.addWidget(self.frame_5, 0, Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.groupBox_3)

        self.parameter_stackedWidget.addWidget(self.parameter_page_3)
        self.parameter_page_4 = QWidget()
        self.parameter_page_4.setObjectName(u"parameter_page_4")
        self.horizontalLayout_6 = QHBoxLayout(self.parameter_page_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.parameter_page_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_31 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.radioButton_mean = QRadioButton(self.frame_8)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radioButton_mean)
        self.radioButton_mean.setObjectName(u"radioButton_mean")

        self.verticalLayout_32.addWidget(self.radioButton_mean)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_57 = QLabel(self.frame_8)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_3.addWidget(self.label_57, 0, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.frame_8)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(20)
        self.spinBox_3.setValue(3)

        self.gridLayout_3.addWidget(self.spinBox_3, 0, 1, 1, 1)

        self.label_58 = QLabel(self.frame_8)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_3.addWidget(self.label_58, 1, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.frame_8)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(20)
        self.spinBox_4.setValue(3)

        self.gridLayout_3.addWidget(self.spinBox_4, 1, 1, 1, 1)


        self.verticalLayout_32.addLayout(self.gridLayout_3)


        self.horizontalLayout_32.addLayout(self.verticalLayout_32)

        self.line_7 = QFrame(self.frame_8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32.addWidget(self.line_7)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.radioButton_median = QRadioButton(self.frame_8)
        self.buttonGroup_3.addButton(self.radioButton_median)
        self.radioButton_median.setObjectName(u"radioButton_median")

        self.verticalLayout_33.addWidget(self.radioButton_median)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_59 = QLabel(self.frame_8)
        self.label_59.setObjectName(u"label_59")

        self.horizontalLayout_34.addWidget(self.label_59)

        self.spinBox_8 = QSpinBox(self.frame_8)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(20)
        self.spinBox_8.setSingleStep(2)
        self.spinBox_8.setValue(5)

        self.horizontalLayout_34.addWidget(self.spinBox_8)


        self.verticalLayout_33.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_32.addLayout(self.verticalLayout_33)

        self.line_8 = QFrame(self.frame_8)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32.addWidget(self.line_8)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.radioButton_Gaussian_2 = QRadioButton(self.frame_8)
        self.buttonGroup_3.addButton(self.radioButton_Gaussian_2)
        self.radioButton_Gaussian_2.setObjectName(u"radioButton_Gaussian_2")

        self.verticalLayout_34.addWidget(self.radioButton_Gaussian_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_61 = QLabel(self.frame_8)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout.addWidget(self.label_61, 0, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.frame_8)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(20)
        self.spinBox_5.setSingleStep(2)
        self.spinBox_5.setValue(3)

        self.gridLayout.addWidget(self.spinBox_5, 0, 1, 1, 1)

        self.label_62 = QLabel(self.frame_8)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout.addWidget(self.label_62, 0, 2, 1, 1)

        self.spinBox_7 = QSpinBox(self.frame_8)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setValue(10)

        self.gridLayout.addWidget(self.spinBox_7, 0, 3, 1, 1)

        self.label_60 = QLabel(self.frame_8)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout.addWidget(self.label_60, 1, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.frame_8)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(20)
        self.spinBox_6.setSingleStep(2)
        self.spinBox_6.setValue(3)

        self.gridLayout.addWidget(self.spinBox_6, 1, 1, 1, 1)

        self.label_63 = QLabel(self.frame_8)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout.addWidget(self.label_63, 1, 2, 1, 1)

        self.spinBox_12 = QSpinBox(self.frame_8)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setValue(10)

        self.gridLayout.addWidget(self.spinBox_12, 1, 3, 1, 1)


        self.verticalLayout_34.addLayout(self.gridLayout)


        self.horizontalLayout_32.addLayout(self.verticalLayout_34)

        self.line_9 = QFrame(self.frame_8)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_32.addWidget(self.line_9)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.radioButton_bilateral = QRadioButton(self.frame_8)
        self.buttonGroup_3.addButton(self.radioButton_bilateral)
        self.radioButton_bilateral.setObjectName(u"radioButton_bilateral")

        self.verticalLayout_35.addWidget(self.radioButton_bilateral)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_64 = QLabel(self.frame_8)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_2.addWidget(self.label_64, 0, 0, 1, 1)

        self.spinBox_9 = QSpinBox(self.frame_8)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setMaximum(20)
        self.spinBox_9.setValue(9)

        self.gridLayout_2.addWidget(self.spinBox_9, 0, 1, 1, 2)

        self.label_65 = QLabel(self.frame_8)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_2.addWidget(self.label_65, 1, 0, 1, 2)

        self.spinBox_10 = QSpinBox(self.frame_8)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setValue(75)

        self.gridLayout_2.addWidget(self.spinBox_10, 1, 2, 1, 1)

        self.label_66 = QLabel(self.frame_8)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_2.addWidget(self.label_66, 2, 0, 1, 2)

        self.spinBox_11 = QSpinBox(self.frame_8)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setValue(75)

        self.gridLayout_2.addWidget(self.spinBox_11, 2, 2, 1, 1)


        self.verticalLayout_35.addLayout(self.gridLayout_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_35)


        self.verticalLayout_31.addWidget(self.frame_8, 0, Qt.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.groupBox_4)

        self.parameter_stackedWidget.addWidget(self.parameter_page_4)
        self.parameter_page_5 = QWidget()
        self.parameter_page_5.setObjectName(u"parameter_page_5")
        self.horizontalLayout_7 = QHBoxLayout(self.parameter_page_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.parameter_page_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_35 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_9 = QFrame(self.groupBox_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.radioButton_dilate = QRadioButton(self.frame_9)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radioButton_dilate)
        self.radioButton_dilate.setObjectName(u"radioButton_dilate")

        self.verticalLayout_36.addWidget(self.radioButton_dilate)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_39 = QLabel(self.frame_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(70, 0))
        self.label_39.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_4.addWidget(self.label_39, 0, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.frame_9)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setMinimum(1)
        self.spinBox_13.setMaximum(20)
        self.spinBox_13.setValue(3)

        self.gridLayout_4.addWidget(self.spinBox_13, 0, 1, 1, 1)

        self.label_38 = QLabel(self.frame_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(70, 0))
        self.label_38.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_4.addWidget(self.label_38, 1, 0, 1, 1)

        self.spinBox_14 = QSpinBox(self.frame_9)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setMinimum(1)
        self.spinBox_14.setMaximum(20)

        self.gridLayout_4.addWidget(self.spinBox_14, 1, 1, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_4)


        self.horizontalLayout_33.addLayout(self.verticalLayout_36)

        self.line_10 = QFrame(self.frame_9)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.line_10)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.radioButton_etch = QRadioButton(self.frame_9)
        self.buttonGroup_4.addButton(self.radioButton_etch)
        self.radioButton_etch.setObjectName(u"radioButton_etch")

        self.verticalLayout_37.addWidget(self.radioButton_etch)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(70, 0))
        self.label_40.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_5.addWidget(self.label_40, 0, 0, 1, 1)

        self.spinBox_15 = QSpinBox(self.frame_9)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setMinimum(1)
        self.spinBox_15.setMaximum(20)
        self.spinBox_15.setValue(3)

        self.gridLayout_5.addWidget(self.spinBox_15, 0, 1, 1, 1)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(70, 0))
        self.label_41.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_5.addWidget(self.label_41, 1, 0, 1, 1)

        self.spinBox_16 = QSpinBox(self.frame_9)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMinimum(1)
        self.spinBox_16.setMaximum(20)

        self.gridLayout_5.addWidget(self.spinBox_16, 1, 1, 1, 1)


        self.verticalLayout_37.addLayout(self.gridLayout_5)


        self.horizontalLayout_33.addLayout(self.verticalLayout_37)

        self.line_11 = QFrame(self.frame_9)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.line_11)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.radioButton_open = QRadioButton(self.frame_9)
        self.buttonGroup_4.addButton(self.radioButton_open)
        self.radioButton_open.setObjectName(u"radioButton_open")

        self.verticalLayout_38.addWidget(self.radioButton_open)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_43 = QLabel(self.frame_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(70, 0))
        self.label_43.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_6.addWidget(self.label_43, 1, 0, 1, 1)

        self.spinBox_18 = QSpinBox(self.frame_9)
        self.spinBox_18.setObjectName(u"spinBox_18")
        self.spinBox_18.setMinimum(1)
        self.spinBox_18.setMaximum(20)

        self.gridLayout_6.addWidget(self.spinBox_18, 1, 1, 1, 1)

        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(70, 0))
        self.label_42.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_6.addWidget(self.label_42, 0, 0, 1, 1)

        self.spinBox_17 = QSpinBox(self.frame_9)
        self.spinBox_17.setObjectName(u"spinBox_17")
        self.spinBox_17.setMinimum(1)
        self.spinBox_17.setMaximum(20)
        self.spinBox_17.setValue(3)

        self.gridLayout_6.addWidget(self.spinBox_17, 0, 1, 1, 1)


        self.verticalLayout_38.addLayout(self.gridLayout_6)


        self.horizontalLayout_33.addLayout(self.verticalLayout_38)

        self.line_12 = QFrame(self.frame_9)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_33.addWidget(self.line_12)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.radioButton_close = QRadioButton(self.frame_9)
        self.buttonGroup_4.addButton(self.radioButton_close)
        self.radioButton_close.setObjectName(u"radioButton_close")

        self.verticalLayout_39.addWidget(self.radioButton_close)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_44 = QLabel(self.frame_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(70, 0))
        self.label_44.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_7.addWidget(self.label_44, 0, 0, 1, 1)

        self.spinBox_19 = QSpinBox(self.frame_9)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setMinimum(1)
        self.spinBox_19.setMaximum(20)
        self.spinBox_19.setValue(3)

        self.gridLayout_7.addWidget(self.spinBox_19, 0, 1, 1, 1)

        self.label_45 = QLabel(self.frame_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(70, 0))
        self.label_45.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_7.addWidget(self.label_45, 1, 0, 1, 1)

        self.spinBox_20 = QSpinBox(self.frame_9)
        self.spinBox_20.setObjectName(u"spinBox_20")
        self.spinBox_20.setMinimum(1)
        self.spinBox_20.setMaximum(20)

        self.gridLayout_7.addWidget(self.spinBox_20, 1, 1, 1, 1)


        self.verticalLayout_39.addLayout(self.gridLayout_7)


        self.horizontalLayout_33.addLayout(self.verticalLayout_39)


        self.horizontalLayout_35.addWidget(self.frame_9, 0, Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.groupBox_5)

        self.parameter_stackedWidget.addWidget(self.parameter_page_5)
        self.parameter_page_6 = QWidget()
        self.parameter_page_6.setObjectName(u"parameter_page_6")
        self.horizontalLayout_8 = QHBoxLayout(self.parameter_page_6)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.parameter_page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_36 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.groupBox_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.radioButton_Canny = QRadioButton(self.frame_10)
        self.buttonGroup_5 = QButtonGroup(MainWindow)
        self.buttonGroup_5.setObjectName(u"buttonGroup_5")
        self.buttonGroup_5.addButton(self.radioButton_Canny)
        self.radioButton_Canny.setObjectName(u"radioButton_Canny")

        self.verticalLayout_40.addWidget(self.radioButton_Canny, 0, Qt.AlignTop)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_8.addWidget(self.label_33, 0, 0, 1, 1)

        self.spinBox_21 = QSpinBox(self.frame_10)
        self.spinBox_21.setObjectName(u"spinBox_21")
        self.spinBox_21.setMaximum(255)
        self.spinBox_21.setValue(100)

        self.gridLayout_8.addWidget(self.spinBox_21, 0, 1, 1, 1)

        self.label_34 = QLabel(self.frame_10)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_8.addWidget(self.label_34, 1, 0, 1, 1)

        self.spinBox_22 = QSpinBox(self.frame_10)
        self.spinBox_22.setObjectName(u"spinBox_22")
        self.spinBox_22.setMaximum(255)
        self.spinBox_22.setValue(160)

        self.gridLayout_8.addWidget(self.spinBox_22, 1, 1, 1, 1)


        self.verticalLayout_40.addLayout(self.gridLayout_8)


        self.horizontalLayout_39.addLayout(self.verticalLayout_40)

        self.line_13 = QFrame(self.frame_10)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_39.addWidget(self.line_13)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.radioButton_Laplacian = QRadioButton(self.frame_10)
        self.buttonGroup_5.addButton(self.radioButton_Laplacian)
        self.radioButton_Laplacian.setObjectName(u"radioButton_Laplacian")

        self.verticalLayout_41.addWidget(self.radioButton_Laplacian)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_47 = QLabel(self.frame_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(70, 0))
        self.label_47.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_38.addWidget(self.label_47)

        self.spinBox_23 = QSpinBox(self.frame_10)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setMinimum(1)
        self.spinBox_23.setMaximum(9)
        self.spinBox_23.setSingleStep(2)
        self.spinBox_23.setValue(3)

        self.horizontalLayout_38.addWidget(self.spinBox_23)


        self.verticalLayout_41.addLayout(self.horizontalLayout_38)


        self.horizontalLayout_39.addLayout(self.verticalLayout_41)

        self.line_14 = QFrame(self.frame_10)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_39.addWidget(self.line_14)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.radioButton_scharr = QRadioButton(self.frame_10)
        self.buttonGroup_5.addButton(self.radioButton_scharr)
        self.radioButton_scharr.setObjectName(u"radioButton_scharr")

        self.verticalLayout_44.addWidget(self.radioButton_scharr)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_11)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.comboBox_4 = QComboBox(self.frame_11)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_42.addWidget(self.comboBox_4)


        self.verticalLayout_44.addWidget(self.frame_11)


        self.horizontalLayout_39.addLayout(self.verticalLayout_44)

        self.line_15 = QFrame(self.frame_10)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_39.addWidget(self.line_15)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.radioButton_sobel = QRadioButton(self.frame_10)
        self.buttonGroup_5.addButton(self.radioButton_sobel)
        self.radioButton_sobel.setObjectName(u"radioButton_sobel")

        self.verticalLayout_43.addWidget(self.radioButton_sobel)

        self.comboBox_5 = QComboBox(self.frame_10)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_43.addWidget(self.comboBox_5)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_46 = QLabel(self.frame_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(70, 0))
        self.label_46.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_37.addWidget(self.label_46)

        self.spinBox_24 = QSpinBox(self.frame_10)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setMinimum(1)
        self.spinBox_24.setMaximum(9)
        self.spinBox_24.setSingleStep(2)
        self.spinBox_24.setValue(3)

        self.horizontalLayout_37.addWidget(self.spinBox_24)


        self.verticalLayout_43.addLayout(self.horizontalLayout_37)


        self.horizontalLayout_39.addLayout(self.verticalLayout_43)


        self.horizontalLayout_36.addWidget(self.frame_10, 0, Qt.AlignVCenter)


        self.horizontalLayout_8.addWidget(self.groupBox_6)

        self.parameter_stackedWidget.addWidget(self.parameter_page_6)

        self.verticalLayout.addWidget(self.parameter_stackedWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 4)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setMinimumSize(QSize(350, 0))
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.histogram_tab = QWidget()
        self.histogram_tab.setObjectName(u"histogram_tab")
        self.verticalLayout_17 = QVBoxLayout(self.histogram_tab)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.histogram_stackedWidget = QStackedWidget(self.histogram_tab)
        self.histogram_stackedWidget.setObjectName(u"histogram_stackedWidget")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_9 = QVBoxLayout(self.page_6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_4 = QFrame(self.page_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_24 = QLabel(self.frame_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(50, 20))
        self.label_24.setMaximumSize(QSize(50, 20))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_24.setFont(font2)

        self.verticalLayout_45.addWidget(self.label_24)

        self.widget = PlotWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setMinimumSize(QSize(170, 140))

        self.verticalLayout_45.addWidget(self.widget)


        self.verticalLayout_46.addLayout(self.verticalLayout_45)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.histogram_stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_18 = QVBoxLayout(self.page_7)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_26 = QLabel(self.page_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(20, 20))
        self.label_26.setMaximumSize(QSize(80, 20))
        self.label_26.setFont(font2)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_26)

        self.widget_2 = PlotWidget(self.page_7)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(160, 140))

        self.horizontalLayout_15.addWidget(self.widget_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_27 = QLabel(self.page_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(20, 20))
        self.label_27.setMaximumSize(QSize(80, 20))
        self.label_27.setFont(font2)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_27)

        self.widget_3 = PlotWidget(self.page_7)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(160, 140))

        self.horizontalLayout_16.addWidget(self.widget_3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_28 = QLabel(self.page_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(20, 20))
        self.label_28.setMaximumSize(QSize(80, 20))
        self.label_28.setFont(font2)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_28)

        self.widget_4 = PlotWidget(self.page_7)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(160, 140))

        self.horizontalLayout_17.addWidget(self.widget_4)


        self.verticalLayout_18.addLayout(self.horizontalLayout_17)

        self.histogram_stackedWidget.addWidget(self.page_7)

        self.verticalLayout_17.addWidget(self.histogram_stackedWidget)

        self.tabWidget.addTab(self.histogram_tab, "")
        self.colorSpace_tab = QWidget()
        self.colorSpace_tab.setObjectName(u"colorSpace_tab")
        self.verticalLayout_10 = QVBoxLayout(self.colorSpace_tab)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.colorSpace_comboBox = QComboBox(self.colorSpace_tab)
        self.colorSpace_comboBox.addItem("")
        self.colorSpace_comboBox.addItem("")
        self.colorSpace_comboBox.addItem("")
        self.colorSpace_comboBox.setObjectName(u"colorSpace_comboBox")

        self.verticalLayout_10.addWidget(self.colorSpace_comboBox)

        self.colorSpace_stackedWidget = QStackedWidget(self.colorSpace_tab)
        self.colorSpace_stackedWidget.setObjectName(u"colorSpace_stackedWidget")
        self.colorSpace_page_HSV = QWidget()
        self.colorSpace_page_HSV.setObjectName(u"colorSpace_page_HSV")
        self.verticalLayout_14 = QVBoxLayout(self.colorSpace_page_HSV)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.colorSpace_page_HSV)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(20, 20))
        self.label_14.setMaximumSize(QSize(80, 20))
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_14)

        self.label_H = QLabel(self.colorSpace_page_HSV)
        self.label_H.setObjectName(u"label_H")
        self.label_H.setMinimumSize(QSize(140, 140))
        self.label_H.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_H)

        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.colorSpace_page_HSV)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(20, 20))
        self.label_18.setMaximumSize(QSize(80, 20))
        self.label_18.setFont(font2)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_18)

        self.label_S = QLabel(self.colorSpace_page_HSV)
        self.label_S.setObjectName(u"label_S")
        self.label_S.setMinimumSize(QSize(140, 140))
        self.label_S.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_S)

        self.horizontalLayout_13.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_17 = QLabel(self.colorSpace_page_HSV)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(20, 20))
        self.label_17.setMaximumSize(QSize(80, 20))
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.label_V = QLabel(self.colorSpace_page_HSV)
        self.label_V.setObjectName(u"label_V")
        self.label_V.setMinimumSize(QSize(140, 140))
        self.label_V.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_V)

        self.horizontalLayout_14.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_14)

        self.colorSpace_stackedWidget.addWidget(self.colorSpace_page_HSV)
        self.colorSpace_page_RGB = QWidget()
        self.colorSpace_page_RGB.setObjectName(u"colorSpace_page_RGB")
        self.verticalLayout_12 = QVBoxLayout(self.colorSpace_page_RGB)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.colorSpace_page_RGB)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(20, 20))
        self.label_8.setMaximumSize(QSize(80, 20))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_R = QLabel(self.colorSpace_page_RGB)
        self.label_R.setObjectName(u"label_R")
        self.label_R.setMinimumSize(QSize(140, 140))
        self.label_R.setMaximumSize(QSize(16777215, 16777215))
        self.label_R.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_R)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.colorSpace_page_RGB)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(20, 20))
        self.label_9.setMaximumSize(QSize(80, 20))
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.label_G = QLabel(self.colorSpace_page_RGB)
        self.label_G.setObjectName(u"label_G")
        self.label_G.setMinimumSize(QSize(140, 140))
        self.label_G.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_G)

        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.colorSpace_page_RGB)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(20, 20))
        self.label_10.setMaximumSize(QSize(80, 20))
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.label_B = QLabel(self.colorSpace_page_RGB)
        self.label_B.setObjectName(u"label_B")
        self.label_B.setMinimumSize(QSize(140, 140))
        self.label_B.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_B)

        self.horizontalLayout_11.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.colorSpace_stackedWidget.addWidget(self.colorSpace_page_RGB)
        self.colorSpace_page_GRAY = QWidget()
        self.colorSpace_page_GRAY.setObjectName(u"colorSpace_page_GRAY")
        self.verticalLayout_16 = QVBoxLayout(self.colorSpace_page_GRAY)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_21 = QLabel(self.colorSpace_page_GRAY)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(50, 20))
        self.label_21.setMaximumSize(QSize(50, 20))
        self.label_21.setFont(font2)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_21)

        self.label_GRAY = QLabel(self.colorSpace_page_GRAY)
        self.label_GRAY.setObjectName(u"label_GRAY")
        self.label_GRAY.setMinimumSize(QSize(0, 0))
        self.label_GRAY.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_GRAY)


        self.verticalLayout_16.addLayout(self.verticalLayout_13)

        self.colorSpace_stackedWidget.addWidget(self.colorSpace_page_GRAY)

        self.verticalLayout_10.addWidget(self.colorSpace_stackedWidget)

        self.tabWidget.addTab(self.colorSpace_tab, "")
        self.frequency_tab = QWidget()
        self.frequency_tab.setObjectName(u"frequency_tab")
        self.verticalLayout_11 = QVBoxLayout(self.frequency_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_7 = QGroupBox(self.frequency_tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(190, 190))
        self.groupBox_7.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_7.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_frequency = QLabel(self.groupBox_7)
        self.label_frequency.setObjectName(u"label_frequency")
        self.label_frequency.setMinimumSize(QSize(190, 0))
        self.label_frequency.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_frequency)


        self.verticalLayout_11.addWidget(self.groupBox_7)

        self.tabWidget.addTab(self.frequency_tab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 7)
        self.horizontalLayout_4.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.parameter_stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        self.histogram_stackedWidget.setCurrentIndex(1)
        self.colorSpace_stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u4e8eOpenCV\u7684\u6570\u5b57\u56fe\u50cf\u5904\u7406\u6559\u5b66\u6f14\u793a\u7cfb\u7edf", None))
        self.label_3.setText("")
        self.left_pushButton_1.setText(QCoreApplication.translate("MainWindow", u"\u5c5e\u6027\u53d8\u6362", None))
        self.left_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9608\u503c", None))
        self.left_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0", None))
        self.left_pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6ee4\u6ce2", None))
        self.left_pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u5f62\u6001\u5b66", None))
        self.left_pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u68af\u5ea6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u5c42\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\uff1a", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u56fe\u7247", None))
        self.file_path_lineEdit.setText(QCoreApplication.translate("MainWindow", u" \u56fe\u50cf\u6587\u4ef6\u8def\u5f84", None))
        self.file_determine_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.file_path_pushButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u663e\u793a", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"Input", None))
        self.output.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.checkBox_brightness.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.checkBox_contrast.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6", None))
        self.doubleSpinBox_2.setPrefix("")
        self.checkBox_saturation.setText(QCoreApplication.translate("MainWindow", u"\u9971\u548c\u5ea6", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8272\u5f69\u7c7b\u578b", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"GRAY", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.radioButton_Gaussian.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u566a\u58f0", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"mean", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"sigma", None))
        self.radioButton_Salt.setText(QCoreApplication.translate("MainWindow", u"\u6912\u76d0\u566a\u58f0", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.radioButton_random.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a\u566a\u58f0", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.radioButton_mean.setText(QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"kernelW", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"kernelH", None))
        self.radioButton_median.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.radioButton_Gaussian_2.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"kernelW", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"sigmaX", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"kernelH", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"sigmaY", None))
        self.radioButton_bilateral.setText(QCoreApplication.translate("MainWindow", u"\u53cc\u8fb9\u6ee4\u6ce2", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"diameter", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"sigmaColor", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"sigmaSpace", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.radioButton_dilate.setText(QCoreApplication.translate("MainWindow", u"\u8150\u8680", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"iternationals", None))
        self.radioButton_etch.setText(QCoreApplication.translate("MainWindow", u"\u81a8\u80c0", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"iternationals", None))
        self.radioButton_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u8fd0\u7b97", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"iternationals", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.radioButton_close.setText(QCoreApplication.translate("MainWindow", u"\u95ed\u8fd0\u7b97", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"iternationals", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u914d\u7f6e", None))
        self.radioButton_Canny.setText(QCoreApplication.translate("MainWindow", u"Canny", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.radioButton_Laplacian.setText(QCoreApplication.translate("MainWindow", u"Laplacian", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.spinBox_23.setPrefix(QCoreApplication.translate("MainWindow", u"0", None))
        self.radioButton_scharr.setText(QCoreApplication.translate("MainWindow", u"scharr", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"XY", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Y", None))

        self.radioButton_sobel.setText(QCoreApplication.translate("MainWindow", u"sobel", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"XY", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"X", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"Y", None))

        self.label_46.setText(QCoreApplication.translate("MainWindow", u"kernelSize", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"GRAY", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.histogram_tab), QCoreApplication.translate("MainWindow", u"\u76f4\u65b9\u56fe", None))
        self.colorSpace_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"RGB", None))
        self.colorSpace_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"GRAY", None))
        self.colorSpace_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"HSV", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_H.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_S.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_V.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_R.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.label_G.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_B.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"GRAY", None))
        self.label_GRAY.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.colorSpace_tab), QCoreApplication.translate("MainWindow", u"\u8272\u5f69\u7a7a\u95f4", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u9891\u8c31", None))
        self.label_frequency.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frequency_tab), QCoreApplication.translate("MainWindow", u"\u9891\u57df", None))
    # retranslateUi

