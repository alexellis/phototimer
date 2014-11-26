phototimer
==========

A smart time-lapse driver for Raspberry PI / raspistill

Usage
-----
    python take.py 60 &
    Takes a photo every 60 seconds
    Default base folder is /mnt/usbflash, photos are then put in a folder such as:
Output file format
-----------------
    /2014/11/20/762132131.jpg
    /yyyy/mm/hh/milliseconds

* Default hours to take images is between 7am and 5pm + 1 hour either side
* Designed to be run constantly - with the quality settings this equates to about 1gb of JPG images per day

Unit testing
------------
    chmod 700 ./run_tests.sh
    ./run_tests.sh

