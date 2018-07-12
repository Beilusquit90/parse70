import re
import urllib.request
from datetime import datetime
from dateutil.parser import parse
from bs4 import BeautifulSoup
import urls


def get_html(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)

    return response.read()



def f79(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('article', attrs={'role': 'article'})
    for node in nodes:
        item = {}
        item['action_link'] = node.h3.a['href']
        print(node.h3.a['href'])
        item['tittle'] = node.h3.a.text.strip().replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        item['description'] = node.p.text.strip().replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f78(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'tile-content'})
    for node in nodes:
        item = {}
        item['tittle'] = node.h4.text.replace('\n', ' ').replace('\xad', '-').replace('  ', ' ').replace(
            '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        href= node.find_all('div', attrs={'class': 'tile-footer'})
        for x in href:
            item['action_link'] =x.a['href']
        discr= node.find_all('div', attrs={'class': 'tile-text'})
        for x in discr:
            item['description'] = x.p.text.replace('\n', ' ').replace('\xa0', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()

        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f77(url):
    response = urllib.request.urlopen(url + "?page=1&pagesize=100")
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes2 = filter(None, (key.parent.parent.parent for key in soup(
        text=re.compile('Take Action'))))
    for node in nodes2:
        item = {}
        item['tittle'] = node.h2.text
        item['post_date'] = datetime.now()
        item['action_link'] = url + node.a['href']

        html2 = (urllib.request.urlopen(url + node.a['href'])).read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('span', attrs={'rc:edit': 'page_text'})
        text = " "
        for zz in nodes2:
            text = text + zz.p.text + " "
        item['description'] = text
        items.append(item)
        break

    nodes = filter(None, (key.parent.parent.parent.parent.parent for key in soup(
        text=re.compile('''TAKE
                        ACTION'''))))
    for node in nodes:
        item = {}
        item['tittle'] = node.h3.text
        item['post_date'] = datetime.now()
        item['action_link'] = url + node.h3.a['href']

        html2 = (urllib.request.urlopen(url + node.a['href'])).read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('span', attrs={'rc:edit': 'page_text'})
        text = " "
        for zz in nodes2:
            text = text + zz.text + " "
        item['description'] = text
        items.append(item)
    return items


def f76(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'grid-item'})
    for node in nodes:
        item = {}
        item['action_link'] = node.a['href']
        item['tittle'] = node.a.text.strip()
        item['description'] = item['tittle']
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f75(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    tits=[]
    discrs=[]
    hrefs=[]
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('h3', attrs={'class': 'description'})
    for node in nodes:
        if(node.a):
            hrefs.append(node.a['href'])
            tits.append(node.a.text.strip())

    soup2 = BeautifulSoup(html, 'html.parser')
    nodes2 = soup2.find_all('div', attrs={'class': 'description'})
    for node in nodes2:
        if(node.p):
            discrs.append(node.p.text.strip())

    for x in range(0,len(tits)):
        item = {}
        item['action_link'] = hrefs[x]
        item['tittle'] = tits[x]
        item['description'] = discrs[x]
        item['post_date'] = datetime.now()
        items.append(item)
    return items




def f74(url):
    response = urllib.request.urlopen(
        'http://www.congressweb.com/9to5/takeaction?framed_parent_url=http%3A%2F%2F9to5.org%2Faction%2F%23%2Ftakeaction&frame_is_responsive=false&frame_break_out=true')
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all(
        'div', attrs={'class': 'congressweb-action-shortdesc'})
    for node in nodes:
        item = {}
        item['action_link'] = 'http://www.congressweb.com' + \
            node.parent.div.a['href']
        item['tittle'] = node.parent.div.a.text
        if(node.div):
            item['description'] = node.div.text.replace('\n', ' ').replace('\xa0', ' ').replace(
                '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        else:
            item['description'] = node.p.text.replace('\n', ' ').replace('\xa0', ' ').replace(
                '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        item['post_date'] = datetime.now()
        items.append(item)

    return items


def f73(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a', attrs={'data-animate-css': 'fadeInUp'})
    for node in nodes:
        item = {}
        text = node.h3.text.replace('\n', ' ')
        item['tittle'] = text
        item['description'] = node.div.text.replace('\n', ' ')
        item['post_date'] = datetime.now()
        item['action_link'] = node['href']
        items.append(item)

    return items


def f72(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'AlertListDescription'})
    for node in nodes:
        item = {}
        item['tittle'] = node.parent.span.a.text
        item['description'] = node.text
        item['post_date'] = datetime.now()
        item['action_link'] = node.parent.span.a['href']
        items.append(item)

    return items


def f71(url):
    items = []
    flag = 1
    count = 1
    while(flag):
        flag = 0
        try:
            response = urllib.request.urlopen(
                url + '?wpv_column_sort_id=post_date&wpv_column_sort_dir=desc&wpv_post_id=401&wpv_view_count=50-CPID401&wpv_paged=' + str(count) )
        except:
            print('danger')
            break
        count += 1
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('a', attrs={'class': 'button take-action'})
        for node in nodes:
            item = {}
            item['action_link'] = node['href']
            item['tittle'] = node.parent.parent.h3.a.text.replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['description'] = node.parent.parent.p.text.replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['post_date'] = datetime.now()
            items.append(item)
            flag = 1
    return items

def f70(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    temp = []
    for node in nodes:
        if (node['href']in temp):
            continue
        temp.append(node['href'])
        item = {}
        if(node['href'].find('action_KEY') > 0):
            item['action_link'] = node['href']
            item['tittle'] = node.text.strip().replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ','')
            opener2 = urllib.request.build_opener()
            opener2.addheaders = [('User-Agent',
                                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
            response2 = opener2.open(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'class': 'description'})
            text = ""
            for node2 in nodes2:
                text += node2.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                         ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ')
            item['description'] = text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
    return items


def f69(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node['href'].find('action_KEY') > 0):
            item['action_link'] = node['href']
            item['tittle'] = node.strong.text.replace('\xa0', ' ').strip()
            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'class': 'description'})
            text = ""
            for node2 in nodes2:
                text += node2.p.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                           ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ').replace('\xa0', ' ')
            item['description'] = text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
    return items


def f68(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'description'})
    count = 0
    for node in nodes:
        count = count + 1
        if(count == 1):
            continue
        item = {}
        t1 = (node.parent.span.a.text).find('\n\t\t\t\t\t ')
        t2 = (node.parent.span.a.text).rfind('\n\t\t\t\t\t ')
        t1 = t1 + (len("\n\t\t\t\t\t "))
        item['tittle'] = node.parent.span.a.text[t1:t2]
        item['description'] = node.text
        item['post_date'] = datetime.now()
        item['action_link'] = url + node.parent.span.a['href']

        items.append(item)
    return items


def f67(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Take Action!'))))
    for node in nodes:
        item = {}
        tt= node['href'].find('issues/bills')
        item['action_link'] = url+node['href'][tt:]
        item['tittle'] = node.parent.parent.parent.h4.a.text.strip()
        item['description'] = node.parent.parent.parent.div.div.text.strip()
        item['post_date'] = datetime.now()
        items.append(item)
    return items

def f66(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all(
        'div', attrs={'style': 'background-color: rgb(246, 246, 246)'})
    for node in nodes:
        item = {}
        item['action_link'] = node.a['href']
        item['description'] = node.text
        item['post_date'] = datetime.now()

        response = urllib.request.urlopen(node.a['href'])
        html = response.read()

        soup2 = BeautifulSoup(html, 'html.parser')
        nodes2 = soup2.find_all('div', attrs={'class': 'item'})
        for node2 in nodes2:
            item['tittle'] = node2.h3.text
        items.append(item)
    return items


def f65(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'content-wrap'})
    for node in nodes:
        item = {}
        tt = node.h3.a['href'][1:].find("engagementId")
        item['action_link'] = (
            "http://cqrcengage.com/ncoa/app/take-action" + node.h3.a['href'][tt:])
        item['tittle'] = node.h3.a.text
        item['description'] = node.div.p.text
        item['post_date'] = datetime.now()

        items.append(item)
        print(item)
    return items


def f64(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node['href'].find('./app/bill/') == 0):
            tt = node['href'].find(';')
            item['action_link'] = 'http://cqrcengage.com/swhr' + node['href'][1:tt]
            item['tittle'] = node.p.text.replace('\xa0', ' ').strip()

            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('section', attrs={'class': 'description'})
            text = ""
            for node2 in nodes2:
                text += node2.p.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                           ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ')
            item['description'] = text

            nodes3 = soup2.find_all('section', attrs={'class': 'introduced '})
            for node3 in nodes3:
                item['post_date'] = parse(node3.p.text.strip())

            items.append(item)
            print(item)
    return items


def f63(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    temp = []
    for node in nodes:
        item = {}
        if(node.span):
            if (node.span.text):
                if(node['href'].find('engagementId') > 0):
                    if(node['href'] in temp):
                        continue
                    temp.append(node['href'])
                    item['action_link'] = 'http://www.npaf.org' + node['href'][1:]
                    item['tittle'] = node.span.text.replace('\xa0', ' ').replace('\n', ' ').replace(
                        '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
                    item['description'] = node.parent.parent.div.p.text.replace('\xa0', ' ').replace('\n', ' ').replace(
                        '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
                    item['post_date'] = datetime.now()
                    items.append(item)
                    print(item)


def f62(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'content-wrap'})
    for node in nodes:
        item = {}
        tt = node.h3.a['href'][1:].find("engagementId")
        item['action_link'] = (
            "http://pornharmsaction.com/app/take-action" + node.h3.a['href'][tt:])
        item['tittle'] = node.h3.a.span.text
        item['description'] = node.div.p.text
        item['post_date'] = datetime.now()

        items.append(item)
    return items

def f61(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'wrap-inner'})
    print('azaza')
    for node in nodes:
        item = {}
        for x in node.find_all('div', attrs={'class': 'text'}):
            item['tittle'] = (x.p.text+' '+ x.a.text).replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['action_link'] = x.a['href']
        item['description'] = item['tittle']
        item['post_date'] = datetime.now()
        items.append(item)
        print(item)
    return items


def f60(url):
    items = []
    flag = 1
    cc = 0
    while flag == 1:
        flag = 0
        response = urllib.request.urlopen(url + "?page=" + str(cc))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('div', attrs={'class': 'col-md-18'})
        for node in nodes:
            flag = 1
            item = {}
            item['action_link'] = node.h2.a['href']
            item['tittle'] = node.h2.a.text
            item['post_date'] = parse(node.div.text)
            text = ""
            count = 0
            for x in node:
                count += 1
                if(count < 3):
                    continue
                text += x.text + '''
    '''
            item['description'] = text
            items.append(item)
            print(item)
        cc += 1


def f59(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'AlertList'})
    for node in nodes:
        item = {}
        item['action_link'] = node.span.a['href']
        item['tittle'] = node.span.a.text
        item['post_date'] = datetime.now()

        response = urllib.request.urlopen(node.span.a['href'])
        html = response.read()
        soup2 = BeautifulSoup(html, 'html.parser')
        nodes2 = soup2.find_all('form', attrs={'id': 'beanForm'})
        text = ""
        for node in nodes2:
            text += node.p.text + '''
'''
        item['description'] = text
        items.append(item)
    return items


def f58(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('img', attrs={'alt': 'Take ACtion Button'})
    for node in nodes:
        item = {}
        item['action_link'] = node.parent['href']
        item['tittle'] = node.parent.parent.parent.parent.h4.text.strip()
        response2 = urllib.request.urlopen(item['action_link'])
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('div', attrs={'id': 'signupheader'})
        text = ""
        for node2 in nodes2:
            text += node2.h1.text.replace('  ', ' ').replace('  ', ' ').replace(
                '  ', ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ').strip()
        item['description'] = text
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f56(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'right-text'})
    for node in nodes:
        item = {}
        item['action_link'] = node.h1.a["href"]
        tt = node.h1.a.text.rfind('\t')
        item['tittle'] = node.h1.a.text[tt + 1:]
        if(node.p):
            item['description'] = node.p.text
        else:
            item['description'] = node.h2.text
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f55(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('li', attrs={'class': 'AlertList'})
    for node in nodes:
        item = {}
        item['action_link'] = node.a['href']
        item['tittle'] = node.a.text
        response = urllib.request.urlopen(node.a['href'])
        html = response.read()
        soup2 = BeautifulSoup(html, 'html.parser')
        nodes2 = soup2.find_all('form', attrs={'id': 'beanForm'})
        text = ""
        for node2 in nodes2:
            text += node2.p.text + '''
'''
        item['description'] = text.replace('\n', ' ')
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f54(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('h1')
    for node in nodes:
        if(node.a):
            item = {}
            if(node.a['href'].find('/') == 0):
                item['action_link'] = 'http://www.ajcongress.org' + node.a['href']
            else:
                item['action_link'] = node.a['href']
                item['post_date'] = datetime.now()
                item['tittle'] = node.a.text
            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'class': 'field-item even'})
            text = ""
            for node2 in nodes2:
                if(node2.p):
                    text += node2.p.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                               ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ')
                # break
            item['description'] = text
            items.append(item)
    return items

def f52(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'congressweb-action-shortdesc'})
    for node in nodes:
        item = {}
        item['action_link'] = node.parent.div.a['href']
        item['tittle'] = node.parent.div.a.text.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        item['description'] = node.div.text.replace('\n', ' ').replace('\xa0', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        item['post_date'] = datetime.now()
        items.append(item)
        print(item)
    return items

def f51(url):
    items = []
    flag = 1
    count = 0
    while(flag):
        flag = 0
        url = 'http://peacenow.org/issue.php?cat=action-alerts&start=' + \
            str(count * 10) + '&limit=10'
        count += 1
        response = urllib.request.urlopen(url)
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('span', attrs={'class': 'entry_authored_on'})
        for node in nodes[1:]:
            item = {}
            if(node.parent.parent.h2.a['href'].find('/entry.php') == 0):
                # if(node.parent.parent.h2.a.text.find('Action')>(-1)and
                # node.parent.parent.h2.a['href'].find('/entry.php')==0):
                # TODO change this if only action needed
                item['action_link'] = 'http://peacenow.org' + \
                    node.parent.parent.h2.a['href']
                item['tittle'] = node.parent.parent.h2.a.text.replace(
                    '\xa0', ' ').strip()
                nodes2 = node.parent.parent.parent.find_all(
                    'div', attrs={'class': 'asset-body'})
                for node2 in nodes2:
                    item['description'] = node2.p.text.replace('\n', ' ').strip().replace('\xa0', ' ').replace(
                        '      ', ' ').replace('  ', ' ').replace('   ', ' ').replace('  ', ' ')
                item['post_date'] = parse(node.text.replace('\n', ''))
                items.append(item)
                flag = 1
    return items


def f50(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node['href'].find('http://p2a.co/') == 0):
            item['action_link'] = node['href']
            item['tittle'] = node.img['title'].replace('\xa0', ' ').strip()

            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'id': 'maincontent'})
            text = ""

            for node2 in nodes2:
                if(node2.span):
                    text += node2.span.text
                else:
                    if(node2.div):
                        text += node2.div.text
                    else:
                        text += node2.p.text

            item['description'] = text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
    return items


def f49(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Take Action'))))
    for node in nodes:
        if(node['href'] == 'https://www.nraila.org/take-action/'):
            continue
        item = {}
        item['action_link'] = url + node['href']
        response = urllib.request.urlopen(url + node['href'])
        html2 = response.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all(
            'section', attrs={'class': 'two-columns with-border'})
        for node2 in nodes2:
            item['tittle'] = node2.h1.text
            item['description'] = (((node2.text[len(node2.h1.text) + 3:].replace(
                '\n', ' ')).replace('\r', ' ')).strip().replace('\xa0', ' '))
            item['post_date'] = datetime.now()
            items.append(item)
    return items


def f48(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'content-wrap'})
    for node in nodes:
        item = {}
        tt = node.h3.a['href'][1:].find("engagementId")
        item['action_link'] = (
            "http://cqrcengage.com/gunowners/app/take-action" + node.h3.a['href'][tt:])
        item['tittle'] = node.h3.a.span.text
        item['description'] = node.div.p.text.replace(
            '\n', ' ').replace('\r', ' ').strip().replace('\xa0', ' ')
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f47(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Take Action'))))
    for node in nodes:
        item = {}
        item['action_link'] = node['href']
        item['tittle'] = node.parent.parent.parent.h2.text
        item['description'] = node.parent.parent.parent.p.text.replace(
            '\n', ' ').replace('\r', ' ').strip().replace('\xa0', ' ')
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f46(url):
    items = []
    flag = 1
    count = 1
    while(flag):
        flag = 0
        try:
            response = urllib.request.urlopen(
                url + '?state_or_national=&spstate_or_national=&spissue=&spcampaign=&doctype=action-alert&spstartDate=&spendDate=&sppage=' + str(count) )
        except:
            break
        count += 1
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('article', attrs={'class': 'search_results'})
        for node in nodes:
            item = {}
            item['action_link'] = node.p.a['href']
            if(item['action_link'].find('\t')==1):
                item['action_link']=item['action_link'][2:]
            item['post_date'] = datetime.now()
            item['tittle'] = node.p.a.text.replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['description'] = node.text.replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            if(len(item['description'])<5):
                item['description']=item['tittle']
            items.append(item)
            flag = 1
            print(item)
    print(len(items))
    return items


def f45(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('h2', attrs={'class': 'field-content'})
    for node in nodes:
        item = {}
        item['action_link'] = 'http:' + node.a['href']
        item['post_date'] = datetime.now()
        item['tittle'] = node.a.text
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
            response2 = opener.open('http:' + node.a['href'])
        except:
            continue
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('div', attrs={'class': 'description'})
        item['description'] = ' '
        for node2 in nodes2:
            item['description'] = node2.text.replace('\n', ' ').replace('\xa0', ' ').replace(
                '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        if(item['description'] == ' '):
            nodes3 = soup2.find_all('p')
            text = ''
            for node3 in nodes3:
                text += node3.text.strip()
            item['description'] = text.replace('\n', ' ').replace('\xa0', ' ').replace('  ', ' ').replace(
                '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
        items.append(item)
    return items


def f44(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node.parent.parent.li):
            if(node.img):
                continue
            if(node['href'].find('/action/issues/') == 0):
                item['action_link'] = 'http://www.opensecrets.org' + node['href']
                item['post_date'] = datetime.now()
                response2 = opener.open(item['action_link'])
                html2 = response2.read()
                soup2 = BeautifulSoup(html2, 'html.parser')
                nodes2 = soup2.find_all('div', attrs={'id': 'rightColumn'})
                text = ""
                for node2 in nodes2:
                    item['tittle'] = node2.h1.text.replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace(
                        '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ')
                    item['description'] = node2.p.text.replace('\xa0', ' ').replace('\r\n', ' ').replace(
                        '\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').strip()
                    text += node2.p.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                               ' ').replace('  ', ' ').replace(' ', ' ')
                items.append(item)
    return items



def f42(url):
    items = []
    flag = 1
    count = 1
    while(flag):
        flag = 0
        try:
            response = urllib.request.urlopen(
                url + '/page/' + str(count) + '/')
        except:
            break
        count += 1
        html = response.read()

        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('span', attrs={'class': 'heading-date'})
        for node in nodes:
            item = {}
            item['action_link'] = node.parent.parent.a['href']
            item['post_date'] = node.text
            item['tittle'] = node.parent.parent.a[
                'title'].replace('\xa0', ' ').strip()
            item['description'] = node.parent.parent.p.text.replace(
                '\xa0', ' ').strip()
            items.append(item)
            flag = 1
    return items


def f41(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Sign this petition'))))
    for node in nodes:
        item = {}
        item['action_link'] = url + node['href']
        item['tittle'] = node.parent.parent.div.h4.text
        item['description'] = (
            node.text[len(node.parent.parent.div.p.text) + 3:].replace('\n', ' '))
        item['post_date'] = datetime.now()
        items.append(item)
    return items




def f40(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node['href'].find('letter_KEY') > 0):
            item['action_link'] = node['href']
            item['tittle'] = node.text.replace('\xa0', ' ').strip()
            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            html2=html2
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'class': 'salsa'})
            text = ""
            for node2 in nodes2:
                text += node2.p.text.replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
                break
            item['description'] = text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
            print(item)
    return items

def f39(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'engagement-card-content'})
    for node in nodes:
        item = {}
        item['action_link'] = node.a['href']
        item['tittle'] = node.a.h3.text
        item['description'] = node.p.text.replace('\n', ' ')
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f37(url):
    items = []
    flag = 1
    count = 1
    while(flag):
        flag = 0
        try:
            response = urllib.request.urlopen(
                url + '?field_issues_tid=All&field_region_state_tid=All&page=' + str(count))
        except:
            break
        count += 1
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        nodes = soup.find_all('div', attrs={'class': 'inner'})
        for node in nodes:
            item = {}
            for x in node.find_all('div', attrs={'class': 'item-title'}):
                item['tittle'] = x.a.text.replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
                item['action_link'] = x.a['href']

            for x in node.find_all('div', attrs={'class': 'item-body'}):
                item['description'] =x.p.text.replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()

            item['post_date'] = datetime.now()
            items.append(item)
            flag = 1
    return items



def f36(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('li', attrs={'class': 'all'})
    for node in nodes:
        item = {}
        if(node.div.a):
            item['action_link'] = node.div.a['href']
        else:
            item['action_link'] = node.a['href']

        item['tittle'] = node.h3.text
        item['description'] = node.p.text.replace('\n', ' ')
        item['post_date'] = datetime.now()
        items.append(item)
        print(item)
    return items


def f34(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'id': 'actions'})
    for node in nodes:
        for x in node.find_all('div', attrs={'class': 'slick-nook-body'}):
            item = {}
            item['tittle'] = x.parent.div.text.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['description'] = x.text.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            try:
                item['post_date'] = parse(item['tittle'][-13:])
            except:
                item['post_date'] = datetime.now()
            items.append(item)
            print(item)
    return items

def f33(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'id': 'actions'})
    for node in nodes:
        for x in node.find_all('div', attrs={'class': 'slick-nook-body'}):
            item = {}
            item['tittle'] = x.parent.div.text.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            item['description'] = x.text.replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
            try:
                item['post_date'] = parse(item['tittle'][-13:])
            except:
                item['post_date'] = datetime.now()
            items.append(item)
            print (item)
    return items



def f32(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'media__content'})
    for node in nodes:
        item = {}
        item['action_link'] = node.a['href']
        item['tittle'] = node.a.text
        response2 = urllib.request.urlopen(node.a['href'])
        html2 = response2.read()

        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('form', attrs={'id': 'beanForm'})
        text = ""
        for node2 in nodes2:
            text += node2.text.strip()
        item['description'] = (text.replace('\n', ' '))
        item['post_date'] = parse(node.span.text)
        items.append(item)
    return items


def f31(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    temp = []
    for node in nodes:
        if (node['href']in temp or node.img):
            continue
        temp.append(node['href'])
        item = {}
        if(node['href'].find('action_KEY') > 0 or node['href'].find('org.salsalabs.com/dia/track.jsp?') > 0):
            if(not(node.text)or len(node.text) < 5):
                continue

            item['action_link'] = node['href']
            if(node.text == 'Take action'):
                item['tittle'] = node.parent.parent.p.text
            else:
                item['tittle'] = node.text
            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'class': 'description'})
            text = ""
            for node2 in nodes2:
                text += node2.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ',
                                                                                         ' ').replace('  ', ' ').replace(' ', ' ').replace('\n', ' ')

            item['description'] = text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
    return items


