# Fuit & Vegies Polish Market analysis

### Data Sources

Agricultural goods prices: https://ec.europa.eu/eurostat/data/database?p_p_id=NavTreeportletprod_WAR_NavTreeportletprod_INSTANCE_nPqeVbPXRmWQ&p_p_lifecycle=0&p_p_state=pop_up&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=1&p_p_col_count=2&_NavTreeportletprod_WAR_NavTreeportletprod_INSTANCE_nPqeVbPXRmWQ_nodeInfoService=true&nodeId=84303

http://ec.europa.eu/eurostat/wdds/rest/data/v2.1/json/en/aact_eaa01?itm_newa=01000&itm_newa=02400&itm_newa=02920&itm_newa=04100&itm_newa=05000&itm_newa=06100&itm_newa=06110&precision=1&indic_ag=PROD_BP&indic_ag=PROD_PP&geo=PL&unit=MIO_EUR

Dane metereologiczne: https://danepubliczne.imgw.pl

### Dependencies and Libraries

#### Machine Learning

* **pandas** - data analysis and manipulation tool, docs: https://pandas.pydata.org/docs/
* **NumPy** - library for adding support for large, multi-dimensional arrays and matrices, docs: https://numpy.org/devdocs/
* **Matplotlib** - library for creating static, animated, and interactive visualizations, docs: https://matplotlib.org/contents.html
* **sckit-learn** - library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities, docs: https://scikit-learn.org/stable/

#### Other

* **requests** - HTTP library, docs: https://requests.readthedocs.io/en/master/
* **pytest** - framework to run tests, docs: https://docs.pytest.org/en/latest/contents.html

### How it was set up?

The project is based on `pipenv`, therefore I've followed steps [from the official documentation](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

First virtualenv and `Pipfile` were created:
```console
$ pipenv --python 3
Creating a virtualenv for this project…
Pipfile: ...\workspace\fruit-veg-pl-market\Pipfile
Using .../Python38/python.exe (3.8.1) to create virtualenv…
[=   ] Creating virtual environment...created virtual environment CPython3.8.1.final.0-64 in 928ms

  creator CPython3Windows(dest=C:\Users\...\.virtualenvs\fruit-veg-pl-market-i4sdn0a1, clear=False, global=False)

  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=C:\Users\...\AppData\Local\Temp\tmp8suw_2l3\seed-app-data\v1)

  activators BashActivator,BatchActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```

Then `pandas`, `numpy`, `matplotlib`,  `sklearn` & `jupyter` librarires were installed:

```console
$ pipenv install pandas
$ pipenv install numpy
$ pipenv install matplotlib
$ pipenv install sklearn
$ pipenv install jupyter
Installing jupyter…
Adding jupyter to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock (c38359) out of date, updating to (19942d)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (c38359)!
Installing dependencies from Pipfile.lock (c38359)…
  ================================ 57/57 - 00:00:09
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

Next, other librarires were also installed:

```console
$ pipenv install requests
$ pipenv install pytest --dev
$ pipenv install pytest-cov --dev
```

## References

* [How to use Pipenv with Jupyter and VSCode](https://towardsdatascience.com/how-to-use-pipenv-with-jupyter-and-vscode-ae0e970df486)

* [How to download files using Python](https://towardsdatascience.com/how-to-download-files-using-python-ffbca63beb5c)