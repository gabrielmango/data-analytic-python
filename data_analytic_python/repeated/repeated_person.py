from typing import Type

import pandas as pd

from data_analytic_python.repeated.generate import GenerateSql
from data_analytic_python.repeated.information import Info


class RepeatedPerson(GenerateSql):
    """Generates SQL script for deleting repeated person records."""

    def __init__(
        self, data: pd.DataFrame, info: Type[Info], locate: str, uuid_2: bool
    ) -> None:
        """Initialize RepeatedPerson with data, info type, location, and UUID flag."""
        self.data = data
        self.info = info
        self.locate = locate
        self.uuid_2 = uuid_2
        self.start()

    def start(self):
        """Starts the process of creating and compiling the SQL script."""
        self.create_script()
        self.compile_script()
        self.create_file(self.info.path, self.info.script)

    def create_script(self):
        """Creates the SQL script by iterating over the provided data."""
        for index, line in self.data.iterrows():
            self.info.components.append(
                self.script_delete_sql(
                    line['no_pessoa'],
                    self.locate,
                    line['co_uuid'],
                    self.uuid_2,
                )
            )

    def compile_script(self):
        """Compiles the SQL script by joining the components."""
        self.info.script = self.script_base(''.join(self.info.components))
