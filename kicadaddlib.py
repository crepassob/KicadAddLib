#导入库
from win32.lib.win32con import *
from win32.win32api import *
from win32.win32gui import *
import random,os,time,sys,zipfile
from win32.lib.commctrl import *
from pythonwin import win32ui
import zipfile
import locale


file_path , content2str = '' , ''
a1,b1,c1 = [],[],[]
x_number,y_number,z_number = 0,0,0
openencoding = locale.getpreferredencoding()

WM_SEARCH_RESULT = WM_USER + 512
WM_SEARCH_FINISHED = WM_USER + 513

#自定义字体
lf = LOGFONT()
lf.lfFaceName = "微软雅黑"
lf.lfHeight = -DEVICE_DEFAULT_FONT + 2
lf.lfWeight = FW_REGULAR
hfont = CreateFontIndirect(lf)

lf1 = LOGFONT()
lf1.lfFaceName = "微软雅黑"
lf1.lfHeight = -DEVICE_DEFAULT_FONT +4
lf1.lfWeight = FW_REGULAR
hfont1 = CreateFontIndirect(lf1)
    
def finddoc(zip,path):
  global a1,b1,c1
  
  
  line = ['.lib','.step','.wrl','.kicad_mod']
  lines = []
  for x in zip.namelist():
    for y in line:
      if y in x :
        zip.extract(x,path)
        lines.append(x)

  for a11 in lines:
    number = GetDlgItemText(hwnd,3)
    if line[0] in a11:
      a1.append(a11)
      SendMessage(Ctrl4,WM_SETTEXT,0, number + '\r\n' + a11)
    if line[1] in a11 or line[2] in a11:
      b1.append(a11)
      SendMessage(Ctrl4,WM_SETTEXT,0, number + '\r\n' + a11)
    if line[3] in a11:
      c1.append(a11)
      SendMessage(Ctrl4,WM_SETTEXT,0, number + '\r\n' + a11)

def filmsexecute(Userpath,content,number):
      #z.zipfile.extractall(path+'/')
          
  line = []
  line = open(Userpath,'r',encoding=openencoding)
  lines = line.readlines()
  
  count = len(lines) - number
  lines.insert(count,content)

  str1 = ''.join(lines)
  line = open(Userpath,'w',encoding=openencoding)
  line.write(str1)
  line.close()

