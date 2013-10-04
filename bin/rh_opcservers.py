from splunk import admin
import sc_rest

class OpcServerConfRes(object):
    endpoint      = '/admin/conf-opcservers'
    optional_args = []
    required_args = ['dcomhost', 'domain', 'user', 'password', 'progid', 'clsid']
    transient_args = []

if __name__ == "__main__":
    admin.init(sc_rest.ResourceHandler(OpcServerConfRes), admin.CONTEXT_NONE)
