PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
TERMGRAPH ?= termgraph


test:
	$(PIP) install termgraph
	$(PYTHON) data_structures.py
	$(PYTHON) algorithms.py
	$(PYTHON) problems.py
	$(PYTHON) visualize_linear_time_complexity.py
	$(TERMGRAPH) visualize_linear_time_complexity.dat
