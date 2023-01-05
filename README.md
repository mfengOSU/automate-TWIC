# automate-TWIC
Automatically download chess PGNs from The Week In Chess (TWIC) and save them to your computer

## How to Use
In twic.py, change the values of `START_NUM` and `END_NUM` to indicate the first and last TWIC pgn files you want to download, respectively. The program will download all TWIC pgn files starting from `START_NUM` to and including `END_NUM`.

To run the code, type 
```
python twic.py
```
in your terminal.

## Requirements
- python 3+

The requests library was used. To install it, run
```
python -m pip install requests
```
in your terminal.

