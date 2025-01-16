# OpenCV-DIP-Show

## 项目简介

OpenCV DIP Show is demonstration software for digital image processing built on OpenCV. It uses Python as the development language and PySide6 for the user interface, showcasing the fundamental operations in digital image processing.

OpenCV DIP Show 是一款基于 OpenCV 的数字图像处理演示软件。该软件使用 Python 作为开发语言，并采用 PySide6 构建用户界面，能够展示数字图像处理中的基本操作。

## 功能特点

1. **图像属性变换** ：调整亮度、对比度和饱和度。
2. **阈值处理** ：设置最小和最大阈值，生成二值化图像。
3. **噪声添加** ：添加高斯噪声、椒盐噪声或随机噪声。
4. **滤波操作** ：应用均值滤波、中值滤波、高斯滤波和双边滤波。
5. **形态学操作** ：膨胀、腐蚀、开运算和闭运算。
6. **梯度计算** ：使用 Canny、Laplacian、Scharr 和 Sobel 算子计算图像梯度。
7. **色彩空间转换** ：支持 RGB、HSV 和灰度图之间的转换。
8. **频域显示** ：显示图像的频域表示。
9. **直方图分析** ：绘制并显示图像的灰度直方图或彩色直方图。

## 安装依赖

为了确保项目正常运行，请确保已安装以下依赖库。你可以使用 `pip` 来安装这些依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

1. **启动程序**
   * 打开终端或命令行，导航到项目目录。
   * 运行 `python Main.py` 启动应用程序。
2. **加载图片**
   * 点击“选择图片”按钮，从文件系统中选择要处理的图像。
   * 或者直接在文件路径输入框中输入图片路径，然后按回车键或点击“确定”按钮加载图片。
3. **切换功能页面**
   * 使用左侧的功能按钮（属性变换、阈值、噪声、滤波、形态学、梯度）切换不同的参数配置页面。
   * 在右侧的色彩空间下拉菜单中选择不同的色彩空间（RGB、HSV、GRAY），以查看不同色彩空间下的图像。
4. **实时预览**
   * 调整各个参数后，图像处理结果会实时显示在输出窗口中。
   * 可以通过调整滑块或输入框中的数值来观察不同参数对图像的影响。

## 打包成可执行文件

#### 使用 PyInstaller 打包项目

为了将项目打包成独立的可执行文件，可以使用 `PyInstaller` 工具。根据 `packaged.txt` 文件中的指令，以下是打包步骤：

1. **创建可执行文件（无控制台窗口）**

   ```bash
   pyinstaller Main.py --noconsole --icon="UI/icons/LOGO.ico"
   ```
2. **创建可执行文件（带所有依赖项，无控制台窗口）**

   ```bash
   pyinstaller -D Main.py --noconsole --icon="UI/icons/LOGO.ico"
   ```

打包完成后，生成的可执行文件及其依赖项将位于 `dist` 目录中。你可以将该目录分发给其他用户，而无需他们安装 Python 或任何依赖项。

#### 注意事项

* 确保 `UI/icons/LOGO.ico` 文件路径正确，否则图标可能无法正确应用。
* 如果项目中有其他资源文件（如图像、配置文件等），请确保它们也被正确包含在打包过程中。可以在 `pyinstaller` 命令中使用 `--add-data` 参数来添加额外的资源文件。或者在打包结束后手动将相关缺失资源拷贝到可执行程序同级目录。

## 文件结构

```
OpenCV-DIP-Show/
├── Main.py                  # 主程序入口
├── UI/                      # 用户界面设计文件
│   └── ui_main.py           # 主界面UI文件
├── Image_processing.py      # 图像处理模块
├── requirements.txt         # 项目依赖文件
├── packaged.txt             # 打包指令文件
└── README.md                # 项目说明文档
```

## 注意事项

* 请确保所使用的图像路径正确无误。
* 如果遇到性能问题，可以尝试减少图像尺寸或优化代码逻辑。
* 本项目使用多线程处理图像，以提高响应速度，但请注意不要过度创建线程池，以免影响系统性能。

## 联系方式

如需帮助或有任何问题，请联系 [ai.engineer.chengfang@gmail.com] 或提交 Issue。

---

希望这个 README 文档能帮助你更好地理解和使用 OpenCV-DIP-Show 项目！
