"""Console script for vcfxplr."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence, cast

import vobject
from bubop import logger, valid_file  # type: ignore

SeqOfVobj = Sequence[vobject.base.Component]


def pretty_print(vobjects: SeqOfVobj):
    for c in vobjects:
        c.prettyPrint()
        print("")

    logger.info(f"total: {len(vobjects)}")


def to_json(vobjects: SeqOfVobj, group_by: str) -> Mapping:
    d: Dict[str, Any] = {}
    for c in vobjects:
        try:
            key = c.contents.pop(group_by)[0].value  # type: ignore
        except KeyError:
            logger.warning(f"vCard {c} doesn't have grouping key {group_by}, skipping it...")
            continue

        curr = {}
        for k, v in c.contents.items():
            li = []
            for value in v:
                value_ = cast(vobject.base.ContentLine, value)
                if isinstance(value_.value, str):
                    val = value_.value
                else:
                    val = str(value_.value)

                val = val.strip()
                if value_.params:
                    item = {"value": val, "params": value_.params}
                else:
                    item = {"value": val}

                li.append(item)
            curr[k] = li

        if not isinstance(key, str):
            key = str(key)
        key = key.strip()

        d[key] = curr

    return d


def main():
    """Console script for vcfxplr."""
    # CLI parsing and validation --------------------------------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--vcf", type=valid_file, help="Path to the VCF cards file", required=True
    )

    subparsers = parser.add_subparsers(help="Format to export the VCF data", dest="subcommand")
    subparsers.required = True
    subparsers.add_parser("pretty", help="Pretty-print to console")
    json_parser = subparsers.add_parser("json", help="Export to JSON")
    json_parser.add_argument(
        "-g",
        "--group-by",
        default="fn",
        help=(
            "Key to group by in the JSON output - skip writing any vCards that don't have"
            " this key. By default uses the fn property (Full Name)"
        ),
    )

    args = vars(parser.parse_args())

    vcf: Path = args["vcf"]

    # Parse VCF file --------------------------------------------------------------------------
    logger.info(f"Parsing VCF file -> {vcf}")
    conts = vcf.read_text()
    try:
        vobjects: Sequence[vobject.base.Component] = list(vobject.readComponents(conts))  # type: ignore
    except Exception as e:
        raise RuntimeError(f"Can't parse the VCF file -> {vcf}") from e

    cmd = args["subcommand"]
    if cmd == "json":
        d = to_json(vobjects, group_by=args["group_by"])
        json.dump(d, fp=sys.stdout, indent=2, ensure_ascii=False)
    elif cmd == "pretty":
        pretty_print(vobjects)
    else:
        raise NotImplementedError(f"Unhandled subcommand - {cmd}")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
