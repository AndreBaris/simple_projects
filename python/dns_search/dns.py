#!/usr/bin/env python3

import dns.reversename
n = dns.reversename.from_address("127.0.0.1")
print(n)
print(dns.reversename.to_address(n))