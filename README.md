# PdfReaderPython

Edit the .spec file that should have been generated automatically.
Put from PyInstaller.utils.hooks import collect_data_files at the top. 
Replace the datas=[] with datas=collect_data_files("tabula"). 
Then rebuild using PyInstaller main.spec from now on.   yourfilename.spec 



For virtual environment access

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
 
 
venv/Scripts/activate.ps1
 
