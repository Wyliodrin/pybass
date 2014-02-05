# -*- coding: utf-8 -*-

# Copyright(c) Wasylews 2013 (sabov.97@mail.ru)

from pybass import *

def main():
    BASS_Init(-1, 44100, 0, 0, 0)
    plugin = BASS_PluginLoad(b"./libbassflac.so", 0)
    print("plugin = %d" % plugin)
    handle = BASS_StreamCreateFile(False, b"test.flac", 0, 0, 0)
    play_handle(handle, show_tags=False)
    BASS_Free()

if __name__ == "__main__":
    main()
