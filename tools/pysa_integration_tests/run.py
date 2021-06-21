# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import logging
import os
from pathlib import Path

from utils import run_pysa_integration_test, LOG


def main() -> None:
    """
    Entry point function which checks if full_result.json is there, calls
    functions from integration_test_utils to run pysa, parse
    full_result.json, and compare the output.
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    vulnerable_flask_app_folder = (
        Path(__file__).resolve().parents[2]
        / "documentation"
        / "deliberately_vulnerable_flask_app"
    )

    full_result_file_path = vulnerable_flask_app_folder / "full_result.json"

    if not os.path.isfile(full_result_file_path):
        raise FileNotFoundError(
            f"{full_result_file_path} containing expected issues is not found"
        )

    LOG.info("Running in `%s`", vulnerable_flask_app_folder)
    run_pysa_integration_test(
        vulnerable_flask_app_folder,
        passthrough_args="",
        skip_model_verification=True,
        filter_issues=False,
        run_from_source=True,
    )


if __name__ == "__main__":
    main()
