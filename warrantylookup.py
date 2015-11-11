import subprocess
import lxml
import bs4
import datetime

class Dell:
    def __init__(self, timeout=15):
        self.apikey = 'd676cf6e1e0ceb8fd14e8cb69acd812d'
        self.url = 'https://api.dell.com/support/v2/assetinfo/warranty/tags.xml?svctags=%s&apikey=%s'
        self.timeout = timeout
    
    def getWarrantyInfo(self, servicetag):
        url = self.url % (servicetag, self.apikey)
        curl = subprocess.Popen(["curl.exe",
                                     "--connect-timeout",
                                     str(self.timeout),
                                     "--proxy",
                                     "10.97.8.18:80",
                                     "--proxy-user",
                                     "overmanjerem@bfusa.com:Swf1067pw12",
                                     "%s" % url], stdout=subprocess.PIPE)
             
        response = curl.communicate()[0]
        
        soup = bs4.BeautifulSoup(response, "xml")
        
        enddates = []
        
        for enddate in soup.find_all("EndDate"):
            parse = enddate.text.split("T")[0]
            year, month, day = parse.split("-")
            date = datetime.date(int(year), int(month), int(day))
            enddates.append(date)
        
        if len(enddates) > 0:    
            enddate = max(enddates)
        else:
            enddate = "Not Available"
        try: ordernum = soup.find_all("OrderNumber")[0].text
        except IndexError: ordernum = None
        try: machinetype = soup.find_all("MachineDescription")[0].text.split(",")[0]
        except IndexError: machinetype = None
        
        return enddate, ordernum, machinetype

if __name__ == "__main__":
    delllookup = Dell()
    print delllookup.getWarrantyInfo("gvn7zq1")