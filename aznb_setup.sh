#!/bin/bash

# Activate env
source /home/nbuser/anaconda3_501/bin/activate

# conda
conda config --add channels conda-forge
conda install gensim -y
conda install bokeh -y
