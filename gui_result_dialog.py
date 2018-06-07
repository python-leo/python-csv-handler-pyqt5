# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_result_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog


class Ui_Dialog_CSV_Data_Result(QDialog):  #: # (object):


    # Please note how to write the UI Class initialization method.

    def __init__(self):
        super(QDialog, self).__init__()
        self.result_window = QtWidgets.QMainWindow()
        pass


    color_test_file_count = 0
    step_test_file_count = 0
    shading_test_file_count = 0

    result_window = None

    result_csv_path = ""

    def set_color_test_file_count(self, file_count):
        self.color_test_file_count = file_count

    def set_step_test_file_count(self, file_count):
        self.step_test_file_count = file_count

    def set_shading_test_file_count(self, file_count):
        self.shading_test_file_count = file_count

    def set_result_csv_path(self, file_path):
        self.result_csv_path = file_path

    def setup_ui_notify_error(self, Dialog_CSV_Data_Result, error_text1):
        print("Debug Place 3")
        Dialog_CSV_Data_Result.setObjectName("Dialog_CSV_Data_Result")
        Dialog_CSV_Data_Result.resize(470, 557)

        self.textEdit_1_invalid_file_added = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_1_invalid_file_added.setGeometry(QtCore.QRect(60, 50, 341, 61))
        self.textEdit_1_invalid_file_added.setObjectName("textEdit_1_invalid_file_added")

        self.textEdit_2_color_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_2_color_test_result.setGeometry(QtCore.QRect(60, 210, 341, 61))
        self.textEdit_2_color_test_result.setObjectName("textEdit_2_color_test_result")

        self.textEdit_3_step_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_3_step_test_result.setGeometry(QtCore.QRect(60, 310, 341, 61))
        self.textEdit_3_step_test_result.setObjectName("textEdit_3_step_test_result")

        self.textEdit_4_shading_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_4_shading_test_result.setGeometry(QtCore.QRect(60, 410, 341, 61))
        self.textEdit_4_shading_test_result.setObjectName("textEdit_4_shading_test_result")

        self.retranslateUi_error_dialog(Dialog_CSV_Data_Result, error_text1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CSV_Data_Result)

    def retranslateUi_error_dialog(self, Dialog_CSV_Data_Result, error_text):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CSV_Data_Result.setWindowTitle(_translate("Dialog_CSV_Data_Result", "CSV数据处理结果"))
        print("Debug Place 4")
        """
        if self.color_test_file_count == 0 and self.shading_test_file_count == 0 and self.step_test_file_count == 0:
            self.textEdit_1_invalid_file_added.setTextColor(QtGui.QColor(200, 0, 0))
            self.textEdit_1_invalid_file_added.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_1_invalid_file_added.setText(_translate("Dialog_CSV_Data_Result", "错误：没有添加任何文件"))
        elif self.color_test_file_count < 0 or self.shading_test_file_count < 0 or self.step_test_file_count < 0:
            self.textEdit_1_invalid_file_added.setTextColor(QtGui.QColor(200, 0, 0))
            self.textEdit_1_invalid_file_added.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_1_invalid_file_added.setText(_translate("Dialog_CSV_Data_Result", "错误：添加的文件格式不正确"))
        """

        self.textEdit_1_invalid_file_added.setTextColor(QtGui.QColor(200, 0, 0))
        # self.textEdit_1_invalid_file_added.setFont(QFont("Times", 12, QFont.Normal))
        self.textEdit_1_invalid_file_added.setFontPointSize(16)
        self.textEdit_1_invalid_file_added.setText(_translate("Dialog_CSV_Data_Result", error_text))

        if self.color_test_file_count < -10:
            self.textEdit_2_color_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_2_color_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_2_color_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个色彩测试文件不是.csv文件" % abs(self.color_test_file_count) - 10
            print("text_str = " + text_str)
            self.textEdit_2_color_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 5")

        elif self.color_test_file_count < 0:
            self.textEdit_2_color_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_2_color_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_2_color_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个色彩测试文件内容不正确" % abs(self.color_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_2_color_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 6")
        else:
            print("Debug Place -7")
            if self.shading_test_file_count == 0:
                self.textEdit_2_color_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            else:
                self.textEdit_2_color_test_result.setTextColor(QtGui.QColor(0, 200, 0))
            print("Debug Place 7")

            # self.textEdit_2_color_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_2_color_test_result.setFontPointSize(16)
            text_str = "总共：添加%d个色彩测试文件" % abs(self.color_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_2_color_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))

        if self.step_test_file_count == -10:
            print("Debug Place -8")
            self.textEdit_3_step_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_3_step_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_3_step_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个灰阶测试文件不是.csv文件" % abs(1)
            print("text_str = " + text_str)
            self.textEdit_3_step_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 8")

        elif self.step_test_file_count < 0:
            print("Debug Place -9, abs(step_test_count) = %d " % abs(self.step_test_file_count))
            self.textEdit_3_step_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_3_step_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_3_step_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个灰阶测试文件内容不正确" % abs(self.step_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_3_step_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 9")
        else:
            if self.shading_test_file_count == 0:
                self.textEdit_3_step_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            else:
                self.textEdit_3_step_test_result.setTextColor(QtGui.QColor(0, 200, 0))

            # self.textEdit_3_step_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_3_step_test_result.setFontPointSize(16)
            text_str = "总共：添加%d个灰阶测试文件" % abs(self.step_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_3_step_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 10")

        if self.shading_test_file_count == -10:
            self.textEdit_4_shading_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_4_shading_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_4_shading_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个均匀度测试文件不是.csv文件" % abs(1)
            print("text_str = " + text_str)
            self.textEdit_4_shading_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 11")

        elif self.shading_test_file_count < 0:
            self.textEdit_4_shading_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            # self.textEdit_4_shading_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_4_shading_test_result.setFontPointSize(16)
            text_str = "错误：添加的第%d个均匀度测试文件内容不正确" % abs(self.shading_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_4_shading_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 12")
        else:
            if self.shading_test_file_count == 0:
                self.textEdit_4_shading_test_result.setTextColor(QtGui.QColor(200, 0, 0))
            else:
                self.textEdit_4_shading_test_result.setTextColor(QtGui.QColor(0, 200, 0))
            # self.textEdit_4_shading_test_result.setFont(QFont("Times", 12, QFont.Normal))
            self.textEdit_4_shading_test_result.setFontPointSize(16)
            text_str = "总共：添加%d个均匀度测试文件" % abs(self.shading_test_file_count)
            print("text_str = " + text_str)
            self.textEdit_4_shading_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
            print("Debug Place 13")

        self.textEdit_1_invalid_file_added.setDisabled(True)
        self.textEdit_2_color_test_result.setDisabled(True)
        self.textEdit_3_step_test_result.setDisabled(True)
        self.textEdit_4_shading_test_result.setDisabled(True)

    def setup_ui_show_open_file(self, Dialog_CSV_Data_Result):
        Dialog_CSV_Data_Result.setObjectName("Dialog_CSV_Data_Result")
        Dialog_CSV_Data_Result.resize(470, 557)
        self.textEdit_color_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_color_test_result.setGeometry(QtCore.QRect(60, 50, 341, 61))
        self.textEdit_color_test_result.setObjectName("textEdit_color_test_result")

        self.textEdit_2_step_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_2_step_test_result.setGeometry(QtCore.QRect(60, 150, 341, 61))
        self.textEdit_2_step_test_result.setObjectName("textEdit_2_step_test_result")

        self.textEdit_3_shading_test_result = QtWidgets.QTextEdit(Dialog_CSV_Data_Result)
        self.textEdit_3_shading_test_result.setGeometry(QtCore.QRect(60, 250, 341, 61))
        self.textEdit_3_shading_test_result.setObjectName("textEdit_3_shading_test_result")

        self.pushButton_open_csv_result_file = QtWidgets.QPushButton(Dialog_CSV_Data_Result)
        self.pushButton_open_csv_result_file.setGeometry(QtCore.QRect(60, 410, 341, 81))
        self.pushButton_open_csv_result_file.setObjectName("pushButton_open_csv_result_file")
        self.pushButton_open_csv_result_file.clicked.connect(self.open_result_csv_button_pressed)
        self.pushButton_open_csv_result_file.setFocus()

        self.retranslateUi(Dialog_CSV_Data_Result)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CSV_Data_Result)

    def retranslateUi(self, Dialog_CSV_Data_Result):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CSV_Data_Result.setWindowTitle(_translate("Dialog_CSV_Data_Result", "CSV数据处理结果"))
        self.pushButton_open_csv_result_file.setText(_translate("Dialog_CSV_Data_Result", "打开CSV结果文件"))
        self.pushButton_open_csv_result_file.setFont(QFont("Times", 16, QFont.Normal))

        self.textEdit_color_test_result.setTextColor(QtGui.QColor(0, 200, 0))
        # self.textEdit_color_test_result.setFont(QFont("Times", 12, QFont.Normal))
        self.textEdit_color_test_result.setFontPointSize(16)
        text_str = "总共：添加%d个色彩测试文件" % abs(self.color_test_file_count)
        print("text_str = " + text_str)
        self.textEdit_color_test_result.setText(
            _translate("Dialog_CSV_Data_Result", text_str))
        self.textEdit_color_test_result.setDisabled(True)

        self.textEdit_2_step_test_result.setTextColor(QtGui.QColor(0, 200, 0))
        # self.textEdit_2_step_test_result.setFont(QFont("Times", 12, QFont.Normal))
        self.textEdit_2_step_test_result.setFontPointSize(16)
        text_str = "总共：添加%d个灰阶测试文件" % abs(self.step_test_file_count)
        print("text_str = " + text_str)
        self.textEdit_2_step_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
        self.textEdit_2_step_test_result.setDisabled(True)

        self.textEdit_3_shading_test_result.setTextColor(QtGui.QColor(0, 200, 0))
        # self.textEdit_3_shading_test_result.setFont(QFont("Times", 12, QFont.Normal))
        self.textEdit_3_shading_test_result.setFontPointSize(16)
        text_str = "总共：添加%d个均匀度测试文件" % abs(self.shading_test_file_count)
        print("text_str = " + text_str)
        self.textEdit_3_shading_test_result.setText(_translate("Dialog_CSV_Data_Result", text_str))
        self.textEdit_3_shading_test_result.setDisabled(True)

    def open_result_csv_button_pressed(self):
        print("open result csv :  " + self.result_csv_path)

        """
        filename = filedialog.askopenfilename(initialdir=result_csv, filetypes=[('csv files', '.csv')])
        last_work_dir = os.path.dirname(filename)
        print("The path of selected file is  " + last_work_dir)
        """

        if os.path.exists(self.result_csv_path) and os.path.isfile(self.result_csv_path):
            os.startfile(self.result_csv_path)
        else:
            print("file does not exists")

        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()

    result_csv_file = os.getcwd() + os.path.sep + "result.csv"
    main_ui = Ui_Dialog_CSV_Data_Result()
    main_ui.set_color_test_file_count(1)
    main_ui.set_shading_test_file_count(1)
    main_ui.set_step_test_file_count(1)
    main_ui.set_result_csv_path(result_csv_file)

    main_ui.setup_ui_show_open_file(main_window)
    main_window.show()

    sys.exit(app.exec_())
    pass
