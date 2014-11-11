
class GraphiteDatabase(object):
  "Abstract base class for Carbon database backends"

  def finder(self):
    raise NotImplemented()
