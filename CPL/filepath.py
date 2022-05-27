import datetime
import os.path


def filepath(request, filename):
    old_filename = filename
    time_now = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (time_now, old_filename)
    return os.path.join('uploads/', filename)
