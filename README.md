![N|Solid](https://img.shields.io/pypi/l/py-vkontakte.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/21c92d804ab541c8ae219b7098df3173)](https://www.codacy.com/app/murych/postin-in-vk-from-trello?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=murych/postin-in-vk-from-trello&amp;utm_campaign=Badge_Grade)

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

- Edit `run.sh` file path to `activate` script in your virtual environment

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

- Check if everything runs without any errors:
```bash
workon trello-vk  # in case you've logged out
python /path/to/your/project/main.py
```

- Make `run.sh` executable:
```bash
chmod +x run.sh
```

- Create a cron job, executing every 5 minutes:
```bash
crontab -e
```
add this to the end of your `*/crontab`
```
 */5 * * * * /path/to/repo/run.sh
```
