# IMPORTANT NOTE
1. filename of the test file must begin with "test" in lowercase (ex. test_math_util.py)
2. test class must inherit unittest.Testcase
3. test method must begin with "test" in lowercase

# precondition
```sh
pip install -r requirements.txt
```

# run test
```sh
nose2 -v
```

# run test with coverage report
```sh
nose2 -v --with-coverage --coverage-report html --coverage src
```

# nose2 -h
```sh
usage: nose2 [-s START_DIR] [-t TOP_LEVEL_DIRECTORY] [--config [CONFIG]]
             [--no-user-config] [--no-plugins] [--plugin PLUGINS]
             [--exclude-plugin EXCLUDE_PLUGINS] [--verbose] [--quiet]
             [--log-level LOG_LEVEL] [-B] [--log-capture] [-D]
             [--coverage PATH] [--coverage-report TYPE]
             [--coverage-config FILE] [-C] [-F] [-h]
             [testNames [testNames ...]]

positional arguments:
  testNames

optional arguments:
  -s START_DIR, --start-dir START_DIR
                        Directory to start discovery ('.' default)
  -t TOP_LEVEL_DIRECTORY, --top-level-directory TOP_LEVEL_DIRECTORY, --project-directory TOP_LEVEL_DIRECTORY
                        Top level directory of project (defaults to start dir)
  --config [CONFIG], -c [CONFIG]
                        Config files to load, if they exist. ('unittest.cfg'
                        and 'nose2.cfg' in start directory default)
  --no-user-config      Do not load user config files
  --no-plugins          Do not load any plugins. Warning: nose2 does not do
                        anything if no plugins are loaded
  --plugin PLUGINS      Load this plugin module.
  --exclude-plugin EXCLUDE_PLUGINS
                        Do not load this plugin module
  --verbose, -v         print test case names and statuses
  --quiet
  --log-level LOG_LEVEL
                        Set logging level for message logged to console.
  -h, --help            Show this help message and exit

plugin arguments:
  Command-line arguments added by plugins:

  -B, --output-buffer   Enable output buffer
  --log-capture         Enable log capture
  -D, --debugger        Enter pdb on test fail or error
  --coverage PATH       Measure coverage for filesystem path (multi-allowed)
  --coverage-report TYPE
                        Generate selected reports, available types: term,
                        term-missing, annotate, html, xml (multi-allowed)
  --coverage-config FILE
                        Config file for coverage, default: .coveragerc
  -C, --with-coverage   Turn on coverage reporting
  -F, --fail-fast       Stop the test run after the first error or failure
```