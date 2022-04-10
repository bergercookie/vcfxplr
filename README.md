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
- Write to JSON and dump to stdout - Use `fullname` to group the items: `vcfxplr -c path/to/file.vcf json -g fullname`
