from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib
import subprocess
import os
from gui import GUI
import sys
print("Start")
UIinterpreter=GUI.ui
mainwindowInt=GUI.MainWindow

class Funcs:
    def __init__(self,directorycheck:str,MYDIR:str,renderformat:str) -> None:
        self.directorycheck=directorycheck
        self.MYDIR=MYDIR
        self.renderformat=renderformat

    def renderexec(self):
        print(self.directorycheck)
        if self.directorycheck==self.MYDIR:
            mainwindowInt.close()
            subprocess.run(["blender","-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
        else:
            mainwindowInt.close()
            subprocess.run(["./blender","-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
            

    def blenddirselect(self):
        self.directorycheck = QtWidgets.QFileDialog.getExistingDirectory(mainwindowInt)
        os.chdir(self.directorycheck)
        UIinterpreter.execloc.setText(f"{os.getcwd()}")

    def renderdirselect(self):
        self.renderdirectory, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Open " + f"{self.renderformat} File", '.', f"(*.{self.renderformat}.)")
        fout = open(f"{self.MYDIR}/subscripts/render_dir.txt", "wt")
        fout.write(f"{self.renderdirectory}")
        fout.close()
        UIinterpreter.label_7.setText(f"{self.renderdirectory}")

    def svgopen(self):
        svgdirectory, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Open " + " SVG File", '.', "(*.svg)")
        fout = open(f"{self.MYDIR}/subscripts/svg_dir.txt", "wt")
        fout.write(f"{svgdirectory}")
        fout.close()
        UIinterpreter.svgloc.setText(f"{svgdirectory}")
    
    def eeveecall(self):
        fout = open(f"{self.MYDIR}/subscripts/renderengine_selector.txt", "wt")
        fout.write('BLENDER_EEVEE')
        fout.close()

    def cyclescall(self):
        fout = open(f"{self.MYDIR}/subscripts/renderengine_selector.txt", "wt")
        fout.write('CYCLES')
        fout.close()
    
    def jpegcall(self):
        self.renderformat="JPEG"
        print("Format set to JPEG")

    def pngcall(self):
        self.renderformat="PNG"
        print("Format set to PNG")
    
    def samplerval(self):
        fout = open(f"{self.MYDIR}/subscripts/samples.txt", "wt")
        fout.write(str(UIinterpreter.samplerselect.value()))
        UIinterpreter.label_9.setText(str(UIinterpreter.samplerselect.value()))
        fout.close()

    def hex(self):
        color = QtWidgets.QColorDialog.getColor()
        rgb=color.getRgbF()
        fout = open(f"{self.MYDIR}/subscripts/hex.txt", "wt")
        fout.write(str(rgb))
        fout.close()

Funcsrunner=Funcs(f"{pathlib.Path(__file__).parent.absolute()}",f"{pathlib.Path(__file__).parent.absolute()}","PNG")
UIinterpreter.pushButton_5.clicked.connect(Funcsrunner.renderexec)
UIinterpreter.blendlocselect.clicked.connect(Funcsrunner.blenddirselect)
UIinterpreter.SVGselector.clicked.connect(Funcsrunner.svgopen)
UIinterpreter.Cyclesselector.toggled.connect(Funcsrunner.cyclescall)
UIinterpreter.Eeveeselector.toggled.connect(Funcsrunner.eeveecall)
UIinterpreter.samplerselect.valueChanged.connect(Funcsrunner.samplerval)
UIinterpreter.renderlocselect.clicked.connect(Funcsrunner.renderdirselect)
UIinterpreter.jpegselect.toggled.connect(Funcsrunner.jpegcall)
UIinterpreter.pngselect.toggled.connect(Funcsrunner.pngcall)
UIinterpreter.pushButton.clicked.connect(Funcsrunner.hex)

def sampler():
    UIinterpreter.samplerselect.setRange(100,3000)
    UIinterpreter.samplerselect.setValue(2000)
    UIinterpreter.samplerselect.setTickInterval(50)
sampler()
appInt=GUI.app
sys.exit(appInt.exec_())

