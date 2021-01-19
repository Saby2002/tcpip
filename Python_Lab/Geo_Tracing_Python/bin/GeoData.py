#/usr/bin/env python

# Module 
import aiohttp
import asyncio
import ssl

# Classes 
class GeoPoller(object):
    def __init__(self, ip_list):
        self.__ips = ip_list
        self.__base_url = 'https://ipapi.co'

        self.__ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.__ssl_context.check_hostname = False
        self.__ssl_context.verify_mode = ssl.CERT_NONE

        async def collect(self):
            tasks = []

            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10) as client_session:
                    for ip_entry in self.__ips:
                        tasks.append(asyncio.ensure_future(self,__single_request(client_session, ip_entry)))

                    results await asyncio.gather(*tasks)

                    resturn results

            async def __single_request(self, session, ip):
                url = f'{self.__base_url}/{ip}/json'

                async with session.get(url, ssl=self.__ssl_contect) as response:
                    result = await response.json()

                return result
