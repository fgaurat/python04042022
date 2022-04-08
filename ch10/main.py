²                   
from bs4 import BeautifulSoup
import glob
import re

def main():
    logs = glob.glob('*.log')
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # data = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
                ip = re.findall(r'^(.*?)\s',line)
                status = re.findall(r'\"\s(\d{3})',line)
                if '404' in status: 
                    print(ip,status)bn 



def main_download():
    url = "http://logs.eolem.com/"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    links = soup.find_all('a')

    # logs_links = []

    # for a in links:
    #     if "apache" in a['href']:
    #         logs_links.append(a['href'])

    # print(logs_links)
    logs_links = [a['href'] for a in links if "apache" in a['href']]
    print(logs_links)

    for link in logs_links:
        r = requests.get(url+link)
        with open(link,'w') as f:
            print(r.text,file=f)


if __name__ == '__main__':
    main()