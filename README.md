# CMIV AI Course

Artificial intelligence and machine learning is becoming more and more prevalent in our everyday lives. In certain contexts, the introduction of AI/ML is predicted to significantly impact the way certain professions practice. Because of this, it is important that these professions, for example healthcare professionals such as radiologists and pathologists, are knowledgeable about AI/ML. 

To ensure this, [CMIV](https://liu.se/en/research/center-for-medical-image-science-and-visualization-cmiv), [Sectra](http://www.sectra.com/medical/) and [AIDA](https://medtech4health.se/aida/) decided to provide an introductory AI/ML course targeting radiologists and pathologists. This repository contains the Jupyter Notebooks used for exercises during the course.

The notebooks are targeted towards users with little or no prior experience from data science in general and machine learning especially. The notebooks are meant to serve as an introduction to the field of machine learning, covering aspects such as:

* Supervised and unsupervised learning
* Classification and regression
* Neural networks
* Deep learning

The contained notebooks are to a large extent based upon the following tutorials:

* ``Scikit-Learn`` - [SciPy 2018 Scikit-learn Tutorial](https://github.com/amueller/scipy-2018-sklearn)
* ``Deep Learning`` - [MachineLearningForMedicalImages](https://github.com/slowvak/MachineLearningForMedicalImages)

## Running with Colab
You can run all notebooks directly from the Github repo by clicking the links below:
* [01 - Introduction to Jupyter Notebooks and Data Science](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/01%20-%20Introduction%20to%20Jupyter%20Notebooks%20and%20Data%20Science.ipynb)
* [02 - Supervised learning - Part 1](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/02%20-%20Supervised%20learning%20-%20Part%201.ipynb)
* [03 - Supervised Learning - Part 2a](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/03%20-%20Supervised%20Learning%20-%20Part%202a.ipynb)
* [03 - Supervised Learning - Part 2b (optional)](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/03%20-%20Supervised%20Learning%20-%20Part%202b%20(optional).ipynb)
* [04 - Unsupervised Learning](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/04%20-%20Unsupervised%20Learning.ipynb)
* [05 - Practical Aspects of Machine Learning](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/05%20-%20Practical%20Aspects%20of%20Machine%20Learning.ipynb)
* [06 - Artificial Neural Networks](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/06%20-%20Artificial%20Neural%20Networks.ipynb)
* [07 - Deep Learning and Medical Imaging - Radiology](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/07%20-%20Deep%20Learning%20and%20Medical%20Imaging%20-%20Radiology.ipynb)
* [08 - Deep Learning and Medical Imaging - Digital Pathology](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/08%20-%20Deep%20Learning%20and%20Medical%20Imaging%20-%20Digital%20Pathology.ipynb)
* [09 - Heart failure prediction](https://colab.research.google.com/github/fordanic/cmiv-ai-course/blob/master/notebooks/heart_failure_lab.ipynb)

Note that this requires a Google account to sign in to Google Colaboratory.

Note that these notebooks were originally written for a Jupyter Notebook environment. We have madae some adjustments to allow them to be run in Google Colab, however, Google Colab uses a fork of Jupyter Notebooks and as such there will be some discrepancies between the content of the notebooks and the runtime environment in Google Colab.

Remember to change change runtime environment to GPU for the deep learning parts.

## Local Installation
Use a browser to access [Anaconda](https://www.anaconda.com/download/) and from there choose to download and install Anaconda. Please select the right Anaconda version as suitable for your platform (Windows, Linux or macOS) and use the Python 3.6 version (not Python 2.7). Anaconda is a so called package manager for Python.

Once downloaded and installed, open a command prompt (cmd, bash or similar), navigate to the location of this file. Next to this file, there should also be a file titled ``environment.yml``. With the help of this file we will create an environment with the needed packages to run the notebooks. In the command prompt, run the following command:

* ``conda env create -f environment.yml``

Say yes if prompted to download any specific Python packages.

### Running the notebooks
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
