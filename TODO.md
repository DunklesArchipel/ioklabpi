On the RaspberryPi:

* A simple argparse interface `./raw.py --frequency=123 --channel 1=name --channel 2=foo` that writes CSV to STDOUT until KeyboardInterrupt or SIGHUP
* A wrapper [sh](https://amoffat.github.io/sh/) script for the common use-case: `./measure.py --prefix=PREFIX --output=DIR -- RAW_ARGS` writes to `DIR/PREFIX-{raw_input()}-0-TIMESTAMP.csv`, shuts down (with a signal) and respawns its child on keypress. And only shuts down everything on a KeyboardInterrupt.

* A [lsyncd](https://github.com/axkibe/lsyncd) that syncs everything to the server over ssh
* A pipe that pushes everything into a RabbitMQ channel for live display in a Jupyter notebook.