def f30(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('div', attrs={'class': 'grid-item'})
    for node in nodes:
        item = {}
        item['action_link'] = node.article.div.a['href']
        item['tittle'] = node.article.div.a['title']
        response2 = urllib.request.urlopen(node.article.div.a['href'])
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, 'html.parser')
        nodes2 = soup2.find_all('div', attrs={'class': 'action-topic'})
        text = ""
        for node2 in nodes2:
            text += node2.p.text.strip()
        item['description'] = text
        item['post_date'] = datetime.now()
        items.append(item)
    return items


def f29(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    response = opener.open(url)

    html = response.read()

    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')[35:]
    for node in nodes:
        try:
            if(node['href'].find('/action-alerts') == 0):
                tt = node['href'].find('?source_code=04AA17AC')
                item = {}
                item['action_link'] = 'http://www.americanforests.org' + node['href']
                item['tittle'] = node.text
                item['post_date'] = datetime.now()
                item['description'] = item['tittle']
                #response2 = urllib.request.urlopen(item['action_link'])
                #html2 = response2.read()
                #print(html2)
                #soup2 = BeautifulSoup(html2, 'html.parser')
                #nodes2 = soup2.find_all('p', attrs={'class': 'ad_Item'})
                #text = ""
                #print(item['action_link'])
                #print('START TEXT FOUND')
                #for node2 in nodes2:
                #    print(node2)
                 #   print(node2.text)
                    # print(node2.h2.text)
                    # text += node2.text.strip().replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ',' ').replace(' ', ' ').replace('\n', ' ')

                    #
                    #item['description'] = node.parent.p.text
                    #
                print(item)
                items.append(item)
        except:
            continue
    return items

def f28(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('hgroup')
    for node in nodes:
        item = {}
        item['action_link'] = 'http://www.cqrcengage.com/nami' + \
            node.parent.a['href'][1:]
        item['tittle'] = node.h1.text
        item['description'] = node.parent.p.text
        item['post_date'] = datetime.now()
        items.append(item)
    return items

def f27(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Action Alert>'))))
    for node in nodes:
        item = {}
        ldata={'2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2009','2008','2007','2006'}
        if(node.parent.text.find('Action Alert>')>0 and node.parent.text.find('Action Alert>')<20):
            item['description']=(node.parent.parent.text[:node.parent.parent.text.find('<!--')].replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip())
        else:
            item['description']=(node.parent.text.replace('\xa0', ' ').replace('\n', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip())

        item['post_date'] = ' '
        for x in ldata:
            try:
                if(item['description'][:20].find(x)>0):
                    z=item['description'][:20].find(x)
                    item['post_date'] = parse(item['description'][:z+4])
            except:
                continue

        if(item['post_date'] ==' '):
            item['post_date'] =datetime.now()

        if(node.parent.a):
            if(node['href'][0] == '/'):
                item['action_link'] = 'http://www.bazelon.org/' + node['href']
            else:
                item['action_link'] = node['href']
            if (node['href'][0] == '.'):
                item[
                    'action_link'] = 'http://www.bazelon.org/What-You-Can-Do/Take-Action/' + node['href']
        else:
            if (node.parent['href'][0] == '/'):
                item['action_link'] = 'http://www.bazelon.org/' + \
                    node.parent['href']
            else:
                item['action_link'] = node.parent['href']
            if (node.parent['href'][0] == '.'):

                item['action_link'] = 'http://www.bazelon.org/What-You-Can-Do/Take-Action/' + \
                    node.parent['href']
        print(item)
        items.append(item)
    return items

def f26(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('li', attrs={'class': 'clearfix'})
    for node in nodes:
        item = {}
        tt = node.h3.a['href'][1:].find("engagementId")
        item['action_link'] = (
            "http://disabilityadvocacynetwork.org/app/take-action" + node.h3.a['href'][tt:])
        item['tittle'] = node.h3.a.span.text
        item['description'] = node.div.p.text.strip()
        item['post_date'] = datetime.now()
        items.append(item)
    return items

def f25(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = filter(None, (key.parent for key in soup(
        text=re.compile('Take Action'))))
    for node in nodes:
        if(node.parent.p):
            item = {}
            if(node['href'][0] == 'h'):
                item['action_link'] = node['href']
            else:
                item['action_link'] = 'https://www.rainn.org/' + node['href']
            item['tittle'] = node.parent.h3.a.text.strip()
            item['description'] = node.parent.p.text.strip()
            item['post_date'] = datetime.now()
            items.append(item)

    return items

def f24(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    items = []
    soup = BeautifulSoup(html, 'html.parser')
    nodes = soup.find_all('a')
    for node in nodes:
        item = {}
        if(node['href'].find('http://conta.cc/') == 0):
            item['action_link'] = node['href']
            item['tittle'] = node.text.replace('\xa0', ' ').strip()

            response2 = urllib.request.urlopen(item['action_link'])
            html2 = response2.read()
            soup2 = BeautifulSoup(html2, 'html.parser')
            nodes2 = soup2.find_all('div', attrs={'dir': 'ltr'})
            text = ""
            for node2 in nodes2:
                text += node2.text.replace('\n', ' ').replace('  ', ' ').replace(
                    '  ', ' ').replace('  ', ' ').replace('  ', ' ').replace(' ', ' ').strip()
                # break

            # item['description'] = node.div.p.text.strip()
            item['post_date'] = datetime.now()
            items.append(item)
    return items



if __name__ == '__main__':
    murl=urls.urls
    p = 65
    print((murl[p]))
    get_html(murl[p])
    f65(murl[p])
    print('-----------------------')
    print('programm end.')


# f24() # No descriptions
# f25() #ВЫЕБАНО
# f26() #ВЫЕБАНО
# f27() # TODO                  #РАСПАРСИЛ ВСЁ КРОМЕ ТИТУЛА!
# f28() #ВЫЕБАНО
# f29() #ВЫЕБАНО           #НЕ СМОГ ЗАПАРСИТЬ ДЕСКРИПШН
# f30() #ВЫЕБАНО
# f31() #ВЫЕБАНО
# f32() #ВЫЕБАНО
# f33() #ВЫЕБАНО
# f34() #ВЫЕБАНО
# 35 ACCESS DENIED
# f36() #ВЫЕБАНО
# f39() #ВЫЕБАНО
# 38 не понятно что парсить  ПОКА ЧТО НАХУЙ ОКЕАН
# f39() #ВЫЕБАНО
# f40() #ВЫЕБАНО
# f41() #ВЫЕБАНО
# f42() #ВЫЕБАНО
# 43    Website got no data.
# f44() #ВЫЕБАНО
# f45() #ВЫЕБАНО
# f46() #ВЫЕБАНО
# f47() #DONE
# f48() #DONE
# f49() #DONE
# f50() #DONE
# f51() #DONE
# f52() #DONE
# 53    Website got no data.
# f54() #DONE
# f55() #DONE
# f56() #DONE
# 57    Website got no data.
# f58() #DONE
# f59() #DONE
# f60() #DONE
# f62() #DONE
# f62() #DONE
# f63() #DONE
# f64() #DONE
# f65() #DONE
# f66() #DONE
# f67() #DONE
# f68() #DONE
# f69() #DONE
# f70() #DONE
# f71() #DONE
# f72() #DONE
# f73() #DONE
# f74() #DONE
# f75() #DONE
# f76() #DONE
# f77() #DONE
# f78() #DONE
# f79() #DONE
