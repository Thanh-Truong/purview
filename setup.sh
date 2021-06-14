# /bin/bash
git clone git@github.com:Thanh-Truong/purview.git
# Install env
python3 -m venv env
source env/bin/activate
# Install packages
export TRUSTED_SITES="--trusted-host pypi.org --trusted-host files.pythonhosted.org"
pip install pyapacheatlas ${TRUSTED_SITES}
pip install pylint ${TRUSTED_SITES}
pip install azure-mgmt-resource ${TRUSTED_SITES}
pip install azure-mgmt-purview ${TRUSTED_SITES}
pip install azure-identity ${TRUSTED_SITES}