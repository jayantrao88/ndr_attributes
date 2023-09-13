# ndr_attributes

Create Custom NDR Features

## Installation

```bash
$ pip install ndr_attributes
```

## Usage

[TODO]: #
`ndr_attributes` can be used to count words in a text file and plot results
as follows:

```python
from ndr_attributes.ndr_attributes import count_words
from ndr_attributes.plotting import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`ndr_attributes` was created by Jayant Rao. Jayant Rao retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.

## Credits

`ndr_attributes` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
