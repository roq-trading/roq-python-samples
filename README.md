# roq-python-samples

Example projects demonstrating how to use Roq's Python bindings.


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
python setup.py clean --all && python -m pip install . -vvv
```

## Using

### Strategy

```bash
python -m roq_samples.strategy ~/run/deribit.sock
```

### FIX Session

```bash
python -m roq_samples.fix_session \
    --sender_comp_id xxx \
    --target_comp_id yyy \
    --username foo \
    --password bar \
    --network_address $HOME/run/fix-bridge.sock
```

### SBE Receiver

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
