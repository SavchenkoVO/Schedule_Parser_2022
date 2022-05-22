from lib import schedule_parser
import numpy as np

class TestLineParsersUnit:
    """
    Pytest requires names of class to start with 'Test...'
    Info about keywords and asterisk (*) could be found by the link: http://www.ipt.ntnu.no/~kleppe/TPG4150/EclipseReferenceManual.pdf
    """
    def test_parse_keyword_DATE_line(self):
        input = "01 JUN 2018 /"
        output = "01 JUN 2018"
        assert schedule_parser.parse_keyword_DATE_line(input) == output

    def test_parse_keyword_COMPDAT_line(self):
        input = "'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"
        output = ["'W1'", np.nan, '10', '10', '1', '3', 'OPEN', '1*', '1',
                  '2', '1', '3*', '1.0']
        print(input, "\n---\n", output, "\n---\n", schedule_parser.parse_keyword_COMPDAT_line(input))
        assert schedule_parser.parse_keyword_COMPDAT_line(input) == output

    def test_parse_keyword_COMPDATL_line(self):
        input = "'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /"
        output = ["'W3'", "'LGR1'", '10', '10', '2', '2', 'OPEN', '1*', '1',
                  '2', '1', '3*', '1.0918']
        print(input, "\n---\n", output, "\n---\n", schedule_parser.parse_keyword_COMPDATL_line(input))
        assert schedule_parser.parse_keyword_COMPDATL_line(input) == output

