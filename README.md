# YFLOG: A Simple Wrapped Logger Used in Python 

A Simple Wrapped Logger Used in Python 

## Installation

```bash
# Install via pip
pip install yflog
```


## Usage

Here is a simple example for the logger.

```python
from yflog import Logger
# replace the 'X' with your token
logger = Logger(filename='my.log',file_level='info')
logger.debug('test')
logger.info('test')
logger.warning('test')
logger.error('test')

```

