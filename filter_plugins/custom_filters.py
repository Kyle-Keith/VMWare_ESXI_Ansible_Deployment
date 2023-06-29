def check_ip_suffix(ip, suffix):
    return ip.split('.')[-1] == str(suffix)

class FilterModule(object):
    def filters(self):
        return {
            'check_ip_suffix': check_ip_suffix
        }
