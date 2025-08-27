import pynput
import pyautogui
import os
import time
from pynput.keyboard import Controller  


keyboard =Controller()


file_type=input("Che tipo di file vuoi creare?").lower()
file_ext=''
#ADD HERE YOUR OTHER DESIRED EXTENTIONS
if file_type == 'cpp' or 'c++':
    file_ext='.cpp'
    path=os.path.expanduser('~/Desktop/cpp')
    MainDir='cpp'
    

elif file_type== 'py' or 'python':
    path=os.path.expanduser('~/Desktop/python')
    file_ext='.py'
    MainDir='python'
dir_num=1 
for name in os.listdir(path):
    full_path=os.path.join(path,name)
    if os.path.isdir(full_path)and name.startswith("prj"):
        dir_num+=1

prj_dir=f"prj{dir_num}"
print(prj_dir)
cd_cmd=f'cd Desktop-{MainDir}'
print(cd_cmd)
create_cmd=f'mkdir {prj_dir}'
print(create_cmd)
sec_cd_cmd=f'cd {prj_dir}'
final_cmd=f'nvim main{file_ext}'
pyautogui.hotkey('ctrl','alt','t')
time.sleep(1)
pyautogui.write(cd_cmd)
pyautogui.press('enter')

pyautogui.write(create_cmd)
pyautogui.press('enter')

pyautogui.write(sec_cd_cmd)
pyautogui.press('enter')

pyautogui.write(final_cmd)
pyautogui.press('enter')
