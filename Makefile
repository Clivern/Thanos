PYTHON ?= python3
PIP ?= $(PYTHON) -m pip
TERMGRAPH ?= termgraph


test:
	$(PIP) install termgraph
	$(PYTHON) data_structures.py
	$(PYTHON) algorithms.py
	$(PYTHON) problems.py
	$(PYTHON) visualize_time_complexity.py
	echo "Visualize Constant Time Complexity — O(1)"
	$(TERMGRAPH) visualize_constant_time_complexity.dat
	echo "Visualize Logarithmic Time Complexity — O(log n)"
	$(TERMGRAPH) visualize_logarithmic_time_complexity.dat
	echo "Visualize Linear Time Complexity — O(n)"
	$(TERMGRAPH) visualize_linear_time_complexity.dat
	echo "Visualize Quadratic Time Complexity — O(n^2)"
	$(TERMGRAPH) visualize_quadratic_time_complexity.dat
	echo "Visualize Linear Time Complexity — O(n + m)"
	$(TERMGRAPH) visualize_linear2_time_complexity.dat
