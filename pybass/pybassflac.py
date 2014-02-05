# Copyright(c) Maxim Kolosov 2009-2013 pyirrlicht@gmail.com
# http://pybass.sf.net
# BSD license

__version__ = '0.2'
__versionTime__ = '2013-03-31'
__author__ = 'Maxim Kolosov <pyirrlicht@gmail.com>'
__doc__ = '''
pybassflac.py - is ctypes python module for
BASSFLAC - extension to the BASS audio library,
enabling the playing of FLAC (Free Lossless Audio Codec) encoded files.
'''

import sys, ctypes, platform, pybass

QWORD = pybass.QWORD
HSTREAM = pybass.HSTREAM
DOWNLOADPROC = pybass.DOWNLOADPROC
BASS_FILEPROCS = pybass.BASS_FILEPROCS

if platform.system().lower() == 'windows':
	bassflac_module = ctypes.WinDLL('bass_flac.dll')
	func_type = ctypes.WINFUNCTYPE
else:
	# correct by Wasylews (sabov.97@mail.ru), thank him
	bassflac_module = ctypes.CDLL('./libbassflac.so', mode=ctypes.RTLD_GLOBAL)
	func_type = ctypes.CFUNCTYPE


# BASS_CHANNELINFO type
BASS_CTYPE_STREAM_FLAC = 0x10900
BASS_CTYPE_STREAM_FLAC_OGG = 0x10901


#HSTREAM BASSFLACDEF(BASS_FLAC_StreamCreateFile)(BOOL mem, const void *file, QWORD offset, QWORD length, DWORD flags);
BASS_FLAC_StreamCreateFile = func_type(HSTREAM, ctypes.c_byte, ctypes.c_void_p, QWORD, QWORD, ctypes.c_ulong)(('BASS_FLAC_StreamCreateFile', bassflac_module))
#HSTREAM BASSFLACDEF(BASS_FLAC_StreamCreateURL)(const char *url, DWORD offset, DWORD flags, DOWNLOADPROC *proc, void *user);
BASS_FLAC_StreamCreateURL = func_type(HSTREAM, ctypes.c_char_p, ctypes.c_ulong, ctypes.c_ulong, DOWNLOADPROC, ctypes.c_void_p)(('BASS_FLAC_StreamCreateURL', bassflac_module))
#HSTREAM BASSFLACDEF(BASS_FLAC_StreamCreateFileUser)(DWORD system, DWORD flags, const BASS_FILEPROCS *procs, void *user);
BASS_FLAC_StreamCreateFileUser = func_type(HSTREAM, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(BASS_FILEPROCS), ctypes.c_void_p)(('BASS_FLAC_StreamCreateFileUser', bassflac_module))


if __name__ == "__main__":
	if not pybass.BASS_Init(-1, 44100, 0, 0, 0):
		print ('BASS_Init error', pybass.get_error_description(pybass.BASS_ErrorGetCode()))
	else:
		handle = BASS_FLAC_StreamCreateFile(False, b'test.flac', 0, 0, 0)
		pybass.play_handle(handle, False)
		if not pybass.BASS_Free():
			print ('BASS_Free error', pybass.get_error_description(pybass.BASS_ErrorGetCode()))
