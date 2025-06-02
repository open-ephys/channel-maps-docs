*************************************************
Documentation for Channel Maps
*************************************************

TODO: Add details here about what this repo is, and what it should be used for.

For more detailed usage instructions, see the `Open Ephys Doc Template <https://github.com/open-ephys/doc-template>`_.

Building locally
######################

Building HTML files locally allows you to preview changes before updating the live site. We recommend working with 'virtual environments' in which you can install the (versions of the) python packages that the site needs, without messing up your own installs. Here's how:

With pipenv (recommended)
-------------------------------------------------

Requirements (system)

* make

Requirements (Python 3):

* pipenv (will automatically download all the project requirements from pypi)

Create a virtual environment with pipenv (will use the Pipfile for installing the necessary packages)

.. code:: shell

    python -m pip install --upgrade pipenv wheel
    pipenv install

You can then spawn a subshell with

.. code:: shell

   pipenv shell

and then you can use ``make`` the usual way

.. code:: shell

   make html     # for html
   make latex    # for latex
   make latexpdf # for latex (will require latexpdf installed)
   make          # list all the available output format

all the outputs will be in docs folder (for html: docs/html)

Exit the virtualenv with

.. code:: exit

   exit


Acknowledgements
####################################

This documentation's source template was taken from the `Spinal HDL <https://github.com/SpinalHDL/SpinalDoc-RTD>`_ project.

The theme is based on the `PyData Sphinx Theme <https://pydata-sphinx-theme.readthedocs.io/en/latest/>`_
