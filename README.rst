spackdemo README
================

A pyramid webapp demo of the <keygen> using pyspack.
It also use nginx for the SSL validation.


Getting Started
---------------

- create a python virtual env and activate it

- git clone git@github.com:mardiros/spackdemo.git 

- $VIRTUAL_ENV/bin/python setup.py develop

- $VIRTUAL_ENV/bin/pserve development.ini &

- sudo ./start_nginx.sh &

- firefox https://localhost/


.. note::

    Demo used self signed certificates available in the certs directory.
    It does not work on chromium (make certificate errors).



See Also
--------

http://lists.whatwg.org/pipermail/whatwg-whatwg.org/attachments/20080714/07ea5534/attachment.txt
