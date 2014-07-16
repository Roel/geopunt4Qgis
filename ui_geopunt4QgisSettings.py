# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisSettings.ui'
#
# Created: Wed Jul 16 23:18:52 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_settingsDlg(object):
    def setupUi(self, settingsDlg):
        settingsDlg.setObjectName(_fromUtf8("settingsDlg"))
        settingsDlg.resize(500, 550)
        settingsDlg.setMinimumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntSettingsSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(settingsDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.settingsTab = QtGui.QToolBox(settingsDlg)
        self.settingsTab.setFrameShape(QtGui.QFrame.NoFrame)
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.generalTab = QtGui.QWidget()
        self.generalTab.setGeometry(QtCore.QRect(0, 0, 482, 325))
        self.generalTab.setObjectName(_fromUtf8("generalTab"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.generalTab)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.networkSettings = QtGui.QGroupBox(self.generalTab)
        self.networkSettings.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.networkSettings.setObjectName(_fromUtf8("networkSettings"))
        self.formLayout = QtGui.QFormLayout(self.networkSettings)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_6 = QtGui.QLabel(self.networkSettings)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.hostTxt = QtGui.QLineEdit(self.networkSettings)
        self.hostTxt.setEnabled(False)
        self.hostTxt.setObjectName(_fromUtf8("hostTxt"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.hostTxt)
        self.portTxt = QtGui.QLineEdit(self.networkSettings)
        self.portTxt.setEnabled(False)
        self.portTxt.setObjectName(_fromUtf8("portTxt"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.portTxt)
        self.label_5 = QtGui.QLabel(self.networkSettings)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_7 = QtGui.QLabel(self.networkSettings)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.label_7)
        self.proxyChk = QtGui.QCheckBox(self.networkSettings)
        self.proxyChk.setObjectName(_fromUtf8("proxyChk"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.proxyChk)
        self.verticalLayout_13.addWidget(self.networkSettings)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.generalTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.timeOutBox = QtGui.QSpinBox(self.generalTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeOutBox.sizePolicy().hasHeightForWidth())
        self.timeOutBox.setSizePolicy(sizePolicy)
        self.timeOutBox.setMinimum(1)
        self.timeOutBox.setMaximum(300)
        self.timeOutBox.setProperty("value", 10)
        self.timeOutBox.setObjectName(_fromUtf8("timeOutBox"))
        self.horizontalLayout_2.addWidget(self.timeOutBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_13.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 44, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem1)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntSmal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.generalTab, icon1, _fromUtf8(""))
        self.adresTab = QtGui.QWidget()
        self.adresTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.adresTab.setObjectName(_fromUtf8("adresTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.adresTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.searchOptionsBox_1 = QtGui.QGroupBox(self.adresTab)
        self.searchOptionsBox_1.setObjectName(_fromUtf8("searchOptionsBox_1"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.searchOptionsBox_1)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.adresSearchOnEditChk = QtGui.QRadioButton(self.searchOptionsBox_1)
        self.adresSearchOnEditChk.setObjectName(_fromUtf8("adresSearchOnEditChk"))
        self.verticalLayout_8.addWidget(self.adresSearchOnEditChk)
        self.adresSearchOnEnterChk = QtGui.QRadioButton(self.searchOptionsBox_1)
        self.adresSearchOnEnterChk.setChecked(True)
        self.adresSearchOnEnterChk.setObjectName(_fromUtf8("adresSearchOnEnterChk"))
        self.verticalLayout_8.addWidget(self.adresSearchOnEnterChk)
        self.verticalLayout_3.addWidget(self.searchOptionsBox_1)
        self.add2mapBox_1 = QtGui.QGroupBox(self.adresTab)
        self.add2mapBox_1.setCheckable(False)
        self.add2mapBox_1.setObjectName(_fromUtf8("add2mapBox_1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.add2mapBox_1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.adresSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_1)
        self.adresSavetoFileChk.setChecked(True)
        self.adresSavetoFileChk.setObjectName(_fromUtf8("adresSavetoFileChk"))
        self.verticalLayout_2.addWidget(self.adresSavetoFileChk)
        self.adresSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_1)
        self.adresSaveMemoryChk.setChecked(False)
        self.adresSaveMemoryChk.setObjectName(_fromUtf8("adresSaveMemoryChk"))
        self.verticalLayout_2.addWidget(self.adresSaveMemoryChk)
        self.label_1 = QtGui.QLabel(self.add2mapBox_1)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout_2.addWidget(self.label_1)
        self.adresLayerTxt = QtGui.QLineEdit(self.add2mapBox_1)
        self.adresLayerTxt.setObjectName(_fromUtf8("adresLayerTxt"))
        self.verticalLayout_2.addWidget(self.adresLayerTxt)
        self.verticalLayout_3.addWidget(self.add2mapBox_1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntAddressSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.adresTab, icon2, _fromUtf8(""))
        self.reverseTab = QtGui.QWidget()
        self.reverseTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.reverseTab.setObjectName(_fromUtf8("reverseTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.reverseTab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.add2mapBox_2 = QtGui.QGroupBox(self.reverseTab)
        self.add2mapBox_2.setObjectName(_fromUtf8("add2mapBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.add2mapBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.reverseSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_2)
        self.reverseSavetoFileChk.setChecked(True)
        self.reverseSavetoFileChk.setObjectName(_fromUtf8("reverseSavetoFileChk"))
        self.verticalLayout_4.addWidget(self.reverseSavetoFileChk)
        self.reverseSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_2)
        self.reverseSaveMemoryChk.setChecked(False)
        self.reverseSaveMemoryChk.setObjectName(_fromUtf8("reverseSaveMemoryChk"))
        self.verticalLayout_4.addWidget(self.reverseSaveMemoryChk)
        self.label_2 = QtGui.QLabel(self.add2mapBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.reverseLayerTxt = QtGui.QLineEdit(self.add2mapBox_2)
        self.reverseLayerTxt.setObjectName(_fromUtf8("reverseLayerTxt"))
        self.verticalLayout_4.addWidget(self.reverseLayerTxt)
        self.verticalLayout_5.addWidget(self.add2mapBox_2)
        spacerItem3 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntReverse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.reverseTab, icon3, _fromUtf8(""))
        self.batchgeoCodeTab = QtGui.QWidget()
        self.batchgeoCodeTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.batchgeoCodeTab.setObjectName(_fromUtf8("batchgeoCodeTab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.batchgeoCodeTab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.add2mapBox_3 = QtGui.QGroupBox(self.batchgeoCodeTab)
        self.add2mapBox_3.setCheckable(False)
        self.add2mapBox_3.setObjectName(_fromUtf8("add2mapBox_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.add2mapBox_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.batchSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_3)
        self.batchSavetoFileChk.setChecked(True)
        self.batchSavetoFileChk.setObjectName(_fromUtf8("batchSavetoFileChk"))
        self.verticalLayout_9.addWidget(self.batchSavetoFileChk)
        self.batchSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_3)
        self.batchSaveMemoryChk.setChecked(False)
        self.batchSaveMemoryChk.setObjectName(_fromUtf8("batchSaveMemoryChk"))
        self.verticalLayout_9.addWidget(self.batchSaveMemoryChk)
        self.label_3 = QtGui.QLabel(self.add2mapBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_9.addWidget(self.label_3)
        self.batchLayerTxt = QtGui.QLineEdit(self.add2mapBox_3)
        self.batchLayerTxt.setObjectName(_fromUtf8("batchLayerTxt"))
        self.verticalLayout_9.addWidget(self.batchLayerTxt)
        self.verticalLayout_10.addWidget(self.add2mapBox_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.maxRecordsLabel = QtGui.QLabel(self.batchgeoCodeTab)
        self.maxRecordsLabel.setObjectName(_fromUtf8("maxRecordsLabel"))
        self.horizontalLayout.addWidget(self.maxRecordsLabel)
        self.maxRowsSpinBox = QtGui.QSpinBox(self.batchgeoCodeTab)
        self.maxRowsSpinBox.setSuffix(_fromUtf8(""))
        self.maxRowsSpinBox.setPrefix(_fromUtf8(""))
        self.maxRowsSpinBox.setMinimum(1)
        self.maxRowsSpinBox.setMaximum(5000)
        self.maxRowsSpinBox.setProperty("value", 500)
        self.maxRowsSpinBox.setObjectName(_fromUtf8("maxRowsSpinBox"))
        self.horizontalLayout.addWidget(self.maxRowsSpinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntBatchgeocodeSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.batchgeoCodeTab, icon4, _fromUtf8(""))
        self.poiTab = QtGui.QWidget()
        self.poiTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.poiTab.setObjectName(_fromUtf8("poiTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.poiTab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.add2mapBox_4 = QtGui.QGroupBox(self.poiTab)
        self.add2mapBox_4.setObjectName(_fromUtf8("add2mapBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.add2mapBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.poiSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_4)
        self.poiSavetoFileChk.setChecked(True)
        self.poiSavetoFileChk.setObjectName(_fromUtf8("poiSavetoFileChk"))
        self.verticalLayout_6.addWidget(self.poiSavetoFileChk)
        self.poiSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_4)
        self.poiSaveMemoryChk.setChecked(False)
        self.poiSaveMemoryChk.setObjectName(_fromUtf8("poiSaveMemoryChk"))
        self.verticalLayout_6.addWidget(self.poiSaveMemoryChk)
        self.label_4 = QtGui.QLabel(self.add2mapBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.poiLayerTxt = QtGui.QLineEdit(self.add2mapBox_4)
        self.poiLayerTxt.setObjectName(_fromUtf8("poiLayerTxt"))
        self.verticalLayout_6.addWidget(self.poiLayerTxt)
        self.verticalLayout_7.addWidget(self.add2mapBox_4)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntPoiSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.poiTab, icon5, _fromUtf8(""))
        self.gipodTab = QtGui.QWidget()
        self.gipodTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.gipodTab.setObjectName(_fromUtf8("gipodTab"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.gipodTab)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.add2mapBox_5 = QtGui.QGroupBox(self.gipodTab)
        self.add2mapBox_5.setObjectName(_fromUtf8("add2mapBox_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.add2mapBox_5)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.gipodSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_5)
        self.gipodSavetoFileChk.setEnabled(True)
        self.gipodSavetoFileChk.setChecked(True)
        self.gipodSavetoFileChk.setObjectName(_fromUtf8("gipodSavetoFileChk"))
        self.verticalLayout_11.addWidget(self.gipodSavetoFileChk)
        self.gipodSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_5)
        self.gipodSaveMemoryChk.setChecked(False)
        self.gipodSaveMemoryChk.setObjectName(_fromUtf8("gipodSaveMemoryChk"))
        self.verticalLayout_11.addWidget(self.gipodSaveMemoryChk)
        self.verticalLayout_12.addWidget(self.add2mapBox_5)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem6)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntGIPODsmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.gipodTab, icon6, _fromUtf8(""))
        self.elevationTab = QtGui.QWidget()
        self.elevationTab.setGeometry(QtCore.QRect(0, 0, 482, 300))
        self.elevationTab.setObjectName(_fromUtf8("elevationTab"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.elevationTab)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.add2mapBox_6 = QtGui.QGroupBox(self.elevationTab)
        self.add2mapBox_6.setObjectName(_fromUtf8("add2mapBox_6"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.add2mapBox_6)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.samplesSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_6)
        self.samplesSaveMemoryChk.setChecked(False)
        self.samplesSaveMemoryChk.setObjectName(_fromUtf8("samplesSaveMemoryChk"))
        self.verticalLayout_14.addWidget(self.samplesSaveMemoryChk)
        self.samplesSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_6)
        self.samplesSavetoFileChk.setEnabled(True)
        self.samplesSavetoFileChk.setChecked(True)
        self.samplesSavetoFileChk.setObjectName(_fromUtf8("samplesSavetoFileChk"))
        self.verticalLayout_14.addWidget(self.samplesSavetoFileChk)
        self.label_8 = QtGui.QLabel(self.add2mapBox_6)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_14.addWidget(self.label_8)
        self.sampleLayerTxt = QtGui.QLineEdit(self.add2mapBox_6)
        self.sampleLayerTxt.setObjectName(_fromUtf8("sampleLayerTxt"))
        self.verticalLayout_14.addWidget(self.sampleLayerTxt)
        self.verticalLayout_16.addWidget(self.add2mapBox_6)
        self.add2mapBox_7 = QtGui.QGroupBox(self.elevationTab)
        self.add2mapBox_7.setObjectName(_fromUtf8("add2mapBox_7"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.add2mapBox_7)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.profileLineSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_7)
        self.profileLineSaveMemoryChk.setChecked(False)
        self.profileLineSaveMemoryChk.setObjectName(_fromUtf8("profileLineSaveMemoryChk"))
        self.verticalLayout_15.addWidget(self.profileLineSaveMemoryChk)
        self.profileLineSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_7)
        self.profileLineSavetoFileChk.setEnabled(True)
        self.profileLineSavetoFileChk.setChecked(True)
        self.profileLineSavetoFileChk.setObjectName(_fromUtf8("profileLineSavetoFileChk"))
        self.verticalLayout_15.addWidget(self.profileLineSavetoFileChk)
        self.label_9 = QtGui.QLabel(self.add2mapBox_7)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_15.addWidget(self.label_9)
        self.profileLineLayerTxt = QtGui.QLineEdit(self.add2mapBox_7)
        self.profileLineLayerTxt.setObjectName(_fromUtf8("profileLineLayerTxt"))
        self.verticalLayout_15.addWidget(self.profileLineLayerTxt)
        self.verticalLayout_16.addWidget(self.add2mapBox_7)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem7)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntElevationSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.elevationTab, icon7, _fromUtf8(""))
        self.verticalLayout.addWidget(self.settingsTab)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDlg.reject)
        QtCore.QObject.connect(self.proxyChk, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.hostTxt.setEnabled)
        QtCore.QObject.connect(self.proxyChk, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.portTxt.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(settingsDlg)

    def retranslateUi(self, settingsDlg):
        settingsDlg.setWindowTitle(_translate("settingsDlg", "Instellingen", None))
        self.networkSettings.setTitle(_translate("settingsDlg", "Netwerk -  Proxy", None))
        self.label_6.setText(_translate("settingsDlg", "Host: ", None))
        self.hostTxt.setPlaceholderText(_translate("settingsDlg", "http://yourProxy", None))
        self.portTxt.setPlaceholderText(_translate("settingsDlg", "bv: 8080", None))
        self.label_5.setText(_translate("settingsDlg", "Poort:", None))
        self.label_7.setText(_translate("settingsDlg", "Herstart qgis om deze instellingen te gebruiken.", None))
        self.proxyChk.setText(_translate("settingsDlg", "Netwerk proxy gebruiken", None))
        self.label.setText(_translate("settingsDlg", "Timeout: ", None))
        self.timeOutBox.setSuffix(_translate("settingsDlg", " seconden", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.generalTab), _translate("settingsDlg", "Algemeen", None))
        self.searchOptionsBox_1.setTitle(_translate("settingsDlg", "Zoeken naar adressen", None))
        self.adresSearchOnEditChk.setText(_translate("settingsDlg", "Zoeken bij elke verandering in de zoektekst", None))
        self.adresSearchOnEnterChk.setText(_translate("settingsDlg", "Zoeken enkel als ENTER wordt ingedrukt", None))
        self.add2mapBox_1.setTitle(_translate("settingsDlg", "Toevoegen punten aan de kaart", None))
        self.adresSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.adresSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.label_1.setText(_translate("settingsDlg", "Naam  van de laag met adrespunten:", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.adresTab), _translate("settingsDlg", "Zoeken naar adressen", None))
        self.add2mapBox_2.setTitle(_translate("settingsDlg", "Toevoegen punten aan de kaart", None))
        self.reverseSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.reverseSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.label_2.setText(_translate("settingsDlg", "Naam  van de laag met adrespunten:", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.reverseTab), _translate("settingsDlg", "Prikken van een adres", None))
        self.add2mapBox_3.setTitle(_translate("settingsDlg", "Toevoegen punten aan de kaart", None))
        self.batchSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.batchSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.label_3.setText(_translate("settingsDlg", "Naam  van de laag met adrespunten:", None))
        self.maxRecordsLabel.setText(_translate("settingsDlg", "Maximaal aantal rijen dat inlezen mag worden: <br/>\n"
"(Grote bestanden kunnen de servers van AGIV belasten)", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.batchgeoCodeTab), _translate("settingsDlg", "CSV-adresbestanden geocoderen", None))
        self.add2mapBox_4.setTitle(_translate("settingsDlg", "Toevoegen punten aan de kaart", None))
        self.poiSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.poiSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.label_4.setText(_translate("settingsDlg", "Naam  van de laag met adrespunten:", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.poiTab), _translate("settingsDlg", "Zoeken naar plaatsen", None))
        self.add2mapBox_5.setTitle(_translate("settingsDlg", "Toevoegen punten aan de kaart", None))
        self.gipodSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.gipodSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.gipodTab), _translate("settingsDlg", "GIPOD", None))
        self.add2mapBox_6.setTitle(_translate("settingsDlg", "Toevoegen van sample punten aan de kaart", None))
        self.samplesSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.samplesSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.label_8.setText(_translate("settingsDlg", "Naam  van de laag met samplepunten:", None))
        self.add2mapBox_7.setTitle(_translate("settingsDlg", "Toevoegen van sample punten aan de kaart", None))
        self.profileLineSaveMemoryChk.setText(_translate("settingsDlg", "Opslaan naar tijdelijke laag", None))
        self.profileLineSavetoFileChk.setText(_translate("settingsDlg", "Opslaan naar bestand ", None))
        self.label_9.setText(_translate("settingsDlg", "Naam  van de laag met de profiellijn:", None))
        self.settingsTab.setItemText(self.settingsTab.indexOf(self.elevationTab), _translate("settingsDlg", "Hoogteprofiel", None))

import resources_rc
