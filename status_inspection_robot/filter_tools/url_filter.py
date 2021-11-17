# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Author   ：jiamid
@Time     ：2021/11/16 15:37
@File     ：url_filter.py
@Software ：PyCharm
"""
import re


def format_url_filter(url):
    if 'gounlimited.to/embed-' in url:
        url = url.replace("gounlimited.to/embed-", 'gounlimited.to/')

    elif '4movierulz.nl' in url:
        id = re.findall('/\?l=(\w+)', url)[0]
        url = 'https://hqq.tv/player/embed_player.php?vid={}'.format(id)

    elif 'dood.watch/d/' in url:
        url = url.replace('dood.watch/d/', 'dood.watch/e/')

    elif 'gofile.io' in url:
        keyid = re.search(r'\?c=(.*)', url).group(1)
        url = 'https://apiv2.gofile.io/getServer?c=%s' % keyid

    elif 'filepup.net' in url:
        url = url.replace('https://', 'http://')

    elif 'thevid.net/v/' in url:
        url = url.replace('thevid.net/v/', 'thevid.net/e/')

    elif 'mystream.to' in url:
        keyid = ""
        if 'embed' in url:
            keyid = re.search(r'embed.mystream.to/(.*)', url).group(1)
        else:
            keyid = re.search(r'mystream.to/watch/(.*)', url).group(1)
        url = 'https://app.mystream.to/video-info/%s' % keyid

    elif 'movcloud.net' in url:
        keyid = re.search(r'movcloud.net/embed/(.*)', url).group(1)
        url = 'https://api.movcloud.net/stream/%s' % keyid
    elif 'vidbom.com' in url or 'vidbom.com' in url:
        url = url.replace("embed-", "")
    elif 'vidlox.tv' in url:
        url = url.replace("vidlox.tv", "vidlox.me")
    elif 'sbembed.com' in url:
        keyid = ""
        if 'embed' in url:
            keyid = re.search(r'sbembed.com/embed-(.*).html', url).group(1)
        else:
            keyid = re.search(r'sbembed.com/(.*).html', url).group(1)
        url = 'https://sbvideo.net/play/%s?auto=1&referer=&' % keyid
    elif 'sbvideo.net' in url:
        keyid = ""
        if 'embed' in url:
            keyid = re.search(r'sbvideo.net/embed-(.*).html', url).group(1)
        else:
            keyid = re.search(r'sbvideo.net/(.*).html', url).group(1)
        url = 'https://sbvideo.net/play/%s?auto=1&referer=&' % keyid
    elif 'sbplay.org' in url:
        keyid = ""
        if 'embed' in url:
            keyid = re.search(r'sbplay.org/embed-(.*).html', url).group(1)
        else:
            keyid = re.search(r'sbplay.org/(.*).html', url).group(1)
        url = 'https://sbplay.org/play/%s?auto=1&referer=&' % keyid
    elif 'sbplay.one' in url:
        keyid = ""
        if 'embed' in url:
            keyid = re.search(r'sbplay.one/embed-(.*).html', url).group(1)
        else:
            keyid = re.search(r'sbplay.one/(.*).html', url).group(1)
        url = 'https://sbplay.one/play/%s?auto=1&referer=&' % keyid
    elif 'jetload.net' in url:
        if url.startswith("http:"):
            url = url.replace("http:", "https:")
        if ('https://jetload.net/e/' not in url) and ('https://jetload.net/p/' not in url) and (
                'https://jetload.net/embed/' not in url):
            return '{"error_code":-2011, "error_extra_info":"Unsupported url"}'
        else:
            keyid = re.search(r'https://jetload.net/./(.*)', url).group(1)
            url = 'https://jetload.net/e/%s' % keyid
    elif 'doodstream.com' in url:
        url = url.replace("doodstream.com", 'dood.la')
    elif 'dood.to' in url:
        url = url.replace("dood.to", 'dood.la')
    elif 'icerbox.com' in url:
        keyid = re.search(r'icerbox.com/(.*)', url).group(1)
        url = "https://icerbox.com/api/v1/file?id=%s" % (keyid)
    elif 'gogoplay1.com/embedplus' in url:
        keyid = re.search(r'gogoplay1.com/embedplus\?id=(\w+)', url).group(1)
        url = "https://gogoplay1.com/streaming.php?id=%s=" % keyid

    elif 'fsapi.xyz/movie/tt' in url:
        imdb_id = re.findall('movie/(tt\d+)', url)[0]
        url = 'https://www.2embed.ru/embed/imdb/movie?id={}'.format(imdb_id)

    return url
