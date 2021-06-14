# /bin/bash
git clone git@github.com:Thanh-Truong/purview.git
# Install env
python3 -m venv env
source env/bin/activate
# Install packages
export TRUSTED_SITES="--trusted-host pypi.org --trusted-host files.pythonhosted.org"
pip install --upgrade pip ${TRUSTED_SITES}
pip install pyapacheatlas==0.6.0 ${TRUSTED_SITES}
pip install pylint ${TRUSTED_SITES}
pip install azure-identity==1.6.0 ${TRUSTED_SITES}
pip install azure-mgmt-resource==18.0.0 ${TRUSTED_SITES}
pip install azure-mgmt-purview==1.0.0b1 ${TRUSTED_SITES}