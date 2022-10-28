# top-fibers
Code to find and rank the top superspreaders of misinformation on Twitter using the FIB-index.

## FIB-index
The FIB-index is a simple yet effective metric for estimating a social media user's influence within a misinformation network on a given platform.
See the working paper for more details: [Matthew R. DeVerna, Rachith Aiyappa, Diogo Pacheco, John Bryden, and Filippo Menczer, 2021](https://arxiv.org/abs/2207.09524).
Should you use the FIB-index in your own work, please cite the latest version of that work.

## Data
This repository is set up to utilize data that is output by the Observatory on Social Media's (OSoMe) Decahose infrastructure.
- [Learn more about OSoMe]()
- [Learn more about Twitter's Decahose]()

Currently, the data is returned in Twitter's V1 format as this is how data is delivered by the.
You can see details on migrating from V1 and V2 [here](https://developer.twitter.com/en/docs/twitter-api/migrate/data-formats/standard-v1-1-to-v2).

## Setting up environment
This repository requires very few dependencies.
The easiest way to make sure that everything will run for you is to install that latest version of [Miniconda](https://docs.conda.io/projects/conda/en/latest/index.html) and then utilize the `conda` package manager to install one of the environment files saved inside of the `environments/` directory.

Note that both environment files are should be interchangeable.
Both are offered because they offer different levels of specificity and, as a result, have their own pros and cons.
See the [conda cheatsheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html) for help with `conda`.

Environment files: 
1. `environments/environment_cross_platform.yml` : this file is intended to be cross-platform compatible, however, it contains considerably less information when compared with the second file. While this is meant to be more compatible, it contains a little bit less information about _exactly_ which packages are being utilized.

2. `environments/environment_plt_pkg.yml` : this file contains much more information about all the versions of everything utilized in the latest working evironment.
You can set up this environment with the following command from the root directory of this repository.

```bash
conda env create -n top-fibers --file environments/ENVIRONMENT_FILE_NAME.yml
```

> Notes:
> - Replace `ENVIRONMENT_FILE_NAME.yml` with the file you prefer to install.
> - Both of the above commands will create an environment called `top-fibers`.
> - To change the name of your environment, replace `top-fibers` with whatever you prefer.

## Local package install (required)
The main script `scripts/calc_fib_indices.py` requires that you locally install the `top_fibers_pkg`.
To do this, change your current working directory to the `package/` directory inside of this repository and then run:

```bash
pip install -e .
```