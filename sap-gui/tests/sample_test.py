import subprocess
import sys
import time
import win32com.client

def sap_login():
    try:
        path = "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"

        subprocess.Popen(path)
        time.sleep(10)

        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine

        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return

        connection = application.Children(0)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)

        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

    except:
        print("THis is except section")


    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None

if __name__ == '__main__':
    sap_login()