function FindProxyForURL(url, host) {


    if (dnsDomainIs(host, ".telstra.com.au"))
	return "PROXY 192.168.99.138:8080";
 /*
// If the hostname matches, send direct.
    if (dnsDomainIs(host, ".telstra.com.au"))
        return "PROXY 192.168.99.138:8080";

   if (dnsDomainIs(host, ".merill.net"))
        return "PROXY 192.168.99.138:8080";
 */
// DEFAULT RULE: All other traffic, use below proxies, in fail-over order.
    return "DIRECT";
}