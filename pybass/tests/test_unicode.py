# -*- coding: cp1251 -*-

'this test with BASS_UNICODE flag, thanks "winand" user from http://un4seen.com/forum'

from pybass import *

def main():
	file_name = u'test_�������.ogg'
	if sys.hexversion >= 0x03000000:
		file_name = 'test_�������.ogg'
	BASS_Init(-1, 44100, 0, 0, 0)
	handle = BASS_StreamCreateFile(False, file_name, 0, 0, BASS_UNICODE)
	play_handle(handle, show_tags = False)
	BASS_Free()

if __name__ == "__main__":
	main()
