# os_utilities

Small collection of cross-platform helper utilities for common OS tasks used in Python projects.

## Features

- Path helpers (normalize, join, safe create)
- File operations with error handling
- Environment variable utilities
- Simple process/command helpers

## Installation

This repository is intended to be used as a small utility package. You can copy the module into your project or install it using pip if packaged.

Basic usage (copy file into your project):

```py
from os_utilities import path_helper, env_helper

p = path_helper.safe_join('some', 'dir', 'file.txt')
print(env_helper.get('HOME', default='~'))
```

## Examples

- Create directories safely:

```py
from os_utilities import file_ops
file_ops.ensure_dir('logs/archive')
```

- Run an external command and capture output:

```py
from os_utilities import process
retcode, out, err = process.run(['echo', 'hello'])
```

## Contributing

Please open issues or pull requests. Keep changes small and include tests where appropriate.

## License

MIT License — see LICENSE file if present.
