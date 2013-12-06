from graphite.util import PluginRegistrar

class GraphiteDatabase(object):
  "Abstract base class for Carbon database backends"
  __metaclass__ = PluginRegistrar
  plugins = {}

  def finder(self):
    raise NotImplemented()
