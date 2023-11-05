#!/usr/bin/env python3

# accentgrave ~ now
# HTML micro-now tool


rightnowdir = "/your/path/to/now/"

import os
import sys
import datetime
from bs4 import BeautifulSoup
from tidylib import tidy_document
from mdx_linkify.mdx_linkify import LinkifyExtension
import markdown



def main(argv, verbose=False):
  rightnow = argv[0]
    
  # dot dot dot
  if not (rightnow.endswith('.') or rightnow.endswith('…') or rightnow.endswith('!') or rightnow.endswith('?')):
    rightnow = rightnow + "."  

  # transform passed markdown to HTML (wrapped in <p>), with linkify extension
  # so that raw URLs are linkified
  now_html = markdown.markdown(rightnow, extensions=[LinkifyExtension()])
  
  # read and update /now  
  rightnow_doc = os.path.join(nowdir,"index.html")
  with open(rightnow_doc, "r") as f:
    # make soup
    soup = BeautifulSoup(f, 'html5lib')
    # find main
    main = soup.find("main")
    rightnow_soup = BeautifulSoup(now_html, 'html.parser')
    
    # what time is it?
    nowtime = datetime.date.today()
    time = soup.new_tag("time")    
    time.string = nowtime.strftime("%d/%m/%Y").strip()

    # find p
    p = rightnow_soup.find("p")
    
    # create a plain text version (for commit message)
    txtrightnow = rightnow_soup.get_text()
    
    # insert content
    p.insert(0, time)
    main.insert(0,rightnow_soup)

    # clean HTML with Tidy
    prettified = soup.prettify(formatter="minimal")
    document, errors = tidy_document(prettified)
    
  # write /rightnow/index.html
  with open(rightnow_doc, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:      
    output_file.write(document)
  
  # return cleaned text string to stdout
  print(txtrightnow)
  sys.exit()


if __name__ == "__main__":
  main(sys.argv[1:])

