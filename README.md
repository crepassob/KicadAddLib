# KicadAddLib

### 这是一个向Kicad添加符号，封装库以及3d模型的一个辅助程序
![image](https://user-images.githubusercontent.com/42341537/174654761-9fd4f20c-963f-4e36-a2a1-b2150214735e.png)

### 用途：

###### 批量添加符号，封装库以及3d模型到Kicad的全局库中。

### 使用方法：

###### 将包含 .lib,.step,.wrl,.kicad_mod 的压缩包拖入程序内，按下’+‘即可。不过需要注意，需要填写保存库的存放地址。这个地址可以是任何地方，但添加后此保存路径就无法更改，再次更改会导致Kicad无法找到文件。

###### 另外，如果导入的3d模型与封装的位置有所偏移，则需要勾选旋转调整。一般情况下，模型的偏移值为：-90，且只有一个轴需要勾选。

###### 例如，您使用：https://www.snapeda.com/ 来下载库，则需要勾选X轴。使用：LCKiConverter浏览器插件来下载库，则需要勾选Z轴（kicad5.x）。一般情况下，一类文件的旋转方向是固定的，不过有些3d模型需要手动调整，这与模型文件本身有关。

### 注意事项：

###### 如果导入3d模型错误，建议取消勾选添加3d模型。如果方向不对，则可以通过程序旋转对勾框以及kicad封装编辑器手动修改。

###### 如果您在使用中发现Kicad意外报错则需要删除 sym-lib-table和fp-lib-table 新添加的项目，可以点击按钮自行修改

------------------------------------------------------------------------------------------------------------------------------------

### This is the Kicad assist program which adds symbol, package library and 3d model 

### Use:

##### Add lots of symbol, package library and 3d model in the Kicad global libs

### Instructions:

##### Drag the compressed package containing .lib,.step,.wrl,.kicad_mod into the program and press'+'. However, it should be noted that you need to fill in the storage address of the repository. This address can be anywhere, but this save path cannot be changed after adding it, and changing it again will cause Kicad to fail to find the file.

##### In addition, if the imported 3d model is offset from the position of the package, you need to check the rotation adjustment. In general, the offset value of the model is: -90, and only one axis needs to be checked.

##### For example, if you use: https://www.snapeda.com/ to download the library, you need to tick the X axis. Use: LCKiConverter browser plug-in to download the library, you need to check the Z axis (kicad5.x). In general, the rotation direction of a class of files is fixed, but some 3D models need to be adjusted manually, which is related to the model file itself.

### Precautions:

##### If the imported 3d model is wrong, it is recommended to uncheck the add 3d model. If the orientation is wrong, it can be manually modified by programmatically rotating the check box and the kicad package editor.

##### If you find that Kicad unexpectedly reports an error during use, you need to delete the newly added items of sym-lib-table and fp-lib-table, you can click the button to modify it yourself
