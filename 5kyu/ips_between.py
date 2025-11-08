# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start, end):
  def ip_to_int(ip):
    octets = [int(x) for x in ip.split('.')]
    return octets[0] * 256**3 + octets[1] * 256**2 + octets[2] * 256 + octets[3]
  
  return ip_to_int(end) - ip_to_int(start)