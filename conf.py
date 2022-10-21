import os

### meta data #################################################################

project = "My Subject"
copyright= "2022, John Doe"
release = "0.1.0"

exclude_patterns = [
    'README.rst',
    'LICENSE.rst',
]

extensions = []

### configuration #############################################################
# @see https://www.sphinx-doc.org/en/master/usage/configuration.html

numfig = True

### html config ###############################################################
html_theme = "sphinx_material"

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Hide hyper link which leeds to the source of page displayed
html_show_sourcelink = True

html_theme_options = {
    'color_primary': 'teal',
    'color_accent' : 'yellow',

    'globaltoc_depth'        : 3,
    'globaltoc_collapse'     : 'true',
    'globaltoc_includehidden': 'true',
}

### plantuml config ###########################################################
extensions.append('sphinxcontrib.plantuml')
conf_location = os.path.realpath(os.path.dirname(__file__))

plantuml = f"plantuml.cmd {conf_location} -config {conf_location}/plantuml.config"
plantuml_output_format = 'svg'

### draw.io config ############################################################
# @see https://pypi.org/project/sphinxcontrib-drawio/
extensions.append('sphinxcontrib.drawio')

### mlx traceability config ###################################################
# @see https://melexis.github.io/sphinx-traceability-extension/configuration.html
extensions.append('mlx.traceability')

import mlx.traceability

html_static_path = [os.path.join(os.path.dirname(mlx.traceability.__file__), 'assets')]

