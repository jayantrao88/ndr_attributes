# read version from installed package
from importlib.metadata import version
__version__ = version("ndr_attributes")

# populate package namespace
from pycounts.pycounts import count_words
from pycounts.plotting import plot_words