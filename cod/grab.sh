#!/bin/bash
FILES=/home/trev/cod/bois/*
for f in $FILES
do
wget 'https://cod.tracker.gg/modern-warfare/profile/psn/'$(echo ${f} | sed -e "s/.*bois\/\(.*\).*/\1/")'/overview'
  cat overview* > $f
  rm overview*
  sleep 5
  # take action on each file. $f store current file name
  # cat $f
done