# Fuit & Vegies Polish Market analysis

### Data Sources

Ceny skupowe: https://dane.gov.pl/dataset/912,zintegrowany-system-rolniczej-informacji-rynkowej-biuletyny-informacyjne-rynek-owocow-i-warzyw-swiezych

Dane metereologiczne: https://danepubliczne.imgw.pl

### Dependencies and Libraries

* **pandas** - data analysis and manipulation tool, docs: https://pandas.pydata.org/docs/
* **NumPy** - library for adding support for large, multi-dimensional arrays and matrices, docs: https://numpy.org/devdocs/
* **Matplotlib** - library for creating static, animated, and interactive visualizations, docs: https://matplotlib.org/contents.html
* **sckit-learn** - library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities, docs: https://scikit-learn.org/stable/

### How it was set up?

The project is based on `pipenv`, therefore I've followed steps [from the official documentation](https://pipenv-fork.readthedocs.io/en/latest/basics.html).

First, to create virtualenv and `Pipfile`:
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

And then install `pandas`, `numpy`, `matplotlib` & `sklearn`:

```console
$ pipenv install pandas
$ pipenv install numpy
$ pipenv install matplotlib
$ pipenv install sklearn
Installing sklearn…
Adding sklearn to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock (19942d) out of date, updating to (0b4fd1)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (19942d)!
Installing dependencies from Pipfile.lock (19942d)…
  ================================ 13/13 - 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```