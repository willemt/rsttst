rsttst makes your reStructuredText documentation testable.

In fact, this README file is testable and is used to test rsttst.

Below is an example:

2 + 2 = 4
---------

The title "2 + 2 = 4" becomes the test name after being converted to a
Python friendly identifier (ie. 2_plus_2_equals_4).

The bash code in the below code block will be run...

.. code-block:: bash

   echo "2 + 2" | bc

...and the resulting stdout will be compared to the following code block:

.. code-block:: bash

   4

The test fails if stdout doesn't match the block above.

Generating tests
----------------

Under the hood rsttst generates Python code which is executable with py.test.

Here's how we generate the Python test code:

.. code-block:: bash

   ./rsttst README.rst
   cat test_readme.py | head -n 26 # use head, otherwise it's turtles all the way down

The resulting test code looks like the following:

.. code-block:: python

  import pytest
  import os
  import subprocess
  import sys
  import shlex
  
  def run(cmd):
      os.system(cmd)
  
  
  def test_2_plus_2_equals_4(capfd):
      run("""echo "2 + 2" | bc""")
      assert capfd.readouterr()[0] == """4
  """
  
  def test_generating_tests(capfd):
      run("""./rsttst README.rst""")
      run("""cat test_readme.py | head -n 26 # use head, otherwise it\'s turtles all the way down""")
      assert capfd.readouterr()[0] == """import pytest
  import os
  import subprocess
  import sys
  import shlex
  
  def run(cmd):
      os.system(cmd)

Running the tests
-----------------

.. code-block:: bash

   py.test -k 'not test_running_the_tests' | grep -v seconds

Note: we had to exclude 'test_running_the_tests', otherwise it's turtles all the way down.

.. code-block:: bash

           ============================= test session starts ==============================
           platform darwin -- Python 2.7.7 -- py-1.4.20 -- pytest-2.5.2
           collected 3 items
           
           test_readme.py ..
           
           ============= 1 tests deselected by '-knot test_running_the_tests' =============

Functionality
-------------

Right now rsttst only supports bash testing.
