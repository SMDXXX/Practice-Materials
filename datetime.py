from time import gmtime, strftime
strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

from datetime import timedelta
d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)
