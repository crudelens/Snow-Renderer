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
    def __init__(self,directorycheck:str,MYDIR:str,renderformat:str,svgdirectory:list) -> None:
        self.directorycheck=directorycheck
        self.MYDIR=MYDIR
        self.renderformat=renderformat
        self.svgdirectory=svgdirectory

    def renderanim(self):
        print(self.directorycheck)
        fout = open(f"{self.MYDIR}/subscripts/optionanim.txt", "wt")
        fout.write("anim")
        fout.close()
        for i in range(0,len(self.svgdirectory)):
            if self.directorycheck==self.MYDIR:
                subprocess.run(["blender", "-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
                for j in range(0,len(self.svgdirectory)):
                    if os.path.isfile(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt"):
                        os.remove(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt")
                        print(f"file {i+1} processed")
                        break
            else:
                subprocess.run(["./blender", "-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
                for j in range(0,len(self.svgdirectory)):
                    if os.path.isfile(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt"):
                        os.remove(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt")
                        break
    
    def renderstill(self):
        print(self.directorycheck)
        fout = open(f"{self.MYDIR}/subscripts/optionanim.txt", "wt")
        fout.write("still")
        fout.close()
        for i in range(0,len(self.svgdirectory)):
            if self.directorycheck==self.MYDIR:
                subprocess.run(["blender", "-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
                for j in range(0,len(self.svgdirectory)):
                    if os.path.isfile(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt"):
                        os.remove(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt")
                        print(f"file {i+1} processed")
                        break
            else:
                subprocess.run(["./blender", "-b", f"{self.MYDIR}/snowflake.blend", "-P", f"{self.MYDIR}/main.py", "-F", f"{self.renderformat}"])
                for j in range(0,len(self.svgdirectory)):
                    if os.path.isfile(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt"):
                        os.remove(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{j}.txt")
                        break

    def blenddirselect(self):
        self.directorycheck = QtWidgets.QFileDialog.getExistingDirectory(mainwindowInt)
        os.chdir(self.directorycheck)
        UIinterpreter.execloc.setText(f"{os.getcwd()}")

    def renderdirselect(self):
        self.renderdirectory = QtWidgets.QFileDialog.getExistingDirectory(None)
        #self.renderdirectory, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Open " + f"{self.renderformat} File", '.', f"(*.{self.renderformat}.)")
        fout = open(f"{self.MYDIR}/subscripts/render_dir.txt", "wt")
        fout.write(f"{self.renderdirectory}")
        fout.close()
        UIinterpreter.label_7.setText(f"{self.renderdirectory}")

    def svgopen(self):
        self.svgdirectory, __filter = QtWidgets.QFileDialog.getOpenFileNames(None, "Open " + "SVG File", '.', "(*.svg)")
        print(len(self.svgdirectory))
        for i in range(0,len(self.svgdirectory)):
            fout = open(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/svg_dir{i}.txt", "wt")
            fout.write(f"{self.svgdirectory[i]}")
            fout.close()
            UIinterpreter.listWidget.insertItem(i,self.svgdirectory[i])
        nooffiles= len(os.listdir(f"{self.MYDIR}/subscripts/SVG DIRECTORIES/"))
        fout2 = open(f"{self.MYDIR}/subscripts/svg_filesno.txt", "wt")
        fout2.write(str(nooffiles))
        fout2.close()
    
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

    def framesval(self):
        fout = open(f"{self.MYDIR}/subscripts/frames.txt", "wt")
        fout.write(str(UIinterpreter.samplerselect_2.value()))
        UIinterpreter.label_12.setText(str(UIinterpreter.samplerselect_2.value()))
        fout.close()

    def hex(self):
        color = QtWidgets.QColorDialog.getColor()
        rgb=color.getRgbF()
        fout = open(f"{self.MYDIR}/subscripts/hex.txt", "wt")
        fout.write(str(rgb))
        fout.close()

Funcsrunner=Funcs(f"{pathlib.Path(__file__).parent.absolute()}",f"{pathlib.Path(__file__).parent.absolute()}","PNG",["SVGDIRECTORY"])
UIinterpreter.pushButton_5.clicked.connect(Funcsrunner.renderanim)
UIinterpreter.pushButton_6.clicked.connect(Funcsrunner.renderstill)
UIinterpreter.blendlocselect.clicked.connect(Funcsrunner.blenddirselect)
UIinterpreter.SVGselector.clicked.connect(Funcsrunner.svgopen)
UIinterpreter.Cyclesselector.toggled.connect(Funcsrunner.cyclescall)
UIinterpreter.Eeveeselector.toggled.connect(Funcsrunner.eeveecall)
UIinterpreter.samplerselect.valueChanged.connect(Funcsrunner.samplerval)
UIinterpreter.samplerselect_2.valueChanged.connect(Funcsrunner.framesval)
UIinterpreter.renderlocselect.clicked.connect(Funcsrunner.renderdirselect)
UIinterpreter.jpegselect.toggled.connect(Funcsrunner.jpegcall)
UIinterpreter.pngselect.toggled.connect(Funcsrunner.pngcall)
UIinterpreter.pushButton.clicked.connect(Funcsrunner.hex)

def sampler():
    UIinterpreter.samplerselect.setRange(100,3000)
    UIinterpreter.samplerselect.setValue(2000)
    UIinterpreter.samplerselect.setTickInterval(50)

def frames():
    UIinterpreter.samplerselect_2.setRange(24,360)
    UIinterpreter.samplerselect_2.setValue(240)
    UIinterpreter.samplerselect_2.setTickInterval(24)
frames()
sampler()
appInt=GUI.app
sys.exit(appInt.exec_())

