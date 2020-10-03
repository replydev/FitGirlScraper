# FitGirl Scraper Telegram Bot

## How to setup in a debian based system

#### Install the python interpreter and git
`sudo apt install python3 python3-pip git`

`git clone https://codeberg.org/replydev/FitGirlScraper.git`

#### Create a venv inside the main source folder
`python3 -m venv FitGirlScraper`

#### Activate the venv
`cd FitGirlScrapersource`

`source bin/activate`

#### Install requirements
`pip install -r requirements.txt`

#### Create your own config
`cp config.py.example config.py`

`nano config.py`

and insert your bot token

#### Start the bot

`python -m FitGirlScraper`