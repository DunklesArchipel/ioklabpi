On the RaspberryPi:

* The high precision board uses an ADS1256 which can be read with [PiPyADC](https://github.com/ul-gh/PiPyADC) or with [py-ads1256](https://github.com/fabiovix/py-ads1256) or [PyADS1256](https://github.com/heathsd/PyADS1256). The first one seems nicest but has no Python3 support yet.
* The low precision board is an [ADS1015](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115) which is probably easier to work with.
* A simple argparse interface `./raw.py --frequency=123 --channel 1=name --channel 2=foo` that writes CSV to STDOUT until KeyboardInterrupt or SIGHUP
* A wrapper [sh](https://amoffat.github.io/sh/) script for the common use-case: `./measure.py --prefix=PREFIX --output=DIR -- RAW_ARGS` writes to `DIR/PREFIX-{raw_input()}-0-TIMESTAMP.csv`, shuts down (with a signal) and respawns its child on keypress. And only shuts down everything on a KeyboardInterrupt.

* A [lsyncd](https://github.com/axkibe/lsyncd) that syncs everything to the server over ssh
* A filebeat that beats everything at the server's logstash

On the Server:

* logstash with [CSV](https://www.elastic.co/guide/en/logstash/6.0/plugins-filters-csv.html) to graphite
* grafana reading from graphite
