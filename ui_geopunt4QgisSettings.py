# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_geopunt4QgisSettings.ui'
#
# Created: Sun Jan 19 15:56:47 2014
#      by: PyQt4 UI code generator 4.10.3
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
        settingsDlg.resize(421, 424)
        settingsDlg.setMinimumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntSettingsSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        settingsDlg.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(settingsDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.settingsTab = QtGui.QToolBox(settingsDlg)
        self.settingsTab.setFrameShape(QtGui.QFrame.NoFrame)
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.adresTab = QtGui.QWidget()
        self.adresTab.setGeometry(QtCore.QRect(0, 0, 403, 258))
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
        self.adresSavetoFileChk.setObjectName(_fromUtf8("adresSavetoFileChk"))
        self.verticalLayout_2.addWidget(self.adresSavetoFileChk)
        self.adresSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_1)
        self.adresSaveMemoryChk.setChecked(True)
        self.adresSaveMemoryChk.setObjectName(_fromUtf8("adresSaveMemoryChk"))
        self.verticalLayout_2.addWidget(self.adresSaveMemoryChk)
        self.label_1 = QtGui.QLabel(self.add2mapBox_1)
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.verticalLayout_2.addWidget(self.label_1)
        self.adresLayerTxt = QtGui.QLineEdit(self.add2mapBox_1)
        self.adresLayerTxt.setObjectName(_fromUtf8("adresLayerTxt"))
        self.verticalLayout_2.addWidget(self.adresLayerTxt)
        self.verticalLayout_3.addWidget(self.add2mapBox_1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntAddressSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.adresTab, icon1, _fromUtf8(""))
        self.reverseTab = QtGui.QWidget()
        self.reverseTab.setGeometry(QtCore.QRect(0, 0, 221, 141))
        self.reverseTab.setObjectName(_fromUtf8("reverseTab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.reverseTab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.add2mapBox_2 = QtGui.QGroupBox(self.reverseTab)
        self.add2mapBox_2.setObjectName(_fromUtf8("add2mapBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.add2mapBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.reverseSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_2)
        self.reverseSavetoFileChk.setObjectName(_fromUtf8("reverseSavetoFileChk"))
        self.verticalLayout_4.addWidget(self.reverseSavetoFileChk)
        self.reverseSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_2)
        self.reverseSaveMemoryChk.setChecked(True)
        self.reverseSaveMemoryChk.setObjectName(_fromUtf8("reverseSaveMemoryChk"))
        self.verticalLayout_4.addWidget(self.reverseSaveMemoryChk)
        self.label_2 = QtGui.QLabel(self.add2mapBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.reverseLayerTxt = QtGui.QLineEdit(self.add2mapBox_2)
        self.reverseLayerTxt.setObjectName(_fromUtf8("reverseLayerTxt"))
        self.verticalLayout_4.addWidget(self.reverseLayerTxt)
        self.verticalLayout_5.addWidget(self.add2mapBox_2)
        spacerItem1 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntReverse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.reverseTab, icon2, _fromUtf8(""))
        self.batchgeoCodeTab = QtGui.QWidget()
        self.batchgeoCodeTab.setGeometry(QtCore.QRect(0, 0, 371, 177))
        self.batchgeoCodeTab.setObjectName(_fromUtf8("batchgeoCodeTab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.batchgeoCodeTab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.add2mapBox_3 = QtGui.QGroupBox(self.batchgeoCodeTab)
        self.add2mapBox_3.setCheckable(False)
        self.add2mapBox_3.setObjectName(_fromUtf8("add2mapBox_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.add2mapBox_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.batchSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_3)
        self.batchSavetoFileChk.setObjectName(_fromUtf8("batchSavetoFileChk"))
        self.verticalLayout_9.addWidget(self.batchSavetoFileChk)
        self.batchSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_3)
        self.batchSaveMemoryChk.setChecked(True)
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
        self.maxRowsSpinBox.setProperty("value", 100)
        self.maxRowsSpinBox.setObjectName(_fromUtf8("maxRowsSpinBox"))
        self.horizontalLayout.addWidget(self.maxRowsSpinBox)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 70, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntBatchgeocodeSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.batchgeoCodeTab, icon3, _fromUtf8(""))
        self.poiTab = QtGui.QWidget()
        self.poiTab.setGeometry(QtCore.QRect(0, 0, 221, 141))
        self.poiTab.setObjectName(_fromUtf8("poiTab"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.poiTab)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.add2mapBox_4 = QtGui.QGroupBox(self.poiTab)
        self.add2mapBox_4.setObjectName(_fromUtf8("add2mapBox_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.add2mapBox_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.poiSavetoFileChk = QtGui.QRadioButton(self.add2mapBox_4)
        self.poiSavetoFileChk.setObjectName(_fromUtf8("poiSavetoFileChk"))
        self.verticalLayout_6.addWidget(self.poiSavetoFileChk)
        self.poiSaveMemoryChk = QtGui.QRadioButton(self.add2mapBox_4)
        self.poiSaveMemoryChk.setChecked(True)
        self.poiSaveMemoryChk.setObjectName(_fromUtf8("poiSaveMemoryChk"))
        self.verticalLayout_6.addWidget(self.poiSaveMemoryChk)
        self.label_4 = QtGui.QLabel(self.add2mapBox_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_6.addWidget(self.label_4)
        self.poiLayerTxt = QtGui.QLineEdit(self.add2mapBox_4)
        self.poiLayerTxt.setObjectName(_fromUtf8("poiLayerTxt"))
        self.verticalLayout_6.addWidget(self.poiLayerTxt)
        self.verticalLayout_7.addWidget(self.add2mapBox_4)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/geopunt4Qgis/images/geopuntPoiSmall.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsTab.addItem(self.poiTab, icon4, _fromUtf8(""))
        self.verticalLayout.addWidget(self.settingsTab)
        self.line = QtGui.QFrame(settingsDlg)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.buttonBox = QtGui.QDialogButtonBox(settingsDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(settingsDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settingsDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settingsDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(settingsDlg)

    def retranslateUi(self, settingsDlg):
        settingsDlg.setWindowTitle(_translate("settingsDlg", "Instellingen", None))
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

import resources_rc
