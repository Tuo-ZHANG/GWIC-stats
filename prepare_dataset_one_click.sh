source ../OGWiC-env/bin/activate
ipython kernel install --user --name=OGWiC-env
jupyter nbconvert --to script stats.ipynb
ipython stats.py 
deactivate