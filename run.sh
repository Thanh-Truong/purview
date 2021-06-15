# /bin/bash
source env/bin/activate
python purview.py --create-purview
python purview.py --assign-roles
# Creation
python purview.py --import-term-templates term_templates.json
python purview.py --import-terms terms_system_templates.csv
python purview.py --import-terms terms.csv

# Deletion
python purview.py --delete-all-terms
python purview.py --delete-term-templates term_templates.json
python purview.py --delete-purview