import argparse
import papermill as pm
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()

# Découpage en étapes
sections = {
    "load": "## 1. Chargement des données",
    "explore": "## 2. Exploration",
    "preprocess": "## 3. Préprocessing",
    "model": "## 4. Modélisation"
}

# Exécution séquentielle
current_notebook = new_notebook()
for step, header in sections.items():
    try:
        # Exécute jusqu'à la section
        pm.execute_notebook(
            args.input,
            args.output,
            parameters={'stop_at': header},
            kernel_name='python3'
        )
        
        # Ajoute au notebook cumulatif
        step_nb = nbformat.read(args.output, as_version=4)
        current_notebook.cells.extend(step_nb.cells)
        current_notebook.cells.append(new_markdown_cell(f"✅ Étape {step} terminée"))
        
    except Exception as e:
        current_notebook.cells.append(new_markdown_cell(f"❌ Erreur à l'étape {step}:\n```\n{str(e)}\n```"))
        break

# Sauvegarde finale
nbformat.write(current_notebook, args.output)
