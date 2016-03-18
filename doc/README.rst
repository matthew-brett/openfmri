##############################
OpenFMRI package documentation
##############################

To build the documentation, change directory to the directory containg this
file (``doc``) and run::

    pip install -r ../doc-requirements.txt
    make html

The built docs will be in ``_build/html``.

To upload the built docs to github, run::

    make github

or (in Windows)::

    .\make.bat github
