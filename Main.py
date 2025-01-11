import sys
import os
import cv2 as cv
import numpy as np
from PySide6.QtGui import QPixmap, QImage, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import pyqtgraph as pg
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from UI.ui_main import Ui_MainWindow
from Image_processing import attribute,threshold,noise,filtering,morphology,gradient,histogram,colorspace,frequency


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # 初始化界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 初始化参数
        self.last_width = 990
        self.last_height = 532
        self.img_input = None
        self.img_output = None
        # 左侧按钮
        self.ui.left_pushButton_1.clicked.connect(self.on_left_pushButton_1_clicked)# 属性变换
        self.ui.left_pushButton_2.clicked.connect(self.on_left_pushButton_2_clicked)# 阈值
        self.ui.left_pushButton_3.clicked.connect(self.on_left_pushButton_3_clicked)# 噪声
        self.ui.left_pushButton_4.clicked.connect(self.on_left_pushButton_4_clicked)# 滤波
        self.ui.left_pushButton_5.clicked.connect(self.on_left_pushButton_5_clicked)# 形态学
        self.ui.left_pushButton_6.clicked.connect(self.on_left_pushButton_6_clicked)# 梯度
        # 选择图片
        self.ui.file_path_pushButton.clicked.connect(self.on_file_path_pushButton_clicked)
        self.ui.file_path_lineEdit.returnPressed.connect(self.on_file_path_lineEdit_returnPressed)
        self.ui.file_determine_pushButton.clicked.connect(self.file_determine_pushButton_clicked)
        # 色彩空间切换
        self.ui.colorSpace_comboBox.currentIndexChanged.connect(self.on_colorSpace_comboBox)
        # 属性变换多选按钮
        self.ui.buttonGroup.buttonClicked.connect(self.buttonGroup_1_run_1)
        self.ui.buttonGroup.setExclusive(False)
        self.ui.doubleSpinBox.valueChanged.connect(self.buttonGroup_1_run_1)
        self.ui.horizontalSlider.valueChanged.connect(self.buttonGroup_1_run_2)
        self.ui.doubleSpinBox_2.valueChanged.connect(self.buttonGroup_1_run_1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.buttonGroup_1_run_2)
        self.ui.doubleSpinBox_3.valueChanged.connect(self.buttonGroup_1_run_1)
        self.ui.horizontalSlider_3.valueChanged.connect(self.buttonGroup_1_run_2)
        # 噪声添加多选按钮
        self.ui.buttonGroup_2.buttonClicked.connect(self.buttonGroup_2_run_1)
        self.ui.doubleSpinBox_6.valueChanged.connect(self.buttonGroup_2_run_2)
        self.ui.doubleSpinBox_7.valueChanged.connect(self.buttonGroup_2_run_2)
        self.ui.pushButton_4.clicked.connect(self.buttonGroup_2_run_1)
        self.ui.pushButton_5.clicked.connect(self.buttonGroup_2_run_1)
        # 阈值选项
        self.ui.spinBox_min.valueChanged.connect(self.threshold_run_1)
        self.ui.spinBox_max.valueChanged.connect(self.threshold_run_1)
        self.ui.horizontalSlider_min.valueChanged.connect(self.threshold_run_2)
        self.ui.horizontalSlider_max.valueChanged.connect(self.threshold_run_2)
        # 滤波多选按钮
        self.ui.buttonGroup_3.buttonClicked.connect(self.buttonGroup_3_run)
        self.ui.spinBox_3.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_4.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_8.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_5.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_6.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_7.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_12.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_9.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_10.valueChanged.connect(self.buttonGroup_3_run)
        self.ui.spinBox_11.valueChanged.connect(self.buttonGroup_3_run)
        # 形态学操作多选按钮
        self.ui.buttonGroup_4.buttonClicked.connect(self.buttonGroup_4_run)
        self.ui.spinBox_13.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_14.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_15.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_16.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_17.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_18.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_19.valueChanged.connect(self.buttonGroup_4_run)
        self.ui.spinBox_20.valueChanged.connect(self.buttonGroup_4_run)
        # 梯度算子多选按钮
        self.ui.buttonGroup_5.buttonClicked.connect(self.buttonGroup_5_run)
        self.ui.spinBox_21.valueChanged.connect(self.buttonGroup_5_run)
        self.ui.spinBox_22.valueChanged.connect(self.buttonGroup_5_run)
        self.ui.spinBox_23.valueChanged.connect(self.buttonGroup_5_run)
        self.ui.comboBox_4.currentIndexChanged.connect(self.buttonGroup_5_run)
        self.ui.comboBox_5.currentIndexChanged.connect(self.buttonGroup_5_run)
        self.ui.spinBox_24.valueChanged.connect(self.buttonGroup_5_run)

    # 阈值调用——1
    def threshold_run_1(self):
        thread_threshold = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_threshold.submit(threshold,self.img_input,
                                                            self.ui.spinBox_min.value(),
                                                            self.ui.spinBox_max.value()).result()
        thread_threshold.shutdown()
        self.ui.horizontalSlider_min.setValue(self.ui.spinBox_min.value())
        self.ui.spinBox_min.setValue(self.ui.horizontalSlider_min.value())
        self.ui.horizontalSlider_max.setValue(self.ui.spinBox_max.value())
        self.ui.spinBox_max.setValue(self.ui.horizontalSlider_max.value())
        self.output_img()
    
    # 阈值调用——2
    def threshold_run_2(self):
        thread_threshold = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_threshold.submit(threshold,self.img_input,
                                                            self.ui.spinBox_min.value(),
                                                            self.ui.spinBox_max.value()).result()
        thread_threshold.shutdown()
        self.ui.spinBox_min.setValue(self.ui.horizontalSlider_min.value())
        self.ui.horizontalSlider_min.setValue(self.ui.spinBox_min.value())
        self.ui.spinBox_max.setValue(self.ui.horizontalSlider_max.value())        
        self.ui.horizontalSlider_max.setValue(self.ui.spinBox_max.value())
        self.output_img()
    
    # 属性变换选项按钮调用——1
    def buttonGroup_1_run_1(self):
        thread_attribute = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_attribute.submit(attribute,self.img_input,
                                    self.ui.checkBox_brightness.isChecked(),
                                    self.ui.checkBox_contrast.isChecked(),
                                    self.ui.checkBox_saturation.isChecked(),
                                    b=self.ui.doubleSpinBox.value(),
                                    c=self.ui.doubleSpinBox_2.value(),
                                    s=self.ui.doubleSpinBox_3.value()).result()
        thread_attribute.shutdown()
        self.ui.horizontalSlider.setValue(self.ui.doubleSpinBox.value())
        self.ui.doubleSpinBox.setValue(self.ui.horizontalSlider.value())
        self.ui.horizontalSlider_2.setValue(self.ui.doubleSpinBox_2.value()*10)
        self.ui.doubleSpinBox_2.setValue(self.ui.horizontalSlider_2.value()*0.1)
        self.ui.horizontalSlider_3.setValue(self.ui.doubleSpinBox_3.value()*10)
        self.ui.doubleSpinBox_3.setValue(self.ui.horizontalSlider_3.value()*0.1)
        self.output_img()
    
    # 属性变换选项按钮调用——2
    def buttonGroup_1_run_2(self):
        thread_attribute = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_attribute.submit(attribute,self.img_input,
                                    self.ui.checkBox_brightness.isChecked(),
                                    self.ui.checkBox_contrast.isChecked(),
                                    self.ui.checkBox_saturation.isChecked(),
                                    b=self.ui.doubleSpinBox.value(),
                                    c=self.ui.doubleSpinBox_2.value(),
                                    s=self.ui.doubleSpinBox_3.value()).result()
        thread_attribute.shutdown()

        self.ui.doubleSpinBox.setValue(self.ui.horizontalSlider.value())
        self.ui.horizontalSlider.setValue(self.ui.doubleSpinBox.value())
        self.ui.doubleSpinBox_2.setValue(self.ui.horizontalSlider_2.value()*0.1)
        self.ui.horizontalSlider_2.setValue(self.ui.doubleSpinBox_2.value()*10)
        self.ui.doubleSpinBox_3.setValue(self.ui.horizontalSlider_3.value()*0.1)
        self.ui.horizontalSlider_3.setValue(self.ui.doubleSpinBox_3.value()*10)
        self.output_img()
    
    # 噪声添加选项按钮调用——1
    def buttonGroup_2_run_1(self):
        thread_noise = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_noise.submit(noise,self.img_input,
                                self.ui.radioButton_Gaussian.isChecked(),
                                self.ui.radioButton_Salt.isChecked(),
                                self.ui.radioButton_random.isChecked(),
                                mean=self.ui.doubleSpinBox_6.value(),
                                sigma=self.ui.doubleSpinBox_7.value(),
                                salt_rate=self.ui.doubleSpinBox_4.value(),
                                random_rate=self.ui.doubleSpinBox_5.value()).result()
        thread_noise.shutdown()
        self.output_img()
    
    # 噪声添加选项按钮调用——2
    def buttonGroup_2_run_2(self):
        if self.ui.radioButton_Salt.isChecked() or self.ui.radioButton_random.isChecked():
            pass
        else:
            thread_noise = ThreadPoolExecutor(max_workers=1)
            self.img_output = thread_noise.submit(noise,self.img_input,
                                    self.ui.radioButton_Gaussian.isChecked(),
                                    self.ui.radioButton_Salt.isChecked(),
                                    self.ui.radioButton_random.isChecked(),
                                    mean=self.ui.doubleSpinBox_6.value(),
                                    sigma=self.ui.doubleSpinBox_7.value(),
                                    salt_rate=self.ui.doubleSpinBox_4.value(),
                                    random_rate=self.ui.doubleSpinBox_5.value()).result()
            thread_noise.shutdown()
            self.output_img()
    
    # 滤波选项按钮调用
    def buttonGroup_3_run(self):
        thread_filtering = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_filtering.submit(filtering,self.img_input,
                                                            self.ui.radioButton_mean.isChecked(),
                                                            self.ui.radioButton_median.isChecked(),
                                                            self.ui.radioButton_Gaussian_2.isChecked(),
                                                            self.ui.radioButton_bilateral.isChecked(),
                                                            self.ui.spinBox_3.value(),
                                                            self.ui.spinBox_4.value(),
                                                            self.ui.spinBox_8.value(),
                                                            self.ui.spinBox_5.value(),
                                                            self.ui.spinBox_6.value(),
                                                            self.ui.spinBox_7.value(),
                                                            self.ui.spinBox_12.value(),
                                                            self.ui.spinBox_9.value(),
                                                            self.ui.spinBox_10.value(),
                                                            self.ui.spinBox_11.value()
                                                            ).result()
        thread_filtering.shutdown()
        self.output_img()
    
    # 形态学操作选项按钮调用
    def buttonGroup_4_run(self):
        thread_morphology = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_morphology.submit(morphology,self.img_input,
                                                   self.ui.radioButton_dilate.isChecked(),
                                                   self.ui.radioButton_etch.isChecked(),
                                                   self.ui.radioButton_open.isChecked(),
                                                   self.ui.radioButton_close.isChecked(),
                                                   self.ui.spinBox_13.value(),
                                                   self.ui.spinBox_14.value(),
                                                   self.ui.spinBox_15.value(),
                                                   self.ui.spinBox_16.value(),
                                                   self.ui.spinBox_17.value(),
                                                   self.ui.spinBox_18.value(),
                                                   self.ui.spinBox_19.value(),
                                                   self.ui.spinBox_20.value()).result()
        thread_morphology.shutdown()
        self.output_img()
    
    # 梯度算子选项按钮调用
    def buttonGroup_5_run(self):
        thread_gradient = ThreadPoolExecutor(max_workers=1)
        self.img_output = thread_gradient.submit(gradient,self.img_input,
                                                 self.ui.radioButton_Canny.isChecked(),
                                                 self.ui.radioButton_Laplacian.isChecked(),
                                                 self.ui.radioButton_scharr.isChecked(),
                                                 self.ui.radioButton_sobel.isChecked(),
                                                 self.ui.spinBox_21.value(),
                                                 self.ui.spinBox_22.value(),
                                                 self.ui.spinBox_23.value(),
                                                 self.ui.comboBox_4.currentText(),
                                                 self.ui.comboBox_5.currentText(),
                                                 self.ui.spinBox_24.value()).result()
        thread_gradient.shutdown()
        self.output_img()
    
    # 图像基本参数显示
    def set_attribute(self):
        if len(self.img_input.shape)==2:
            layer = 1
        else:
            layer = 3
        self.ui.layer_lineEdit.setText(str(layer))
        self.ui.width_lineEdit.setText(str(self.img_input.shape[1]))
        self.ui.high_lineEdit.setText(str(self.img_input.shape[0]))
        self.ui.type_lineEdit.setText(str(self.img_input.dtype))
    
    # 窗口尺寸实时监控
    def resizeEvent(self, event):
        # 获取新的窗口大小
        new_size = event.size()
        if new_size.width() != self.last_width or new_size.height() != self.last_height:
            self.last_width,self.last_height = new_size.width(), new_size.height()
            # 调整图像显示比例
            self.input_img()
            self.output_img()
    
    # input图像显示
    def input_img(self):
        if type(self.img_input) == np.ndarray:
            self.set_attribute()
            img = self.img_input
            img_scale = img.shape[1]/img.shape[0]
            self.on_Imgcolor_type()
            self.on_colorSpace_comboBox()
            label_scale = self.ui.input.width()/self.ui.input.height()
            img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            _image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out = QPixmap(_image).scaled(self.ui.input.height()*img_scale, self.ui.input.height())
            else:
                jpg_out = QPixmap(_image).scaled(self.ui.input.width(), self.ui.input.width()/img_scale)
            self.ui.input.setPixmap(jpg_out)
        else:
            pass
    
    # output图像显示
    def output_img(self):
        if type(self.img_output) == np.ndarray:
            img = self.img_output
            img_scale = img.shape[1]/img.shape[0]
            label_scale = self.ui.input.width()/self.ui.input.height()
            img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            _image = QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out = QPixmap(_image).scaled(self.ui.input.height()*img_scale, self.ui.input.height())
            else:
                jpg_out = QPixmap(_image).scaled(self.ui.input.width(), self.ui.input.width()/img_scale)
            self.ui.output.setPixmap(jpg_out)
        else:
            pass
    
    # 频域图像显示
    def frequency_output(self):
        if type(self.img_input) == np.ndarray:
            thread_frequency = ThreadPoolExecutor(max_workers=1)
            img = thread_frequency.submit(frequency,self.img_input).result()
            thread_frequency.shutdown()
            img_scale = img.shape[1]/img.shape[0]
            label_scale = self.ui.label_frequency.width()/self.ui.label_frequency.height()
            _image = QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out = QPixmap(_image).scaled(self.ui.label_frequency.height()*img_scale, self.ui.label_frequency.height())
            else:
                jpg_out = QPixmap(_image).scaled(self.ui.label_frequency.width(), self.ui.label_frequency.width()/img_scale)
            self.ui.label_frequency.setPixmap(jpg_out)
        else:
            pass
    
    # HSV图像显示
    def HSV_output(self):
        if type(self.img_input) == np.ndarray:
            thread_colorspace = ThreadPoolExecutor(max_workers=1)
            H,S,V = thread_colorspace.submit(colorspace,self.img_input,"HSV").result()
            thread_colorspace.shutdown()
            img_scale = self.img_input.shape[1]/self.img_input.shape[0]
            label_scale = self.ui.label_H.width()/self.ui.label_H.height()
            H_image = QImage(H[:], H.shape[1], H.shape[0], H.shape[1] * 3, QImage.Format_RGB888).copy()
            S_image = QImage(S[:], S.shape[1], S.shape[0], S.shape[1] * 3, QImage.Format_RGB888).copy()
            V_image = QImage(V[:], V.shape[1], V.shape[0], V.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out_H = QPixmap(H_image).scaled(self.ui.label_H.height()*img_scale, self.ui.label_H.height())
                jpg_out_S = QPixmap(S_image).scaled(self.ui.label_S.height()*img_scale, self.ui.label_S.height())
                jpg_out_V = QPixmap(V_image).scaled(self.ui.label_V.height()*img_scale, self.ui.label_V.height())
            else:
                jpg_out_H = QPixmap(H_image).scaled(self.ui.label_H.width(), self.ui.label_H.width()/img_scale)
                jpg_out_S = QPixmap(S_image).scaled(self.ui.label_S.width(), self.ui.label_S.width()/img_scale)
                jpg_out_V = QPixmap(V_image).scaled(self.ui.label_V.width(), self.ui.label_V.width()/img_scale)
            self.ui.label_H.setPixmap(jpg_out_H)
            self.ui.label_S.setPixmap(jpg_out_S)
            self.ui.label_V.setPixmap(jpg_out_V)
        else:
            pass
    
    # RGB图像显示
    def RGB_output(self):
        if type(self.img_input) == np.ndarray:
            thread_colorspace = ThreadPoolExecutor(max_workers=1)
            R,G,B = thread_colorspace.submit(colorspace,self.img_input,"RGB").result()
            thread_colorspace.shutdown()
            img_scale = self.img_input.shape[1]/self.img_input.shape[0]
            label_scale = self.ui.label_R.width()/self.ui.label_R.height()
            R_image = QImage(R[:], R.shape[1], R.shape[0], R.shape[1] * 3, QImage.Format_RGB888).copy()
            G_image = QImage(G[:], G.shape[1], G.shape[0], G.shape[1] * 3, QImage.Format_RGB888).copy()
            B_image = QImage(B[:], B.shape[1], B.shape[0], B.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out_R = QPixmap(R_image).scaled(self.ui.label_R.height()*img_scale, self.ui.label_R.height())
                jpg_out_G = QPixmap(G_image).scaled(self.ui.label_G.height()*img_scale, self.ui.label_G.height())
                jpg_out_B = QPixmap(B_image).scaled(self.ui.label_B.height()*img_scale, self.ui.label_B.height())
            else:
                jpg_out_R = QPixmap(R_image).scaled(self.ui.label_R.width(), self.ui.label_R.width()/img_scale)
                jpg_out_G = QPixmap(G_image).scaled(self.ui.label_G.width(), self.ui.label_G.width()/img_scale)
                jpg_out_B = QPixmap(B_image).scaled(self.ui.label_B.width(), self.ui.label_B.width()/img_scale)
            self.ui.label_R.setPixmap(jpg_out_R)
            self.ui.label_G.setPixmap(jpg_out_G)
            self.ui.label_B.setPixmap(jpg_out_B)
        else:
            pass
    
    # 灰度图显示
    def GRAY_output(self):
        if type(self.img_input) == np.ndarray:
            thread_colorspace = ThreadPoolExecutor(max_workers=1)
            img = thread_colorspace.submit(colorspace,self.img_input,"GRAY").result()
            thread_colorspace.shutdown()
            img_scale = img.shape[1]/img.shape[0]
            label_scale = self.ui.label_GRAY.width()/self.ui.label_GRAY.height()
            _image = QImage(img.data, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888).copy()
            if img_scale <= label_scale :
                jpg_out = QPixmap(_image).scaled(self.ui.label_GRAY.height()*img_scale, self.ui.label_GRAY.height())
            else:
                jpg_out = QPixmap(_image).scaled(self.ui.label_GRAY.width(), self.ui.label_GRAY.width()/img_scale)
            self.ui.label_GRAY.setPixmap(jpg_out)
        else:
            pass

    # 加载图片
    def load_img(self,filePath):
        if os.path.exists(filePath) == True:
            self.img_input = cv.imread(filePath)
            self.input_img()
        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '文件路径不存在！')
            msg_box.exec_()
    
    # 选择图片
    def on_file_path_pushButton_clicked(self):
        filePath,_ = QFileDialog.getOpenFileName(self,caption="选择图像",dir=os.getcwd(),filter="图像类型(*.png *.jpg)")
        self.ui.file_path_lineEdit.setText(filePath)
        self.load_img(filePath)
    
    # 文本框回车
    def on_file_path_lineEdit_returnPressed(self):
        self.load_img(self.ui.file_path_lineEdit.text())
    
    # 文件确定
    def file_determine_pushButton_clicked(self):
        self.load_img(self.ui.file_path_lineEdit.text())

    # 左侧按钮，切换参数配置页面
    def on_left_pushButton_1_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(0)
        self.buttonGroup_1_run_1()
        self.output_img()

    def on_left_pushButton_2_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(1)
        self.threshold_run_1()
        if type(self.img_input) == np.ndarray:
            if len(self.img_input.shape)==2:
                t = "GRAY"
                self.ui.label_56.setText(t)
            else:
                t = "RGB"
                self.ui.label_56.setText(t)
        self.output_img()

    def on_left_pushButton_3_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(2)
        self.buttonGroup_2_run_1()
        self.output_img()

    def on_left_pushButton_4_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(3)
        self.buttonGroup_3_run()
        self.output_img()

    def on_left_pushButton_5_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(4)
        self.img_output = morphology(self.img_input)
        self.output_img()

    def on_left_pushButton_6_clicked(self):
        self.ui.parameter_stackedWidget.setCurrentIndex(5)
        self.img_output = gradient(self.img_input)
        self.output_img()

    # 右侧色彩空间切换
    def on_colorSpace_comboBox(self):
        data = self.ui.colorSpace_comboBox.currentText()
        if data == "HSV":
            self.ui.colorSpace_stackedWidget.setCurrentIndex(0)
            self.HSV_output()
        elif data == "RGB":
            self.ui.colorSpace_stackedWidget.setCurrentIndex(1)
            self.RGB_output()
        elif data == "GRAY":
            self.ui.colorSpace_stackedWidget.setCurrentIndex(2)
            self.GRAY_output()
    # 右侧，直方图界面切换
    def on_Imgcolor_type(self):
        self.frequency_output()
        if len(self.img_input.shape) == 2:
            self.ui.histogram_stackedWidget.setCurrentIndex(0)
            thread_hist = ThreadPoolExecutor(max_workers=1)
            hist_gray = thread_hist.submit(histogram,self.img_input).result()
            thread_hist.shutdown()
            self.ui.widget1.plot(hist_gray.flatten())
        if len(self.img_input.shape) == 3:
            self.ui.histogram_stackedWidget.setCurrentIndex(1)
            thread_hist = ThreadPoolExecutor(max_workers=1)
            hist_R,hist_G,hist_B = thread_hist.submit(histogram,self.img_input).result()
            thread_hist.shutdown()
            penstate_b = pg.mkPen(width=2, color='b')
            penstate_g = pg.mkPen(width=2, color='g')
            penstate_r = pg.mkPen(width=2, color='r')
            self.ui.widget_2.plot(hist_R.flatten(),pen=penstate_r)
            self.ui.widget_3.plot(hist_G.flatten(),pen=penstate_g)
            self.ui.widget_4.plot(hist_B.flatten(),pen=penstate_b)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("UI/icons/LOGO.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())