def WndClass0(hwnd, msg, wParam, lParam):
    
    #关闭销毁窗口
    if msg == WM_DESTROY:
      openfile = []
      open1 = GetDlgItemText(hwnd,0)
      open2 = GetDlgItemText(hwnd,10)
      x_choose = SendMessage (Ctrl8, BM_GETCHECK, 0, 0)
      y_choose = SendMessage (Ctrl9, BM_GETCHECK, 0, 0)
      z_choose = SendMessage (Ctrl10, BM_GETCHECK, 0, 0)
      openfile.append(str(open1)+ ' ')
      openfile.append(str(open2) + ' ')
      openfile.append(str(x_choose) + ' ')
      openfile.append(str(y_choose) + ' ')
      openfile.append(str(z_choose))
      str1 = ''.join(openfile)
      configtxt = open(configfile + 'config.txt','w',encoding=openencoding)
      configtxt.write(str1)
      configtxt.close()
      
      PostQuitMessage(0)
    if msg == WM_DROPFILES:
      
      path = GetDlgItemText(hwnd,0)
      file = DragQueryFile(wParam,0)
      SendMessage(Ctrl4,WM_SETTEXT,0,file)
      #number = GetDlgItemText(hwnd,3)
      try :
        ziplist = zipfile.ZipFile(file, 'r')
        SendMessage(Ctrl3,WM_SETREDRAW,TRUE,0)
        finddoc(ziplist,path)
      except:
        MessageBox(hwnd,"导入的ZIP有误，请导入包含 .lib,.step,.wrl,.kicad_mod 的ZIP","提示",MB_OK | MB_ICONERROR)
        SendMessage(Ctrl3,WM_SETREDRAW,FALSE,0)
    if msg == WM_COMMAND:
      def click_1():
        global x_number,y_number,z_number,content2str
        path = GetDlgItemText(hwnd,0)
        path1 = GetDlgItemText(hwnd,3)
        pathzip = path1.split('\r\n')
        
        z = zipfile.ZipFile(pathzip[0], 'r') 

        x_choose = SendMessage (Ctrl8, BM_GETCHECK, 0, 0)
        y_choose = SendMessage (Ctrl9, BM_GETCHECK, 0, 0)
        z_choose = SendMessage (Ctrl10, BM_GETCHECK, 0, 0)
        rotate = GetDlgItemText(hwnd,10)
        
        if x_choose == 1:
          x_number = rotate
        if y_choose == 1:
          y_number = rotate        
        if z_choose == 1:
          z_number = rotate
                  
        Userpath1 = "C:\\Users\\"+os.environ['USERNAME']+"\\AppData\\Roaming\\kicad\\sym-lib-table" + '.'
        Userpath2 = "C:\\Users\\"+os.environ['USERNAME']+"\\AppData\\Roaming\\kicad\\fp-lib-table" + '.'
        
        folder = os.path.exists(path)
        if not folder:
          os.makedirs(path)
          print('built success')
        else :
          print('not built')

        for libname in a1 :
          libname1 = (((libname.split('/'))[-1]).split('.'))[0]
          
          content1 = '  (lib (name ' + libname1 + ')(type Legacy)(uri ' + path + '/' + libname + ')(options "")(descr "")) \n'
          filmsexecute(Userpath1,content1,1)
        
        for libname in c1:
          Userpath3 =  path + '/' + libname
          listfile1 = []
          
          
          try :
            list1 = libname.split('/')
            list1.pop()
            list2 = (list1[-1].split('.'))[0]
            for listfile in list1:
              listfile = '/' + listfile
              listfile1.append(listfile)
            c11 = ''.join(listfile1)
          except:
            list1 = libname.split('/')
            list2 = (list1[-1].split('.'))[0]
            c11 = ''
          
          content2 = '  (lib (name ' + list2 + ')(type KiCad)(uri ' + path  + c11 + ')(options "")(descr "")) \n'
          
          if content2 != content2str:
            filmsexecute(Userpath2,content2,1)
          
          content2str = content2
        for libname in b1:
          Userpath4 =  path + '/' + libname
          content3 = '\n (model ' + Userpath4 +' (offset (xyz 0 0 0)) (scale (xyz 1 1 1)) (rotate (xyz '+str(x_number)+' '+str(y_number)+' '+str(z_number)+')))'
          filmsexecute(Userpath3,content3,1)
        
        MessageBox(hwnd,"执行完成！","提示",MB_OK | MB_ICONINFORMATION)
        
      Click_Command = {
            2 : click_1 
        }
      if LOWORD(wParam) in Click_Command :
        Click_Command[LOWORD(wParam)]()
    #返回
    return DefWindowProc(hwnd, msg, wParam, lParam)

wcex = WNDCLASS()
hinst = dllhandle
#wcex.SetDialogProc()

wcex.hbrBackground  = COLOR_3DFACE + 1;
wcex.style          = CS_HREDRAW | CS_VREDRAW |CS_GLOBALCLASS;
wcex.hInstance      = hinst
wcex.lpfnWndProc    = DefWindowProc;
#wcex.hIcon          = LoadIcon(GetModuleHandle(None), 1)
wcex.hCursor        = LoadCursor(0, IDC_ARROW)
wcex.lpszClassName  = 'Class0'
wcex.lpfnWndProc    = WndClass0

class_atom = RegisterClass(wcex)
#创建窗口
hwnd = CreateWindowEx(WS_EX_ACCEPTFILES,class_atom, u'kicad批量导入', WS_POPUP |WS_VISIBLE | WS_CAPTION | WS_SYSMENU | DS_SETFONT  | WS_MINIMIZEBOX, 0, 0, 400,200,0,0, 0, None)

