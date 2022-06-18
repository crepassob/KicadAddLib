# KicadAddLib

### 这是一个向Kicad添加符号，封装库以及3d模型的一个辅助程序

### 用途：

###### 批量添加符号，封装库以及3d模型到Kicad的全局库中。

### 使用方法：

###### 将包含 .lib,.step,.wrl,.kicad_mod 的压缩包拖入程序内，按下’+‘即可。不过需要注意，需要填写保存库的存放地址。这个地址可以是任何地方，但添加后此保存路径就无法更改，再次更改会导致Kicad无法找到文件。

###### 另外，如果导入的3d模型与封装的位置有所偏移，则需要勾选旋转调整。一般情况下，模型的偏移值为：-90，且只有一个轴需要勾选。

###### 例如，您使用：https://www.snapeda.com/ 来下载库，则需要勾选X轴。使用：LCKiConverter浏览器插件来下载库，则需要勾选Z轴。

### 注意事项：

###### 如果您所在的地区没有使用 utf-8 编码格式，会导致Kicad报错。如果您想要继续使用，则需要修改kicadaddlib.py 的第13行编码格式，并修改 C:\Users\ '用户名' \AppData\Roaming\kicad\ 其中的 ： sym-lib-table和fp-lib-table 的编码格式。

###### 如果您在使用中发现Kicad意外报错则需要删除 sym-lib-table和fp-lib-table 新添加的项目，并注意括号的数量。本人使用上述网址以及插件能够正常运行，不保证其他网站下载的压缩包能够正确添加。

### 后言：

###### 这只是本人随手随便写的程序，不保证其他情况能够正确运行，如果无法使用请自行修改或绕行。

------------------------------------------------------------------------------------------------------------------------------------

### This is the Kicad assist program which adds symbol, package library and 3d model 

### Use:

##### Add lots of symbol, package library and 3d model in the Kicad global libs

### Instructions:

##### Drag the compressed package containing .lib,.step,.wrl,.kicad_mod into the program and press'+'. However, it should be noted that you need to fill in the storage address of the repository. This address can be anywhere, but this save path cannot be changed after adding it, and changing it again will cause Kicad to fail to find the file.

##### In addition, if the imported 3d model is offset from the position of the package, you need to check the rotation adjustment. In general, the offset value of the model is: -90, and only one axis needs to be checked.

##### For example, if you use: https://www.snapeda.com/ to download the library, you need to tick the X axis. Use: LCKiConverter browser plugin to download the library, you need to check the Z axis.

### Precautions:

##### If your region does not use the utf-8 encoding format, Kicad will report an error. If you want to continue using it, you need to modify the encoding format of line 13 of kicadaddlib.py, and modify C:\Users\ 'username' \AppData\Roaming\kicad\ in a sym-lib-table and fp-lib-table.

##### If you find that Kicad unexpectedly reports an error during use, you need to delete the newly added items of sym-lib-table and fp-lib-table, and pay attention to the number of brackets. I use the above URL and plug-ins to run normally, and I do not guarantee that the compressed packages downloaded from other websites can be added correctly.
