spec-as-code
============

Technical Writing 4coders with Sphinx + VS-code


The content (head of branch develop) of this repository serves as a starting point for technical writings as code.

It offers following features:

:FEAT_01: 
   Bla blub bla.

:FEAT_02:
   Bla blub bla.


Usage
-----

Assuming being in a `git-bash` on a Windows10 (or higher) box you do the following:

Initializing:

.. code-block:: bash

    $ git clone https://github.com/basejumpa/spec-as-code.git                          # Clone the repository
    $ rm -rf spec-as-code/.git                                                         # Strip down to working copy 
    $ mv spec-as-code my-subject                                                       # Baptize own project
    $ cd my-subject                                                                    # Enter root dir
    $ git init .                                                                       # Initialize new git repository
    $ git add .                                                                        # Create first commit (1/2)
    $ git commit -m "Use template from https://github.com/basejumpa/spec-as-code.git"  # Create first commit (2/2)
    $ scoop import scoopfile.json                                                      # Install tools
    $ pipenv install                                                                   # Install python packages
    
In case you're luckily sitting in front of a Mac replace the line starting with :code:`scoop` by :code:`brew bundle install` .

Having trouble with either `scoop <https://scoop.sh>`_ or `brew <https://brew.sh>`_ command? Then you don`t have the de-facto-standard package managers installed. You fix it by executing the following line:

* Windows: :code:`Set-ExecutionPolicy RemoteSigned -Scope CurrentUser ; irm get.scoop.sh | iex` 

* Mac: :code:`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Work loop:

.. code-block:: bash
    $ code .                                                                           # Open Visual Studio Code (VScode)

Use the internal terminal of VScode and proceed:

.. code-block:: bash

    $ pipenv shell                                                                     # Use the pipenv python environment defined by Pipfile
    $ sphinx-autobuild . build/html                                                    # Make sphinx watching for changes and rebuild automatically
    $ chrome http://127.0.0.1:8000                                                     # Open Chrome and watch the output


Attributions
============

* Attribution 1
* Attribution 2


