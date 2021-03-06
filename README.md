# pathconfig

pathconfig is a small library that aims to make it easy to make your
application configurable and find its data easily.

it features the following central functions/classes:

 * *pathconfig.load_configuration* creates an AppContext object that allows
   to retrieve configuration variables (`get_config_var`)
 * *pathconfig.Factory* is a class for objects that have parts that can be
   loaded on-demand. If `obj` is your object, and it has a `load_banana`
   method, then `obj.get('banana')` will either returned the cached banana
   or invoke its `load_banana`  method to retrieve one.
 * *pathconfig.load_plugin* provides a friendly wrapper around setuptools'
   `entry_points` mechanism.

# Install
The most convenient way is to install pathconfig via pip or easy_install:

`pip install pathconfig`

# Getting started
see examples/simple_example.py

