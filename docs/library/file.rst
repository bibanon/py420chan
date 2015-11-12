:class:`py420chan.File` – 420chan File
=======================================

:class:`py420chan.Post` allows for standard access to a 420chan file. This provides programs with a complete File object that contains all metadata about the 420chan file, and makes migration easy if 420chan ever makes multiple files in one Post possible (as 8chan does).

Basic Usage
-----------

.. autoclass:: py420chan.File

    File objects are not instantiated directly, but through a :class:`py420chan.File` object with an attribute like :attr:`py420chan.Post.first_file`.