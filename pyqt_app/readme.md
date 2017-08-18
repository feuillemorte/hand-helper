## Build (Ubuntu): ##
* Install python 3.5

* Create virtualenv and activate it:
```
    python3.5 -m venv env
    source env/bin/activate
```

* Install packages:
```
    pip install -r requirements.txt
```

* Install pyinstaller:
```
    pip install pyinstaller
```

* Run command
```
    pyinstaller --onefile --clean -y --noconsole linux.spec
```

* Check bin file in dist folder

## Install (Ubuntu): ##
* Install google chrome

* Create virtualenv and activate it:
```
    python3 -m venv env
    source env/bin/activate
```

* Install packages:
```
    pip3 install -r requirements.txt
```

* (OPTIONAL) Copy configs/config_default.yml to configs/config.yml and edit config.yml with your requirements

## Install (Mac os): ##
* Install google chrome

* Install brew (if not installed):
```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Install python3:
```
    brew install python3
```
    
* Install pip:
```
    sudo easy_install pip
```

* Install packages:
```
    pip install -r requirements.txt
```
    
* (OPTIONAL) Copy configs/config_default.yml to configs/config.yml and edit config.yml with your requirements

## How to start ##
* Go to hand-helper folder (if not activated yet):
* activate virtualenv (if not activated yet):
```
    source env/bin/activate
```

* Start hand-helper:
```
    python start.py
```
