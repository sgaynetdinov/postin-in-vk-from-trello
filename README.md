![N|Solid](https://img.shields.io/pypi/l/py-vkontakte.svg)
![N|Solid](https://img.shields.io/pypi/pyversions/py-vkontakte.svg)

To start:
- Install `virtualenv`
```bash
sudo pip3 install virtualenv virtualenvwrapper
```

- Point it to always run `python3` executable
```bash
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
```

- Point it to directory, where your venv will be placed
```bash
export WORKON_HOME=/path/to/directory
```

- Create new virtual environment
```bash
mkvirtualenv trello-vk
```
- Install requirements in it
```bash
pip install -r requirements.txt
```

- In directory with cloned repo create file `config.ini` and fill it w/ your settings like this:
```ini
[DEFAULT]

[TRELLO]
KEY = AAAAAAAA
TOKEN = AAAAAAAA
BOARD = AAAAAAAA

[VK]
ACCESS_TOKEN = AAAAAAAA
GROUP = AAAAAAAA
```

- Create a cron job, executing every 5 minutes:
```bash
crontab -e
```
add this to the end of your `*/crontab`
```
*/5 * * * * workon trello-vk && python /path/to/your/project/main.py
```
