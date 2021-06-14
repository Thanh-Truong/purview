# /bin/bash
source env/bin/activate
python purview.py --create-purview
python purview.py --assign-roles
python purview.py --import-term-templates term_templates.json
python purview.py --delete-purview