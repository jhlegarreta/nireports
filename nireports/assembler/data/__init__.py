"""Nireports assembler data files

.. autofunction:: load

.. automethod:: load.readable

.. automethod:: load.as_path

.. automethod:: load.cached
"""

from acres import Loader

load = Loader(__spec__.name)
