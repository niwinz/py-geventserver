.. py-geventserver documentation master file, created by
   sphinx-quickstart on Sun Jun 12 11:18:46 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to py-geventserver's documentation!
===========================================

Script for launch any wsgi or django application over gevent wsgi server. 

Obtain source.
^^^^^^^^^^^^^^

Currently the source code is at github and may obtain a copy to::
    
    git clone git://github.com/niwibe/py-geventserver.git
    cd py-geventserver

Install py-geventserver in your system with::
    
    sudo python setup.py install


Possible parameters:
^^^^^^^^^^^^^^^^^^^^

.. option:: -P <file>, --pidfile=<file>
   
   Set pidfile location. If not specified, file is not written.

.. option:: -p <port>, --port=<port>
   
   Set port number for listen. Default is 9000.

.. option:: -i <host>, --host=<host>
   
   Set hostname or interface ip address for listen. Default: any (0.0.0.0)

.. option:: -r <path>, --root=<path>
   
   Use this parameter if you like, that before doing anything, is positioned to a directory.

.. option:: -s <settings>, --settings=<settings>
   
   Optional parameter. Only if you use geventserver with django. Specify python-like path
   of you settings location.

.. option:: -d, --daemon
   
   Use this parameter if you want the process to run in the background.

.. option:: -t <type>, --type=<type>
   
   Select the application type to run. Posible options: wsgi, django.
   The default is django.



Example usage with django application.
""""""""""""""""""""""""""""""""""""""

This is a posible invironment::
    
    [niwi@vaio.niwi.be][~/devel/niwi-web/src]% l
    total 272K
    -rw-r--r--  1 niwi    0 Feb 26 04:32 __init__.py
    -rw-r--r--  1 niwi  594 May 28 18:08 manage.py
    drwxr-xr-x  3 niwi    8 Jun  5 15:09 media/
    drwxr-xr-x 10 niwi  20K Jun 12 01:34 niwi/
    -rw-r--r--  1 niwi 1.7K Jun  5 14:48 settings.py
    -rw-r--r--  1 niwi  869 Jun 11 16:20 urls.py

This is a example to run this project with geventserver::
    
    [niwi@vaio.niwi.be][~/devel/niwi-web/src]% geventserver.py -s settings -p 9000
    Serving on 0.0.0.0:9000


How run other wsgi app with geventserver.
"""""""""""""""""""""""""""""""""""""""""

This is an example of the simplest 'Hello world' wsgi app::
    
    def application(environ, start_response):
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']
        status = '200 OK'

        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]

        start_response(status, response_headers)
        return [response_body]

Run this app is very simple::
    
    [niwi@vaio.niwi.be][/tmp]% geventserver.py -t wsgi -p 9000 /tmp/testwsgiapp.py 
    Serving /tmp/testwsgiapp.py on 0.0.0.0:9000


Other posible combination is run mercurial server over gevent with supervisord.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This is an example of hgweb.py file::
    
    import os.path
    config = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.ini')

    from mercurial import demandimport; demandimport.enable()
    from mercurial.hgweb import hgweb
    
    application = hgweb(config)

If you want to lift the mercurial service without supervisord. It's just as easy as the previous example.

This is an example of supervisord config::
    
    [program:niwihg]
    command=/usr/bin/geventserver.py --port 10000 --type='wsgi' /srv/www/hg/niwihg.py
    user=http
    directory=/srv/www/hg
    autostart=true
    autorestart=true

