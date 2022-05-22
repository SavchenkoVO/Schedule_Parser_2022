import pytest
import pandas as pd
import numpy as np
from lib import schedule_parser
from numpy import nan


class TestUnitParser:
    @pytest.fixture
    def set_up(self):
        """
        Prepares info for reference input file(s)
        @return: None
        """
        self.keywords = ("DATES", "COMPDAT", "COMPDATL")
        self.parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
                  "Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
                  "Skin factor", "D-factor", "Dir_well_penetrates_grid_block", "Press_eq_radius")

        # TODO: с названиями стоит подумать
        self.input_file_reference = "data/test_schedule_input_reference.inc"
        self.output_csv_reference = "data/schedule_output_reference.csv"

        self.clean_file = "output_data/handled_schedule.inc"
        self.output_csv = "data/schedule_output.csv"

        with open(self.clean_file, "r", encoding="utf-8") as file:
            self.clean_file_text = file.read()

        self.parse_list_output_reference = [
            [nan, "'W1'", nan, '10', '10', '1', '3', 'OPEN', '1*', '1', '2', '1', '3*', '1.0'],
            [nan, "'W2'", nan, '32', '10', '1', '3', 'OPEN', '1*', '1', '2', '1', '3*', '2.0'],
            [nan, "'W3'", nan, '5', '36', '2', '2', 'OPEN', '1*', '1', '2', '1', '3*', '3.0'],
            [nan, "'W4'", nan, '40', '30', '1', '3', 'OPEN', '1*', '1', '2', '1', '3*', '4.0'],
            [nan, "'W5'", nan, '21', '21', '4', '4', 'OPEN', '1*', '1', '2', '1', '3*', '5.0'],
            ['01 JUN 2018', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
            ['01 JUL 2018', "'W3'", nan, '32', '10', '1', '1', 'OPEN', '1*', '1', '2', '1', '3*', '1.0718'],
            ['01 JUL 2018', "'W5'", nan, '21', '21', '1', '3', 'OPEN', '1*', '1', '2', '1', '3*', '5.0'],
            ['01 AUG 2018', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
            ['01 SEP 2018', "'W1'", nan, '10', '10', '2', '3', 'OPEN', '1*', '1', '2', '1', '3*', '1.0918'],
            ['01 SEP 2018', "'W2'", nan, '32', '10', '1', '2', 'OPEN', '1*', '1', '2', '1', '3*', '2.0'],
            ['01 SEP 2018', "'W3'", "'LGR1'", '10', '10', '2', '2', 'OPEN', '1*', '1', '2', '1', '3*', '1.0918'],
            ['01 OCT 2018', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
            ['01 NOV 2018', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan],
            ['01 DEC 2018', nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan]]


    def test_parse_schedule(self, set_up):
        assert schedule_parser.parse_schedule(self.clean_file_text, keywords_tuple=self.keywords) \
               == self.parse_list_output_reference
