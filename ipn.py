import mechanize
from bs4 import BeautifulSoup as btu
from colorama import Fore, Style
import folium
import re

__author__="Naci Caner"
__version__ = "0.1.0"


class colors:
    Red = Fore.RED + Style.BRIGHT #kirmizi
    Gren = Fore.GREEN + Style.BRIGHT #yesil
    blue= Fore.BLUE + Style.BRIGHT # mavi
    yellow= Fore.YELLOW + Style.BRIGHT 
    magenta = Fore.MAGENTA + Style.BRIGHT # mor
    cyan = Fore.CYAN + Style.BRIGHT # acik mavi
    white = Fore.WHITE + Style.BRIGHT # beyaz




class İnfoİP():
    def __init__(self) :
        """
        İp_info(ip_info:str) - > 192.168.1.1 == str
        
        Since the type of IP entered is str, we process it as a string.
        
        
        Entered IP Address Company will give a map link showing latitude and longitude.
        
        """
        self.Url = "https://whatismyipaddress.com/ip/"
        self.headers={'User-Agent': 'Mozilla/5.0', 'X-Requested-With': 'XMLHttpRequest', 'Accept': 'application/json, text/javascript, */*; q=0.01'}
        self.ip_info = str(input(colors.Gren +"~#: ")).strip()
        self.enlem = 0
        self.boylam = 0
        self.general_information = None
        self.İpfo(self.ip_info)
        self.MapCreate()

    def req(self, url:str) -> str:
        """
        With the normal "requests" module, the site blocks requests,
        but with the "mechanize" module, this problem disappears.

        :parameter self.Url
        :return: Returns the html codes of the site. "out" variable
        """
        browser = mechanize.Browser()
        headers = [
            ('Accept', 'text/javascript, text/html, application/xml, text/xml, */*'),
            ('Content-type', 'application/x-www-form-urlencoded; charset=UTF-8'),
            ('User-Agent', 'Foobar'),
        ]
        browser.addheaders = headers
        browser.set_handle_robots(False)
        browser.open(url)
        out = browser.response().read()
        return out


    def İpfo(self,ip_info:str) -> str:

        """

        Decimal: 1911040789 Hostname: 113.232.43.21
        ASN: 4837 ISP: China Unicom Liaoning Province Network Services: None detected
        Assignment: Likely Static IP Country: China State/Region: Liaoning City: Shenyang

        :parameter ip => 192.168.1.3
        :param ip_info
        :type Str
        :type İnt
        :return: Returns information about latitude, longitude and ip
        """
        NewsR = self.req(self.Url+ip_info)
        NewsS = btu(NewsR,"lxml")
        try:
            self.general_information = NewsS.find("div",attrs={"class":"left"}).text
            maplist = []
            NewsM = NewsS.find_all("div",{"class":"right"})
            for i in NewsM:
                map_data = i.find_all("p")
            for map in map_data:
                sonuc = maplist.append(map.text)


            self.enlem = maplist[0].split(" ")[1].split()[0]
            self.boylam = maplist[1].split(" ")[1].split()[0]
        except:
            return "NOT found ip"



    def MapCreate(self):  ##### TAMAMDIR BU
        """
        The entered ip finds the exact location of the ip and shows it to us on the map, and writes the map to the index.html file.

        :return: index.html map
        :parameter latitude , longitude
        prints the spinning thread information nicely on the screen

        I called them to inherit from two classes

        NFO_MAL: Indicates whether there is a leak about the entered mail.

        :type Class
        :parameter None
        """
        Map_new = folium.Map(location=[self.enlem, self.boylam])
        Map_new.save("index.html")

        text = self.general_information
        decimal_pattern = r"Decimal: (\d+)"
        decimal_match = re.search(decimal_pattern, text)
        decimal = decimal_match.group(1)

        # Hostname
        hostname_pattern = r"Hostname: (\d+\.\d+\.\d+\.\d+)"
        hostname_match = re.search(hostname_pattern, text)
        hostname = hostname_match.group(1)

        # ASN
        asn_pattern = r"ASN: (\d+)"
        asn_match = re.search(asn_pattern, text)
        asn = asn_match.group(1)

        # ISP
        isp_pattern = r"ISP: (.+?)Network Services:"
        isp_match = re.search(isp_pattern, text)
        isp = isp_match.group(1)

        # Assignment
        assignment_pattern = r"Assignment: (.+?)Country:"
        assignment_match = re.search(assignment_pattern, text)
        assignment = assignment_match.group(1)

        # Country
        country_pattern = r"Country: (.+?)State/Region:"
        country_match = re.search(country_pattern, text)
        country = country_match.group(1)

        # State/Region
        state_region_pattern = r"State/Region: (.+?)City:"
        state_region_match = re.search(state_region_pattern, text)
        state_region = state_region_match.group(1)

        # City
        city_pattern = r"City: (.+)"
        city_match = re.search(city_pattern, text)
        city = city_match.group(1)

        print(f"""
{colors.Red+"+----------------------------------------------------+"}
{colors.blue}Decimal:{colors.yellow} {decimal}
{colors.blue}Host Name:{colors.yellow} {hostname}
{colors.blue}ASN:{colors.yellow} {asn}
{colors.blue}ISP:{colors.yellow} {isp}
{colors.blue}Assignment:{colors.yellow} {assignment}
{colors.blue}Country:{colors.yellow} {country}
{colors.blue}State/Region:{colors.yellow} {state_region}
{colors.blue}City:{colors.yellow} {city}

{colors.magenta}Its map is in the "index.html" file in your directory!
{colors.Red+"+----------------------------------------------------+"}

        """)

if __name__=="__main__":
   print(colors.white+"""   dMP .aMMMb  .dMMMb  dMP dMMMMb dMMMMMMP 
   amr dMP"dMP dMP" VP amr dMP dMP   dMP    
  dMP dMP dMP  VMMMb  dMP dMP dMP   dMP     
 dMP dMP.aMP dP .dMP dMP dMP dMP   dMP      
dMP  VMMMP"  VMMMP" dMP dMP dMP   dMP       
                                        
v0.1.0                                      
""")
   İnfoİP()

