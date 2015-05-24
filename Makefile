PACKAGE=django_factory_boy

# Use current python binary instead of system default.
COVERAGE = python $(shell which coverage)

# Dependencies
DJANGO ?= 1.8
NEXT_DJANGO = $(shell python -c "v='$(DJANGO)'; parts=v.split('.'); parts[-1]=str(int(parts[-1])+1); print('.'.join(parts))")

REQ_FILE = auto_dev_requirements_django$(DJANGO).txt

all: default


default:


install-deps: $(REQ_FILE)
	pip install --upgrade pip setuptools
	pip install --upgrade -r $<
	pip freeze

$(REQ_FILE): dev_requirements.txt requirements.txt
	grep --no-filename "^[^#-]" $^ | egrep -v "^Django" > $@
	echo "Django>=$(DJANGO),<$(NEXT_DJANGO)" >> $@


clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -path '*/__pycache__/*' -delete
	find . -type d -empty -delete
	@rm -f auto_dev_requirements_*


test: install-deps
	python -W default setup.py test

pylint:
	pylint --rcfile=.pylintrc --report=no $(PACKAGE)/

coverage: install-deps
	$(COVERAGE) erase
	$(COVERAGE) run "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py" --branch setup.py test
	$(COVERAGE) report "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py"
	$(COVERAGE) html "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py"


.PHONY: all default clean coverage install-deps pylint test
