phototimer - smart time-lapses
==========

phototimer gives you a smart way to capture photos for your timelapses. It is smart because it only takes pictures between the hours you specify, creates a useful folder structure and simple because it only needs Python.

How does it work?
------------------

Start phototimer through a terminal, ssh connection or `@reboot crontab` specifying the amount of seconds between photos after that. By default photos are stored in /mnt/usbflash, but this is configurable along with daylight hours and the quality level of the photos.


Usage
-----
```
$ python take.py 60 &
```

This will takes a photo every 60 seconds. The default base folder is /mnt/usbflash, photos are then put in a folder such as:
Output file format
-----------------
    /2014/11/20/762132131.jpg
    /yyyy/mm/hh/milliseconds

* Default hours to take images is between 7am and 5pm + 1 hour either side
* Designed to be run constantly - with the quality settings this equates to about 1gb of JPG images per day

Troubleshooting
---------------
If you find that phototimer is automatically exiting then you may want to use a tool like `screen` to make sure you can keep an eye on the process.

```
$ screen
$ cd phototimer
$ python2 take.py 60
[Control A + D]
```

To reconnect later type in `screen -r`.

Unit testing
------------

The exposure calculations and some other functions have been unit tested, if you change the code or want to extend it please look at these before contributing.

Here's how you run them:

```
chmod 700 ./run_tests.sh
./run_tests.sh
```

Feedback?
---------

Please get in touch with me on Twitter @alexellisuk if you have any requests, comments or suggestions. If you run into problems then you could also raise a Github issue.
