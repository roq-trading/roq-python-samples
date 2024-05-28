# roq-python-samples

Example projects demonstrating how to use Roq's Python bindings.


## Operating Systems

* Linux (x86-64, AArch64)
* macOS (Arm64, x86-64)


## Library/Package Dependencies

* [fastcore](https://github.com/fastai/fastcore) (Apache 2.0 License)


## Installing

If you just want to install the project.

### Stable Channel

```bash
conda install -y --channel https://roq-trading.com/conda/stable roq-python-samples
```

### Unstable Channel

```bash
conda install -y --channel https://roq-trading.com/conda/unstable roq-python-samples
```


## Prerequisites

If you want to build from source.

Install Roq's Python bindings

### Stable Channel

```bash
conda install -y --channel https://roq-trading.com/conda/stable roq-python
```

### Unstable Channel

```bash
conda install -y --channel https://roq-trading.com/conda/unstable roq-python
```

### Third-party

Some examples use the `@typedispatch` decorator from the [fastcore](https://github.com/fastai/fastcore) library

```bash
conda install -y fastcore
```

## Building

If you want to build from source.

```bash
python setup.py clean --all && python -m pip install . -vvv
```


## Using

### Strategy

Demonstrates how to set up a gateway client

* Implements the callback handlers
* Sends requests using the dispatcher interface

```bash
python -m roq_samples.strategy ~/run/deribit.sock
```

### FIX Session

Demonstrates how to set up a FIX client session

```bash
python -m roq_samples.fix_session \
    --sender_comp_id xxx \
    --target_comp_id yyy \
    --username foo \
    --password bar \
    --network_address $HOME/run/fix-bridge.sock
```

### SBE Receiver

Demonstrates how to maintain market data from SBE incremental / snapshot multicast feeds

```bash
python -m roq_samples.sbe_receiver \
    --local_interface 192.168.188.66 \
    --multicast_snapshot_address 225.0.0.1 \
    --multicast_snapshot_port 1234 \
    --multicast_incremental_address 225.0.0.1 \
    --multicast_incremental_port 2345
```


## License

The project is released under the terms of the BSD 3-Clause license.


## Links

* [Roq GmbH](https://roq-trading.com/)
* [Documentation](https://roq-trading.com/docs/)
* [Contact us](mailto:info@roq-trading.com)
