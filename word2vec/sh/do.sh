#!/bin/bash

ROOT_DIR=/home/iknow/wc/jupyter/xing_nlp/word2vec

for file in $ROOT_DIT/jobs/*
do
  bash file >> result.txt
done