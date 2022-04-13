# vcfxplr

<a href="https://github.com/bergercookie/vcfxplr/actions" alt="CI">
<img src="https://github.com/bergercookie/vcfxplr/actions/workflows/ci.yml/badge.svg" /></a>
<a href="https://github.com/pre-commit/pre-commit">
<img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="pre-commit"></a>

<a href="https://github.com/bergercookie/vcfxplr/blob/master/LICENSE.md" alt="LICENSE">
<img src="https://img.shields.io/github/license/bergercookie/vcfxplr.svg" /></a>
<a href="https://pypi.org/project/vcfxplr/" alt="pypi">
<img src="https://img.shields.io/pypi/pyversions/vcfxplr.svg" /></a>
<a href="https://badge.fury.io/py/vcfxplr">
<img src="https://badge.fury.io/py/vcfxplr.svg" alt="PyPI version" height="18"></a>
<a href="https://pepy.tech/project/vcfxplr">
<img alt="Downloads" src="https://pepy.tech/badge/vcfxplr"></a>
<a href="https://github.com/psf/black">
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

## Description

The goal of the tool is to explore and export data from a `VCF` / `vCard` file.
It currently serves two functions:

- Reads the `VCF` file and pretty-prints it to stdout
- Reads the `VCF` file and dumps it in JSON format.

## Installation

Install it from `PyPI`:

```sh
pip3 install --user --upgrade vcfxplr
```

To get the latest version install directly from source:

```sh
pip3 install --user --upgrade git+https://github.com/bergercookie/vcfxplr
```

## Example - Usage

- Pretty-print a file: `vcfxplr -c path/to/file.vcf pretty`
- Write to JSON and dump to stdout: `vcfxplr -c path/to/file.vcf json`
- Write to JSON and dump to stdout - Use `fullname` to group the items: `vcfxplr -c path/to/file.vcf json -g uid`

## Sample Output

Sample execution for `vcfxplr -c ~/Downloads/test.vcf json`

```
2022-04-13 10:30:59.923 | INFO     | vcfxplr.scripts.main:main:87 - Parsing VCF file -> /home/berger/Downloads/test.vcf
{
  "John Doe": {
    "version": [
      {
        "value": "4.0"
      }
    ],
    "email": [
      {
        "value": "john@doe.com",
        "params": {
          "PREF": [
            "1"
          ]
        }
      },
      {
        "value": "john2@doe.com"
      }
    ],
    "n": [
      {
        "value": "John  Doe"
      }
    ],
    "tel": [
      {
        "value": "+44113712382",
        "params": {
          "TYPE": [
            "home"
          ],
          "VALUE": [
            "TEXT"
          ]
        }
      },
      {
        "value": "+44113728883",
        "params": {
          "TYPE": [
            "work"
          ],
          "VALUE": [
            "TEXT"
          ]
        }
      },
      {
        "value": "+44111238885",
        "params": {
          "TYPE": [
            "fax"
          ],
          "VALUE": [
            "TEXT"
          ]
        }
      }
    ],
    "uid": [
      {
        "value": "88cb5e2c-30e3-4b2e-b7bd-ce347a3652a7"
      }
    ]
  },
  "Ground Control": {
    "version": [
      {
        "value": "4.0"
      }
    ],
    "email": [
      {
        "value": "ground@control.com",
        "params": {
          "PREF": [
            "1"
          ]
        }
      }
    ],
    "tel": [
      {
        "value": "+1123456789",
        "params": {
          "VALUE": [
            "TEXT"
          ]
        }
      }
    ],
    "uid": [
      {
        "value": "7d50ef3d-32be-4b3c-a36b-9a083a8d67b6"
      }
    ]
  },
  "another  contact": {
    "version": [
      {
        "value": "4.0"
      }
    ],
    "nickname": [
      {
        "value": "contact@gmail.com"
      }
    ],
    "n": [
      {
        "value": "another   contact"
      }
    ],
    "tel": [
      {
        "value": "+12344566789",
        "params": {
          "VALUE": [
            "TEXT"
          ]
        }
      }
    ],
    "uid": [
      {
        "value": "bf2439a6-35cb-4d97-970d-bd31486b61e8"
      }
    ]
  },
  "one more contact": {
    "version": [
      {
        "value": "4.0"
      }
    ],
    "n": [
      {
        "value": "one  more contact"
      }
    ],
    "tel": [
      {
        "value": "+49728392882",
        "params": {
          "VALUE": [
            "TEXT"
          ]
        }
      }
    ],
    "uid": [
      {
        "value": "99b7de2c-26c7-4655-aa19-74c51a1507b0"
      }
    ]
  }
}
```
