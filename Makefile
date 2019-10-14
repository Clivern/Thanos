PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
TERMGRAPH ?= termgraph


test:
	$(PIP) install termgraph
	$(PYTHON) Python/data_structures.py
	$(PYTHON) Python/algorithms.py
	$(PYTHON) Python/problems.py
	$(PYTHON) Python/visualize_time_complexity.py
	$(TERMGRAPH) visualize_constant_time_complexity.dat
	$(TERMGRAPH) visualize_logarithmic_time_complexity.dat
	$(TERMGRAPH) visualize_linear_time_complexity.dat
	$(TERMGRAPH) visualize_quadratic_time_complexity.dat
	$(TERMGRAPH) visualize_linear2_time_complexity.dat
