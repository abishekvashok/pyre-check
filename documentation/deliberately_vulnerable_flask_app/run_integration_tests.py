# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import logging
from pathlib import Path

from integration_test_utils import run_pysa_analysis, LOG


def main() -> None:
    """
    Entry point function which checks if full_result.json is there, calls
    functions from integration_test_utils to run pysa, parse
    full_result.json, and compare the output.
    """
    if not os.path.isfile("./full_result.json"):
        raise FileNotFoundError(
            "./full_result.json file containing expected issues is not found"
        )

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    current_directory = Path(__file__).parent.absolute()

    os.chdir(str(current_directory))
    LOG.info("Running in `%s`", os.getcwd())
    run_pysa_analysis(
        current_directory,
        passthrough_args="",
        skip_model_verification=True,
        filter_issues=False,
    )
    LOG.info("Run produced expected results")


if __name__ == "__main__":
    main()
