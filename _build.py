url_nbviewer = "https://nbviewer.jupyter.org"
url_github = "/github/pinedance/workshop-KM-data-analysis"
url_path = "/blob/master/notebooks"
url_full = url_nbviewer + url_github + url_path


with open("_template/_README.md", 'r', encoding="utf-8") as fl:
    text = fl.read()

new_text = text.replace( "*URL*", url_full )

# README.md

with open("README.md", 'w', encoding="utf-8") as fl:
    fl.write( new_text )
    
    
    
# README.ipynb

readme_ipynb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [  new_text  ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

    
import json
    
with open("notebooks/README.ipynb", 'w', encoding="utf-8") as fl:
    fl.write( json.dumps( readme_ipynb )  )
 
