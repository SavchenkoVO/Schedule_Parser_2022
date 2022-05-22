# -*- coding: utf-8 -*-
from lib import schedule_parser_pre
from lib import schedule_parser
from lib import schedule_parser_post


if __name__ == "__main__":
	keywords = ("DATES", "COMPDAT", "COMPDATL")
	parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
					"Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
					"Skin factor", "D-factor")
	input_file = "input_data/test_schedule.inc"
	output_csv = "output_data/schedule.csv"

	pre_schedule = schedule_parser_pre.pre_transform_schedule(path=input_file, mode='reading', enc='UTF-8')
	schedule = schedule_parser.parse_schedule(pre_schedule, keywords)
	schedule_parser_post.transform_schedule(schedule, parameters, output_csv)
	print('===Все готово!===')