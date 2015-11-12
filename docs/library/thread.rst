:class:`py420chan.Thread` – 420chan Threads
============================================

:class:`py420chan.Thread` allows for standard access to a 420chan thread, including listing all the posts in the thread, information such as whether the thread is locked and stickied, and lists of attached file URLs or thumbnails.

Basic Usage
-----------

.. autoclass:: py420chan.Thread

Methods
-------

    Thread objects are not instantiated directly, but instead through the appropriate :class:`py420chan.Board` methods such as :meth:`py420chan.Board.get_thread`.

    .. automethod:: py420chan.Thread.files

    .. automethod:: py420chan.Thread.thumbs

    .. automethod:: py420chan.Thread.filenames

    .. automethod:: py420chan.Thread.thumbnames

    .. automethod:: py420chan.Thread.update

    .. automethod:: py420chan.Thread.expand
