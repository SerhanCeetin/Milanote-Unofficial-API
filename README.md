# Unofficial Milanote API for Python

![GitHub](https://img.shields.io/github/license/SerhanCeetin/Milanote-Unofficial-API)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Milanote-Unofficial-API)

This is an unofficial api for [Milanote](https://milanote.com/). It can be used to automate planned tasks on Milanote. <br>
It is **not** affiliated with Milanote in any way.<br>
<br>
<br>
#### Disclaimer:
Please do not use this to spam or do anything illegal.<br>
I am not responsible for any misuse of this library.


## Table of Contents

- [Documentation](#documentation)
- [Installation](#installation)
- [Quickstart](#quickstart)
  - [How to get headers and cookies](#how-to-get-headers-and-cookies)
  - [Example usage](#example-usage)

## Documentation

Documentation can be found [here](https://serhanceetin.github.io/Milanote-Unofficial-API/docs).

## Installation

```bash
pip install milanote-unofficial-api
```

## Quickstart

### How to get headers and cookies
1. Login your Milanote account in your browser and go to home page.
2. Open the developer tools (F12) and go to the network tab.
3. Filter the results by `Fetch/XHR` and reload the page.
4. You should see a request to `me`. Right click on it and click `Copy -> Copy as cURL (bash)`.
5. Go to [curlconverter.com](https://curlconverter.com/) and paste the copied text.
6. Get the headers and cookies from the generated code.
7. Now you can use the headers and cookies in the example below.

### Example usage

```python
from MilanoteUnofficialApi import MilanoteApi

my_headers = {...}
my_cookies = {...}

api = MilanoteApi(headers=my_headers, cookies=my_cookies)

# Get the user's home board.
home_board = api.get_home_board()

# Get the board by id.
my_board = api.get_board_by_id("1Pwm1W1wCvBF4C")

# Get the sub elements of the board.
for board in my_board.elements["BOARD"]:
    api.get_board_elements(board)

if(my_board.elements["TASK"]):
    for task in my_board.elements["TASK"]:
        print(task.text_content,
              "completed" if task.is_complete else "not completed")
```
