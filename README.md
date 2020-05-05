# Fuit & Vegies Polish Market analysis

### Data Sources

Ceny skupowe: https://dane.gov.pl/dataset/912,zintegrowany-system-rolniczej-informacji-rynkowej-biuletyny-informacyjne-rynek-owocow-i-warzyw-swiezych

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