source /home/users1/zhangto/shared_space/computational_annotators/durel_system_annotators_tuo/random-annotator-venv/bin/activate
ipython kernel install --user --name=random-annotator-venv
jupyter nbconvert --to script stats.ipynb
ipython stats.py 
deactivate