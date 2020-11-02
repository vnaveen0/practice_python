class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        ip_list = address.split('.')
        new_ip = '[.]'.join(ip_list)
        return new_ip