Ctrl1 = CreateWindowEx(0, "EDIT", (""), WS_VISIBLE | WS_CHILD | WS_TABSTOP | WS_BORDER | ES_AUTOHSCROLL, 118, 135, 261, 21, hwnd, 0, None, None);
Ctrl2 = CreateWindowEx(0, "Static", ("导入存放地址："), WS_VISIBLE | WS_CHILD | WS_GROUP | SS_LEFT, 10, 135, 85, 21, hwnd, 1, None, None);
Ctrl3 = CreateWindowEx(0, "BUTTON", ("+"), WS_VISIBLE | WS_CHILD | WS_TABSTOP | 0x00000001, 90, 135, 21, 21, hwnd, 2, None, None);
Ctrl4 = CreateWindowEx(0,"EDIT",(""),  WS_VISIBLE | WS_CHILD | WS_BORDER | ES_AUTOHSCROLL |ES_MULTILINE |ES_READONLY | WS_VSCROLL, 118, 10, 261, 95, hwnd, 3, None, None)
Ctrl5 = CreateWindowEx(0, "Static", ("拖入zip"), WS_VISIBLE | WS_CHILD | WS_GROUP | SS_LEFT, 30, 50, 61, 51, hwnd, 4, None, None);
Ctrl6 = CreateWindowEx(0, "Static", ("3d旋转调整："), WS_VISIBLE | WS_CHILD | WS_GROUP | SS_LEFT, 10, 110, 76, 21, hwnd, 5, None, None);
Ctrl7 = CreateWindowEx(0, "Static", ("偏移值："), WS_VISIBLE | WS_CHILD | WS_GROUP | SS_LEFT, 260, 112, 54, 21, hwnd, 6,None, None);
Ctrl8 = CreateWindowEx(0, "BUTTON", ("X轴"), WS_VISIBLE | WS_CHILD | WS_TABSTOP | 0x00000003, 118, 110, 41, 21, hwnd, 7, None, None);
Ctrl9 = CreateWindowEx(0, "BUTTON", ("Y轴"), WS_VISIBLE | WS_CHILD | WS_TABSTOP | 0x00000003, 168, 110, 41, 21, hwnd, 8, None, None);
Ctrl10 = CreateWindowEx(0, "BUTTON", ("Z轴"), WS_VISIBLE | WS_CHILD | WS_TABSTOP | 0x00000003, 218, 110, 41, 21, hwnd, 9, None, None);
Ctrl11 = CreateWindowEx(0, "EDIT", (""), WS_VISIBLE | WS_CHILD | WS_TABSTOP | WS_BORDER | ES_AUTOHSCROLL, 310, 110, 51, 21, hwnd, 10, None, None);

SendMessage(Ctrl1, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl2, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl3, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl4, WM_SETFONT,hfont1,FALSE);
SendMessage(Ctrl5, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl6, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl7, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl8, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl9, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl10, WM_SETFONT,hfont,FALSE);
SendMessage(Ctrl11, WM_SETFONT,hfont,FALSE);

configfile = "C:\\Users\\"+os.environ['USERNAME']+"\\AppData\\Roaming\\KicadAddLib\\"
folder = os.path.exists(configfile)

print(openencoding)

if not folder:
  os.makedirs(configfile)
  configtxt = open(configfile + 'config.txt','w',encoding=openencoding)
  SendMessage (Ctrl11,WM_SETTEXT,0,'-90')
else :
  configtxt = open(configfile + 'config.txt','r',encoding=openencoding)
  configopen = configtxt.readlines()
  print(configopen)
  configopen1 = ''.join(configopen)
  configopen = configopen1.split(' ')

  SendMessage (Ctrl1,WM_SETTEXT,0,configopen[0])
  SendMessage (Ctrl11,WM_SETTEXT,0,configopen[1])
  SendMessage (Ctrl8, BM_SETCHECK,int(configopen[2]),0)
  SendMessage (Ctrl9, BM_SETCHECK,int(configopen[3]),0)
  SendMessage (Ctrl10, BM_SETCHECK,int(configopen[4]),0)
#显示窗口
UpdateWindow(hwnd); 
ShowWindow(hwnd,SW_SHOWNORMAL)
PumpMessages()

'''
dlg = win32ui.CreateFileDialog(1)
dlg.SetOFNInitialDir("默认打开路径")
dlg.DoModal()
path = dlg.GetPathName()

'''

