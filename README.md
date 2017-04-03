phototimer - smart time-lapses
==========

phototimer gives you a smart way to capture photos for your timelapses. It is smart because it only takes pictures between the hours you specify and creates a useful folder structure. It is simple because it only depends on Python and `raspistill` both of which are normally already available.

This software was originally featured on my blog in Oct 2015:

* [Portable wildlife timelapse](http://blog.alexellis.io/centreparcs-timelapse/)

An example timelapse was uploaded to YouTube showing some mint cuttings growing in May 2016:

* [Video: Mint cuttings on - PI Zero Timelapse ](https://www.youtube.com/watch?v=Kkg6dyr4t0c)

How does it work?
------------------

Start phototimer through a terminal, `ssh` connection or `@reboot crontab` specifying the amount of seconds between photos after that. By default photos are stored in `/mnt/usbflash`, but this is configurable along with daylight hours and the quality level of the photos. Enable the http server to view the images from a browser.

This is an example `config.py` file which should create files that are about 2MB in size:

```python
config = {}
config["am"] = 400
config["pm"] = 2000

config["flip_horizontal"] = False
config["flip_vertical"] = False
config["metering_mode"] = "matrix"

config["base_path"] = "/var/image"
config["height"] = 1536
config["width"] = 2048
config["quality"] = 35

# Set True to enable http server
config["http_server"] = False
config["http_port"] = 8000
```


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

Docker
------

Stay tuned for a Dockerfile that packages this code into a single unit. For now checkout `alexellis2/raspistill` for a Docker image with the `raspistill` tool installed. 

> You will need to run the container in privileged mode to gain access to the camera.

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

Please get in touch with me on Twitter [@alexellisuk](https://twitter.com/alexellisuk) if you have any requests, comments or suggestions. If you run into problems then you could also raise a Github issue.
