#!/bin/bash

if [ "$wyliodrin_board" == "raspberrypi" ] || [ "$wyliodrin_board" == "beagleboneblack" ]; then
	cp lib/hardfp/*.so /usr/local/lib
fi

if [ "$wyliodrin_board" == "arduinogalileo" ] || [ "$wyliodrin_board" == "edison" ]; then
	mkdir /usr/local
	mkdir /usr/local/lib
	cp lib/x86/*.so /usr/lib
	cp lib/x86/*.so /usr/local/lib
fi

ldconfig

python setup.py install

