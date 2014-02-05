pybass
======

Python BASS Library with ctypes python module for BASS (http://www.un4seen.com).

BASS is an audio library for use in Windows, Linux and MacOSX software. Its
purpose is to provide the most powerful and efficient (yet easy to use),
sample, stream, MOD music, and recording functions. All in a tiny DLL,
under 100KB in size.

See the documentation for descriptions of all the BASS functions. You
should also look at the included example program source-codes for some
examples of how to use BASS in your own programs.


Requirements
============
Win32 version
-------------
BASS requires DirectX 3 or above for output. BASS does not require that a
soundcard with DirectSound/DirectSound3D hardware accelerated drivers is
installed, but it does improve performance if there is one. BASS also takes
advantage of MMX, which improves the performance of the MOD music playback.

MacOSX version
--------------
OSX 10.3 or above is recommended. BASS uses CoreAudio for output, so there
are no special library/driver requirements. BASS supports both PowerPC and
Intel Macs.


Main Features
=============
* Samples
  supports WAV/AIFF/MP3/MP2/MP1/OGG and custom generated samples

* Sample streams
  stream any sample data in 8/16/32 bit, with both "push" and "pull" systems

* File streams
  MP3/MP2/MP1/OGG/WAV/AIFF file streaming

* Internet file streaming
  stream files from the internet, including Shout/Icecast

* User file streaming
  stream files from anywhere using any delivery method

* Multi-channel streaming
  support for more than plain stereo, including multi-channel OGG/WAV/AIFF files

* MOD music
  uses the same engine as XMPlay = best accuracy, speed, and quality

* MO3 music
  MP3/OGG compressed MOD music

* Add-on system
  support for more formats is available via add-ons (aka plugins)

* Multiple outputs
  simultaneously use multiple soundcards, and move channels between them

* Recording
  flexible recording system, with support for multiple devices

* Decode without playback
  streams and MOD musics can be outputted in any way you want

* Speaker assignment
  assign streams and MOD musics to specific speakers

* High precision synchronization
  synchronize events in your software to the streams and MOD musics

* DirectX 8 effects
  chorus/compressor/distortion/echo/flanger/gargle/parameq/reverb

* User defined DSP functions
  custom effects may be applied to musics and streams

* 32 bit floating-point decoding and processing
  floating-point stream/music decoding, DSP, FX, and recording

* 3D sound
  play samples/streams/musics in any 3D position, with EAX support

* Small
  BASS is under 100KB (on Windows), so won't bloat your distribution


Using BASS
==========
There is no guarantee that all future BASS versions will be compatible
with all previous versions, so your program should use BASS_GetVersion
to check the version that is loaded. This also means that you should
put the BASS module in the same directory as your executable (not just
somewhere in the path), to avoid the possibility of a wrong version being
loaded.

If you are updating your software from a previous BASS version, then
you should check the "History" section (below), to see if any of the
functions that you are using have been affected by a change.
