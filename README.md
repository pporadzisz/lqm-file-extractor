# lqm-file-extractor
Small Python tool for extract text content from lqm and jlqm file format (QuickMemo+)


# Instalation (Linux):

Download extract.py file
wget https://raw.githubusercontent.com/pporadzisz/lqm-file-extractor/master/extract.py


# Usage:

python3 extract.py path_to_lqm_files


# Example:

python3 extract.py /home/radny/Downloads/quickmemo_plus


Result:

'#####        QuickMemo+_190212_021335(1).lqm          #####

Text:
Nokia 6.1
Lg q7


'#####        QuickMemo+_190212_021340(1).lqm          #####

Text:
My second text script


'#####        QuickMemo+_190212_021338(2).lqm          #####

Text:
96




# Step by step

All you have to do is :

1.Use Share option in QuickMemo+ on Android device. 

2."Select all" and click "Share" button.

3.Select "QuickMemo+ file (.lqm)" option.

4.Save *.lqm files into Google Drive.

5.Download files from Google Drive into one local folder.

6.Download extractor.py file

7.Please run command in terminal : 

python3 extract.py /home/radny/Downloads/quickmemo


And as a result you'll see:

'##### QuickMemo+_190212_021335(1).lqm #####

Text: Nokia 6.1 Lg q7

'##### QuickMemo+_190212_021340(1).lqm #####

Text: My second text script

'##### QuickMemo+_190212_021338(2).lqm #####

Text: 96
