# Unittest python
workshop about writing unittest written in python.

This project use [PDM](https://pdm.fming.dev/latest/) as package manager.

## Run test Example
for example on test_number_utils.py
```
py -m unittest -v tests/test_number_utils.py;
```
### Using nose2 run to all test

```
nose2 -v --with-coverage
```