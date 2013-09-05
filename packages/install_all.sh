#!/bin/bash

ESTAPP="$(dirname "$(readlink -f "$0")")/.."
fi

function pip_install {
    pip install --no-index --find-links file://$ESTAPP/packages/ $1
}

function pip_egg_install {
    pip install --egg --no-index --find-links file://$ESTAPP/packages/ $1
}

function py_install {
    easy_install --always-unzip --upgrade -H $HOSTNAME --find-links $ESTAPP/packages $1
}

function deb_install {
    dpkg -l $1 || sudo apt-get install $1
}

deb_install python-dev

py_install pip
pip_egg_install virtualenv
pip_install bottle
pip_egg_install Jinja2
pip_egg_install beaker
pip_egg_install tornado