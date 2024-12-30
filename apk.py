from subprocess import CalledProcessError, check_call, DEVNULL
from typing import Any, List, Sequence

import dotbot


class Apk(dotbot.Plugin):
    def can_handle(self, directive: str) -> bool:
        return directive == "apk"

    def handle(self, directive: str, packages: List[str]) -> bool:
        success = self._run(["apk", "update"], "Updating apk") and self._run(
            ["apk", "add"] + packages,
            "Installing the apk packages: {}".format(", ".join(packages)),
        )

        if success:
            self._log.info("apk packages installed successfully")

        return success

    def _run(self, command: Sequence[Any], low_info: str) -> bool:
        self._log.lowinfo(low_info)
        try:
            check_call(command, stdout=DEVNULL, stderr=DEVNULL)
            return True
        except CalledProcessError as e:
            self._log.error(e)
            return False
