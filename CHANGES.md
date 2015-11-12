The 420chan API was designed to be as close as possible to the 4chan API, circa 2013 anyway. Documentation can be found here: http://api.420chan.org/

## Differences From 4chan API

* **Pages Start at 0** - Historically, pages on the 4chan API started at 0, but now they start at 1. 420chan retains this historical convention.
* **`tim` renamed to `filename`** - While 420chan also names it's images based on UNIX timestamps + milliseconds, it no longer  Also, the original filename is not preserved on 420chan.

### Not Implemented Yet

The 420chan is missing some handy features compared to the 4chan API, such as the following:

* omitted_posts - The lack of this feature forces us to ditch `expand()` and use `update()` instead.
* omitted_images - Because the `omitted` attributes are missing, the `repr` no longer reports them.
* filedeleted - The image will just 404 if it was deleted.
* spoiler
* images - No total of all images in the thread.
* bumplimit

In addition, the 420chan API is missing some useful HTTP headers that the 4chan API has:

* **Last-Modified** - This is a major missing feature. The lack of a Last-Modified header forces us to update the entire thread JSON each time, rather than checking the header and knowing that it hasn't been modified yet.