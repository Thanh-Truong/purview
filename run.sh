# /bin/bash
source env/bin/activate
python purview.py --create-purview
python purview.py --assign-roles
# Creation
# Purview displays only a default glossary named as Glossary
# Without this step, one needs to manually create a term in
# GUI
python purview.py --create-glossary "Glossary"
python purview.py --import-term-templates term_templates.json
#python purview.py --import-terms terms_system_templates.csv
python purview.py --import-terms terms.csv

# Import entities

# Create lineage between two entities

# Deletion
python purview.py --delete-all-terms
python purview.py --delete-term-templates term_templates.json
#python purview.py --delete-purview