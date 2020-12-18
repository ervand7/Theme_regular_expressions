import re
from h_w.work_with_file import open_file


class DefinitionsForRegExp:
    @classmethod
    def re_name_firstname_lastname(cls):
        """Here we compile heterogeneous data <name firstname lastname> to unit format
        <name,firstname,lastname>"""
        better_contacts_list = []
        for row_ in open_file():
            pattern_ = re.compile(r"\b([А-Я]\w+)\s*,*([А-Я]\w+)\s*,*([А-Я]\w+\s*)*")
            row_ = pattern_.sub(r"\1, \2, \3", str(row_))
            better_contacts_list.append(row_)
        return better_contacts_list

    @classmethod
    def re_phone_number(cls):
        """Here we compile heterogeneous data <phone number> to unit format
                <+7(999)999-99-99>"""
        better_contacts_list_2 = []
        for row__ in cls.re_name_firstname_lastname():
            pattern__ = re.compile(r"(\+7\s*|8\s*)\(*(\d{3})\)*\s*-*(\d{3})-*\s*(\d{2})-*\s*(\d{2})")
            row__ = pattern__.sub(r"+7(\2)\3-\4-\5", str(row__))
            better_contacts_list_2.append(row__)
        return better_contacts_list_2

    @classmethod
    def re_add_phone_number(cls):
        """Here we compile heterogeneous data <additional phone number> to unit format
                        <re_phone_number доб.9999>"""
        better_contacts_list_3 = []
        for row___ in cls.re_phone_number():
            pattern = re.compile(r"\(*(\b[д][о][б])\s*(\.*)\s*(\w+)\)*")
            row___ = pattern.sub(r"\1\2\3", str(row___))
            better_contacts_list_3.append(row___)
        return better_contacts_list_3

    @classmethod
    def transform_elements_from_str_to_list(cls):
        """Due to last changes every our row from list turned into str, and
        we want to reverse this process"""
        better_contacts_list_4 = []
        for i in cls.re_add_phone_number():
            i = [element.strip("'[]") for element in i.split(", ")]
            better_contacts_list_4.append(i)
        return better_contacts_list_4

    @classmethod
    def finish_list_without_duplicate(cls):
        """There initially were duplicate data in our document, and
        we want to get rid of them"""
        better_contacts_list_5 = []
        for one_row in cls.transform_elements_from_str_to_list():
            if not one_row[0][0:7] in [i[0][0:7] for i in better_contacts_list_5]:
                better_contacts_list_5.append(one_row)
        return better_contacts_list_5
