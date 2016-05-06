.PHONY: clean data lint requirements sync_data_to_s3 sync_data_from_s3

#################################################################################
# GLOBALS                                                                       #
#################################################################################

#BUCKET = {#{ cookiecutter.s3_bucket }#}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

requirements:
	pip3 install -r requirements.txt

data: 
	# generates data/raw/dataset.csv.gz
	python3 src/data/make_dataset.py

analysis: data/raw/dataset.csv.gz
	python3 src/analysis.py

clean:
	find . -name "*.pyc" -exec rm {} \;

lint:
	flake8 .

#sync_data_to_s3:
	#s3cmd sync --recursive data/ s3://$(BUCKET)/data/

#sync_data_from_s3:
	#s3cmd sync --recursive s3://$(BUCKET)/data/ data/

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################
