from ninfo import PluginBase

class cif_plug(PluginBase):
    """This plugin returns any information from cif"""
    name    =    'cif'
    title   =    'CIF'
    description   =  'Collective Intelligence Framework'
    cache_timeout   =  60*60
    types   =    ['ip','ip6','hostname','username']
    local = False

    def setup(self):
        from cif_http_client import Client
        http_options = {}
        config = self.plugin_config.copy()
        if config.pop("verify_ssl", None) == "false":
            http_options = {"verify": False}
        self.cif = Client(http_options=http_options, **config) #should contain url, api_key, and optional arguments

    def get_info(self, arg):
        results = self.cif.search(q=arg)

        flat = {}
        for r in results:
            tup = (r["address"], r["description"], r["alternativeid"], r.get("portlist"))
            if tup not in flat:
                r["time_first"] = r["time_last"] = r["detecttime"]
                flat[tup] = r
            else:
                fr = flat[tup]
                flat[tup]["time_first"] = min(fr["time_first"], r["detecttime"])
                flat[tup]["time_last"] = max(fr["time_last"], r["detecttime"])

        return {
            "results": results,
            "flat": flat.values(),
        }

plugin_class = cif_plug
