PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
TERMGRAPH ?= termgraph


test:
	$(PIP) install termgraph
	$(PYTHON) data_structures.py
	$(PYTHON) algorithms.py
	$(PYTHON) problems.py
	$(PYTHON) visualize_time_complexity.py
	$(TERMGRAPH) visualize_constant_time_complexity.dat
	$(TERMGRAPH) visualize_logarithmic_time_complexity.dat
	$(TERMGRAPH) visualize_linear_time_complexity.dat
	$(TERMGRAPH) visualize_quadratic_time_complexity.dat
	$(TERMGRAPH) visualize_linear2_time_complexity.dat
