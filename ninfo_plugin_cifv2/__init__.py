from ninfo import PluginBase

COLS = ['tlp', 'group', 'lasttime', 'reporttime', 'observable', 'otype', 'cc', 'asn', 'asn_desc', 'confidence', 'description', 'tags', 'rdata', 'rtype', 'provider', 'altid']

class cif_plug(PluginBase):
    """This plugin returns any information from cif"""
    name    =    'cif'
    title   =    'CIF'
    description   =  'Collective Intelligence Framework'
    cache_timeout   =  60*60
    types   =    ['ip','ip6','cidr', 'cidr6', 'hostname','username']
    local = False

    def setup(self):
        from cifsdk.client import Client
        from cifsdk.format import Table
        self.Table = Table
        config = self.plugin_config.copy()
        self.table_cols = None
        if 'table_cols' in config:
            self.table_cols = config.pop('table_cols').split(",")
        self.cif = Client(**config) #should contain token, remote, verify_ssl

    def make_table(self, data):
        if not self.table_cols:
            return self.Table(data)
        else:
            return self.Table(data, self.table_cols)

    def get_info(self, arg):
        results = self.cif.search(arg, nolog=True)

        return {
            "results": results,
            "table": self.make_table(results),
        }

plugin_class = cif_plug
