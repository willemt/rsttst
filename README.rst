.. image:: https://img.shields.io/badge/rsttst-testable-brightgreen.svg
   :target: https://github.com/willemt/rsttst

.. image:: https://travis-ci.org/willemt/rsttst.png
   :target: https://travis-ci.org/willemt/rsttst

.. image:: https://pypip.in/version/rsttst/badge.svg
   :target: https://pypi.python.org/pypi/rsttst
 
.. image:: https://pypip.in/download/rsttst/badge.svg
   :target: https://pypi.python.org/pypi/rsttst

rsttst makes your reStructuredText documentation testable.

In fact, this README file is testable and is used to test rsttst.

If your tests document how your system works, why not formally combine your tests and documentation into one?

Below is an example:

2 + 2 = 4
=========

The title "2 + 2 = 4" becomes the test name after being converted to a
Python friendly identifier (ie. 2_plus_2_equals_4).

The bash code in the below code block will be run...

.. code-block:: bash

   echo '2 + 2' | bc

...and the resulting stdout will be compared to the following code block:

.. code-block:: bash

   4

The test fails if stdout doesn't match the block above.

Dotted notation
===============

Sometimes you want to be flexible with the output you accept.

You can use "." and the ":class: dotted" rst directive option to support this.

.. code-block:: bash

   echo Date: $(date)
   echo '\ok'

The below code block uses the ":class: dotted" option.

.. code-block:: bash
   :class: dotted

   Date: ............................
   \ok

Three dots match in a similiar way to what you'd expect for a regex pattern of ".+" to work:

.. code-block:: bash

   echo '<NZ>'
   echo $(date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S")

The below code block uses the ":class: dotted" option.

.. code-block:: bash
   :class: dotted

   <...>
   DATE: ... TIME: ...

Generating tests
================

Under the hood rsttst generates Python code which is executable with py.test.
Here's how we generate the Python test code:

.. code-block:: bash

   rsttst README.rst
   cat test_readme.py | head -n 28

The resulting test code looks like the following:

.. code-block:: bash

   # -*- coding: utf-8 -*-
   from rsttst.core import run, Dotted
   
   def test_2_plus_2_equals_4():
       output = run(u"""echo '2 + 2' | bc""")
       assert output == u"""4"""
   
   def test_dotted_notation():
       output = run(u"""echo Date: $(date)
   echo '\\ok'""")
       expected = Dotted(u"""Date: ............................
   \\ok""")
       cmp(output, expected)
       expected = u"{0}".format(expected)
       assert output == expected
   
   def test_dotted_notation__2():
       output = run(u"""echo '<NZ>'
   echo $(date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S")""")
       expected = Dotted(u"""<...>
   DATE: ... TIME: ...""")
       cmp(output, expected)
       expected = u"{0}".format(expected)
       assert output == expected
   
   def test_generating_tests():
       output = run(u"""rsttst README.rst
   cat test_readme.py | head -n 28""")

Windows new lines
=================

^M characters are automatically removed.

.. code-block:: bash

   printf 'supports\012\015windows new lines'

.. code-block:: bash

   supports
   windows new lines

Ignore code-blocks
==================

Sometimes you want to use a code-block without it being tested by rsttst.

You can use the ":class: ignore" directive to ignore this code-block:

.. code-block:: bash
   :class: ignore

   .. code-block:: bash
      :class: ignore

Running the tests
=================

You could probably use another test runner, but pytest works quite well:

.. code-block:: bash

   py.test -k 'not test_running_the_tests' | grep -v seconds

Note: we had to exclude 'test_running_the_tests', otherwise it's turtles all the way down.

.. code-block:: bash
   :class: dotted

   ============================= test session starts ==============================
   platform ...
   collected 6 items
           
   test_readme.py .....
           
   ============= 1 tests deselected by '-knot test_running_the_tests' =============


Functionality
=============

Right now rsttst only supports bash testing.

FAQ
===

*Why does pytest throw an "IndexError: list index out of range" exception for my JSON tests?*

Please upgrade to the latest version of pytest
