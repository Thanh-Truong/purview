# /bin/bash
source env/bin/activate
python purview.py --create-purview
python purview.py --assign-roles
python purview.py --import-term-templates term_templates.json
python purview.py --import-terms terms_system_templates.csv
# Terms based on custom templates
python purview.py --import-terms terms.csv
python purview.py --delete-purview