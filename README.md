# Histograms as Objects
PRE-Alpha stage

Click here to try in Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/henryiii/histogram-tutorial/master?urlpath=lab/tree/1_1D_histograms.ipynb)

## Abstract


This is an introduction to histogramming using the Scikit-HEP family of histogram tools, built on the powerful histogram-as-an-object concept. Attendees will learn how to replace a tedious manual histogram workflow with a simple, elegant one based on the histogram object. For example, allowing a histogram to be filled multiple times removes the need to manually combine NumPy arrays, and opens up new workflows where the fills happen in the most natural place in a data ingestion pipeline. Supporting easy rebinning  allows filling to happen at a higher resolution than the final histogram, allowing multiple resolutions to be tested with a single fill. Projections allow the final histogram to be made from one with more dimensions; combined with numerical, categorical, and boolean axes, this allows large numbers of histograms to be combined into one histogram, with one fill, and then projected out to from there to the final result. These are generalized histograms, as well, so you can track means as well, not just sums.

We will cover some places that (generalized) histograms are the most natural solution to problems, such as imaging and data aggregation. An example of this is with GitHub repository interactions; where users will query stats on GitHub, and will build a histogram that uses string categorical axes. Then they will plot interactions based on cross-terms in the histogram axes. Another example will show manipulating image data with the slicing syntax with natural data coordinates. Applying reductions to a selected subset will make it easy to compute statistics over a visible portion of an image. We'll also look at a more general analysis example, extracting information from multiple axes instead of using if statements in code.

We will also investigate how static typing improves interaction between histogramming libraries. Attendees will implement a basic plotting function that passes a MyPy check using the `uhi` (Universal Histogram Interface) library, plotting any PlottableProtocol histogram (such as boost-histogram/hist, uproot, and possibly Physt at some point). They are expected to learn about how Protocols work and how they can formalize interactions between libraries.


## Short description

This is an introduction to histogramming using the Scikit-HEP family of histogram tools, built on the powerful histogram-as-an-object concept. You will learn how to replace a tedious manual histogram workflow. You will also see places that (generalized) histograms are the most natural solution to problems, such as imaging and big data aggregation. Histogram axes can be used for categorical or boolean selections, often removing loops from your code and giving you more flexibility at the end to answer a wider variety of information without rerunning loops. We'll also investigate how static typing improves interaction between histogramming libraries.


Some familiarity with NumPy and at least passing knowledge of NumPy's histogram functions is expected. Some familiarity with Matplotlib is also useful, but not required. We will be making parallels to Pandas fairly often, so Pandas knowledge is also useful, but not required.

We will start each hour with a notebook lecture, and then we will then solve an interesting problem in smaller groups. For the final problem, we will look at implementing a plotting function consuming a PlottableProtocol using MyPy, so that you can build your own compatible and plotting functions.

---

## Tutorial Outline

### Environment setup (10 minutes)

Before starting, a link to a GitHub repository will be provided, containing at least an `environment.yaml` file that can be used to quickly set up a reproducible environment using Conda.

### 1. 1D histograms (30 minute lecture, 20 minute exercise)

This will introduce the concept of a histogram. It will start by computing a standard histogram with NumPy, then move to the drop-in replacement using Hist, a library backed by the powerful boost-histogram, noting the speed difference.  Then, we will move to returning an object, but then converting it to a NumPy style output, and will eventually arrive at the full histogram object start to finish. The lesson will fill in the basic concepts of a histogram, such as axis properties and slicing, and then participants will get to try converting a piece of code from NumPy to histogram objects.

#### 1.a Exercise: data investigation

### 2. ND histograms (20 minute lecture, 20 + 20 minute exercises)

This will cover multidimensional histograms. While they have the same API, there several new concepts for attendees to learn, such as plotting in 2D, projection and categorical selection, and dictionary indexing. A few of the special axes 

#### 2.a Exercise: Images as histograms

#### 2.b Exercise: Computing GitHub repository interactions via histograms

### 3. Special histogram storages and axes (30 minute lecture, 30 minute exercise)

This will cover the non-default storages. We will focus on the accumulator based storages (weighted, mean, weighted mean) and how to manipulate the Numpy record views returned from these storages efficiently. This will use accumulators directly as well, to illustrate how they work without the extra complications of manipulating views.

This will delve into the different axis options (under/overflow, growth, circular) and the four main categories of axes. Custom transform creation will be explored, using Numba to produce a c callback with `@cfunc` that can be used to provide regular spaced binning transforms with virtually no performance loss over purely compiled code. String based categorical axes will get extra detail.

#### 3.a Exercise: selections as categories

This will cover a realistic example of an analysis, where a collection of different selections are required. Selections (such as data quality criteria) can be converted into categorical or integer axes, and then included in a single histogram; this allows traditionally large collections of histograms to be combined into a single object, and also makes it easier to add new control checks, so that selections can be made when histogramming that can later be removed.

### 4 Building a PlottableProtocol function with MyPy (40 mins lecture, 20 mins exercise)

This will look into implementing a PlottableProtocol function that accepts any histogram object that conforms to the PlottableProtocol specification from UHI.



#### Removed/optional example: xarray histograms

Boost-histogram is meant to be a core library that the other 1-2 dozen histogramming libraries currently available can use as a backend to simplify their code and increase their performance.  One example of this will be attempted with `xhistogram`, a package that combines histograms and `xarray` objects. Using boost-histogram's powerful axis metadata and other features, we will replicate a significant portion of xhistogram with just a few lines of code.


# Setup instructions


## Install

Install miniconda on your platform. Either follow the instructions here:
<https://conda.io/docs/install/quick.html>, or if one of the following applies
to you, use that:

* On macOS, using brew: `brew cask install miniconda`
* On Windows, using chocolaty: `choco install miniconda3`

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


---

## Tutorial Prerequisites

* NumPy (required)
* Matplotlib (recommended)
* Pandas (optional)
* MyPy (for final exercise; will be covered in material)

---

## About the author

Henry Schreiner is a Research Software Engineer and Computational Physicist in High Energy Physics at Princeton University. He specializes in the interface between high-performance compiled codes and interactive computation in Python, in software distribution, and in interface design. He has previously worked on computational cosmic-ray tomography for archaeology and high performance GPU model fitting. He is currently a member of the IRIS-HEP project, developing tools for the next era of the Large Hadron Collider (LHC). He is an admin for Scikit-HEP, and as a maintainer for pybind11, cibuildwheel, pypa/build, and plumbum.

* Author's blog: http://iscinumpy.gitlab.io
* About the author: https://iscinumpy.gitlab.io/page/about/
* Past presentations: http://iscinumpy.gitlab.io/page/presentations/ (most presentations this last year have been minicourses, see main blog page for links)
* Most recent mini-course: Level Up Your Python, https://henryiii.github.io/level-up-your-python

