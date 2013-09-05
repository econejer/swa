#!/bin/bash
#
# Create a virtual environment with only the packages we want
#
set -e
ESTAPP="$(dirname "$(readlink -f "$0")")/"

virtualenv ENV --no-site-packages --python=python${PYVERSION:-2.7}

# Note this doesn't carry over to your shell, it is only 
# here for easy_install_all.bash below
source ENV/bin/activate

# Install downloaded packages
$ESTAPP/packages/install_all.sh

echo '####################################################'
echo ''
echo 'Don"t forget to source ENV/bin/activate'
echo ''
echo '####################################################'