@echo off

title Toontown Offline - Astron Server

cd..
cd astron
astrond --loglevel info config/astrond.yml
pause