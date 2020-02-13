# 
PRE-Alpha stage

Click here to try in Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/henryiii/histogram-tutorial/master?urlpath=lab/tree/1_1D_histograms.ipynb)

## Short description

This tutorial is an introduction to boost-histogram, a library providing a
powerful histogram-as-an-object concept. It is aimed at scientists and data
analyst who use histograms in their analysis. Some familiarity with numpy and
at least passing knowledge of numpy's histogram functions is expected. Some
familiarity with matplotlib is also useful, but not required.

We will work though a series of notebooks and will build up the idea of a
histogram as an object instead of a collection of arrays. We will then solve
several realistic problems.

---

### Environment setup (10 minutes)

Before starting, a link to a GitHub repository will be provided, containing at
least an `environment.yaml` file that can be used to quickly set up a
reproducible environment using conda.

### 1. 1D histograms (50 minutes)

This will introduce the concept of a histogram. It will start by computing a
standard histogram with Numpy, then move to the drop-in replacement in
boost-histogram, noting the speed difference. Then, we will move to returning
an object, but then converting it to a Numpy style output, and will slowly
iterate until we arrive at the full histogram object start to finish. The
lesson will fill in the basic concepts of a histogram, such as axis properties
and slicing, and then participants will get to try converting a piece of code
from Numpy to histogram objects.

### 2. ND histograms (40 minutes)

This will cover multidimensional histograms. While they have the same API,
there several new concepts for attendees to learn, such as plotting in 2D,
projection and categorical selection (used in lesson 5), and dictionary
indexing.

### 3. Special histogram storages (30 minutes)

This will cover the non-default storages. After a quick mention of selecting
other simple storages (double, int, atomic int, unlimited), we will focus on
the four accumulator based storages (weighted, weighted sum, mean, weighted
mean) and how to manipulate the Numpy record views returned from these storages
efficiently. This will use accumulators directly as well, to illustrate how
they work without the extra complications of manipulating views.

### 4. Special histogram axes (30 minutes)

This will delve into the axis options (under/overflow, growth, circular)
as well as look at the four main categories of axes. Custom transform creation
will be explored, using Numba to produce a c callback with `@cfunc` that can be
used to provide regular spaced binning transforms with virtually no performance
loss over purely compiled code.

### 5. Analysis example: selections as categories (25 minutes)

This will cover a realistic example of an analysis, where a collection of
different selections are required. Selections (such as data quality criteria)
can be converted into categorical or integer axes, and then included in a
single histogram; this allows traditionally large collections of histograms to
be combined into a single object, and also makes it easier to add new control
checks, so that selections can be made when histogramming that can later be
removed.

### 6. Analysis example: TBD (25 minutes)

### 7. Advanced: xarray histograms (30 minutes)

Boost-histogram is meant to be a core library that the other 1-2 dozen
histogramming libraries currently available can use as a backend to simplify
their code and increase their performance.  One example of this will be
attempted with `xhistogram`, a package that combines histograms and `xarray`
objects. Using boost-histogram's powerful axis metadata and other features, we
will replicate a significant portion of xhistogram with just a few lines of
code.


# Setup instructions


## Install

Install miniconda on your platform. Either follow the instructions here:
<https://conda.io/docs/install/quick.html>, or if one of the following applies
to you, use that:

* On macOS, using brew: `brew cask install miniconda`
* On Windows, using chololaty: `choco install miniconda3`

## Get dependencies

Download the github repository (note: During the workshop, you can skip the branch selection.
It is there if you clone after the workshop and want identical contents).

```bash
git clone https://github.com/henryiii/histogram-tutorial --branch scipy2020
```

Change directory and create the `scipy-2020-hist` environment from `environment.yaml`:

```bash
cd histogram-tutorial
conda env create
```

Activate your environment (if you already use Conda, the environment does
install a IPython kernel, so you can just use your existing favorite Juptyer
lab environment to run and then select the `scipy-2020-hist` kernel).

```bash
conda activate scipy-2020-hist
```

Start up a JuptyerLab instance:

```bash
jupyter lab
```
