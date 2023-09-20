## Duke IDS 706 Data Engineering mini project 4
---

[![cicd](https://github.com/nogibjj/Yuwen-IDS706-miniproject4/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Yuwen-IDS706-miniproject4/actions/workflows/cicd.yml)

**Summary**

The objective of Week 4 mini project was to create a GitHub Actions Matrix Build that tests more than one than one version of Python. This script has been integrated with the Python CiCd automation template: https://github.com/Candice1121/IDS706-template.

---

**Code Location**

You can find the relevant code in the following files:
- `main.py`
- `test_main.py`

---

Three functions (load_data, test_descriptive_stats, test_plot_hisogram) check the availability of Python scripts with pandas works properly.

**Modification**

1. Update main.py to integrate a data visualization function to plot histogram
2. Update workflow cicd.yml to create a matrix with three versions of python

---

**Visualization**

### Pandas Descriptive Statistics
![](/output/visualization_hist.png)

### Make Test Pass
![](/output/pass_test.png)

### Github Actions Matrix
![](/output/python_matrix.png)

---

**Run**

install code: make install

lint code: make lint

format code: make format

test code: make test

run all steps: make all

