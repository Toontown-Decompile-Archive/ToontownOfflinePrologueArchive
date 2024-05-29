# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.launcher.procapi
# Compiled at: 2014-04-30 09:53:54
import ctypes
from ctypes.wintypes import *
TH32CS_SNAPPROCESS = 2
INVALID_HANDLE_VALUE = -1
cwk = ctypes.windll.kernel32

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
     (
      'dwSize', DWORD),
     (
      'cntUsage', DWORD),
     (
      'th32ProcessID', DWORD),
     (
      'th32DefaultHeapId', HANDLE),
     (
      'th32ModuleID', DWORD),
     (
      'cntThreads', DWORD),
     (
      'th32ParentProcessID', DWORD),
     (
      'pcPriClassBase', LONG),
     (
      'dwFlags', DWORD),
     (
      'szExeFile', c_char * MAX_PATH)]


class ProcessEntryPY:

    def __init__(self, name, pid):
        self.name = name
        self.pid = pid


def getProcessList():
    hProcessSnap = cwk.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)
    processList = []
    if hProcessSnap != INVALID_HANDLE_VALUE:
        pe32 = PROCESSENTRY32()
        pe32.dwSize = sizeof(pe32)
        if cwk.Process32First(hProcessSnap, ctypes.byref(pe32)):
            while 1:
                processList.append(ProcessEntryPY(pe32.szExeFile.lower(), int(pe32.th32ProcessID)))
                if not cwk.Process32Next(hProcessSnap, ctypes.byref(pe32)):
                    break

        cwk.CloseHandle(hProcessSnap)
    return processList