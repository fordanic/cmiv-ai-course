# ML tutorials

Machine learning is becoming a technology that is more and more prevalent in our everyday lives. In certain contexts, the introduction of machine learning is predicted to significantly impact the way certain professions practice. Because of this, it is important that these professions, e.g. radiologists and pathologists, are knowledgeable about machine learning. 

To ensure this, [CMIV](https://liu.se/en/research/center-for-medical-image-science-and-visualization-cmiv), [Sectra](http://www.sectra.com/medical/) and [Visual Sweden](http://www.visualsweden.se/) decided to provide an introductory machine learning course for radiologists and pathologists. This repository contains the Jupyter Notebooks used for exercises during the course.

The notebooks are targeted towards users with little or no prior experience from data science in general and machine learning especially. The notebooks are meant to serve as an introduction to the field of machine learning, covering aspects such as:

* Supervised and unsupervised learning
* Classification and regression
* Neural networks
* Deep learning

The contained notebooks are to a large extent based upon the following tutorials:

* ``Scikit-Learn`` - [SciPy 2017 Scikit-learn Tutorial](https://github.com/amueller/scipy-2017-sklearn)
* ``Deep Learning`` - [MachineLearningForMedicalImages](https://github.com/slowvak/MachineLearningForMedicalImages)

## Installation
Use a browser to access [Anaconda](https://www.anaconda.com/download/) and from there choose to download and install Anaconda. Please select the right Anaconda version as suitable for your platform (Windows, Linux or macOS) and use the Python 3.6 version (not Python 2.7). Anaconda is a so called package manager for Python.

Once downloaded and installed, open a command prompt (cmd, bash or similar), navigate to the location of this file. Next to this file, there should also be a file titled ``environment.yml``. With the help of this file we will create an environment with the needed packages to run the notebooks. In the command prompt, run the following command:

* ``conda env create -f environment.yml``

Say yes if prompted to download any specific Python packages.

## Running the notebooks
Open a command prompt (cmd, bash or similar), navigate to the location of this file.

To activate the created Python environment, run the following command:

* ``activate mltutorials`` (Windows)
* ``source activate mltutorials`` (macOS and Linux)

To ensure that some widgets that are used in the notebooks work, run the following command:

* ``jupyter nbextension enable --py --sys-prefix widgetsnbextension``

This command only needs to be executed the first time.

To start the Jupyter notebooks, run the following command:

* ``jupyter notebook``

This should automatically launch a browser and start up the notebooks.

Note that running the deep learning notebook on your CPU without a GPU can take considerable time. 
