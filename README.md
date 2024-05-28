# roq-python-samples

Samples demonstrating how to implement various features of algorithmic trading
solutions.


## Operating Systems

* Linux (x86-64, AArch64)
* macOS (x86-64, Arm64)


## Library/Package Dependencies

* [fastcore](https://github.com/fastai/fastcore) (Apache 2.0 License)


## Prerequisites

Install Roq's Python bindings

```bash
conda install -y --channel https://roq-trading.com/conda/stable roq-python
```

Some examples use the `@typedispatch` decorator from the [fastcore](https://github.com/fastai/fastcore) library

```bash
conda install -y fastcore
```

## Building

```bash
python setup.py clean --all && \
python -m pip install . -vvv
```

## Using

### Strategy

```bash
python -m roq_samples.strategy ~/run/deribit.sock
```


## License

The project is released under the terms of the BSD 3-Clause license.
