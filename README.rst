mama-ng-controlinterface
=======================================

The MAMA Nigeria programme aims to deliver stage based messages to mothers and gatekeepers in Nigeria in order to increase demand for quality maternal and child health care services in the country.


Django Setup
---------------------------------------

Remember to enable hbase on your postgres template

::

    psql -d template1 -c 'create extension hstore;'


Pattern Lab Setup
---------------------------------------

The control interface comes with a atomic design system to aid code reuse
and limit the need for complex wireframe and design processes.

Visit: http://patternlab.io/ to learn more.

Remember to install scss:

::

    gem install sass

To build and serve the lab locally:

::

    cd src
    npm install
    gulp serve
