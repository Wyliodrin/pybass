# Copyright(c) Max Kolosov 2009 maxkolosov@inbox.ru
# http://vosolok2008.narod.ru
# BSD license

__version__ = '0.2'
__versionTime__ = '2013-01-22'
__author__ = 'Max Kolosov <maxkolosov@inbox.ru>'
__doc__ = '''
pybass_ape.py - is ctypes python module for
BASS_APE - extension to the BASS audio library
that enables the playback of Monkey's Audio streams.
'''

import sys, ctypes, platform, pybass

QWORD = pybass.QWORD
HSTREAM = pybass.HSTREAM
BASS_FILEPROCS = pybass.BASS_FILEPROCS

if platform.system().lower() == 'windows':
	bass_ape_module = ctypes.WinDLL('bass_ape')
	func_type = ctypes.WINFUNCTYPE
else:
	bass_ape_module = ctypes.CDLL('bass_ape')
	func_type = ctypes.CFUNCTYPE


# Additional tags available from BASS_StreamGetTags
BASS_TAG_APE = 6# APE tags

# BASS_CHANNELINFO type
BASS_CTYPE_STREAM_APE = 0x10700


#HSTREAM BASSAPEDEF(BASS_APE_StreamCreateFile)(BOOL mem, const void *file, QWORD offset, QWORD length, DWORD flags);
BASS_APE_StreamCreateFile = func_type(HSTREAM, ctypes.c_byte, ctypes.c_void_p, QWORD, QWORD, ctypes.c_ulong)(('BASS_APE_StreamCreateFile', bass_ape_module))
#HSTREAM BASSAPEDEF(BASS_APE_StreamCreateFileUser)(DWORD system, DWORD flags, const BASS_FILEPROCS *procs, void *user);
BASS_APE_StreamCreateFileUser = func_type(HSTREAM, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(BASS_FILEPROCS), ctypes.c_void_p)(('BASS_APE_StreamCreateFileUser', bass_ape_module))


if __name__ == "__main__":
	if not pybass.BASS_Init(-1, 44100, 0, 0, 0):
		print('BASS_Init error %s' % pybass.get_error_description(pybass.BASS_ErrorGetCode()))
	else:
		handle = BASS_APE_StreamCreateFile(False, b'test.ape', 0, 0, 0)
		pybass.play_handle(handle)
		if not pybass.BASS_Free():
			print('BASS_Free error %s' % pybass.get_error_description(pybass.BASS_ErrorGetCode()))
