"""
------------------------------------------------------------
ECAT - Field Dictionary
Build : 1.0.9
------------------------------------------------------------
"""


class FieldDictionary:

    def __init__(self):

        self.dictionary = {

            "Consumer": [
                "Consumer",
                "Consumer No",
                "Consumer Number",
                "BP Number",
                "Account Number",
                "Consumer ID"
            ],

            "Meter": [
                "Meter",
                "Meter No",
                "Meter Number"
            ],

            "Feeder": [
                "Feeder",
                "Feeder Name",
                "Feeder Code"
            ],

            "Reader": [
                "Reader",
                "Meter Reader",
                "Reader Name",
                "MR Name"
            ],

            "Tariff": [
                "Tariff",
                "Tariff Category",
                "Category"
            ],

            "Units": [
                "Units",
                "Total Units",
                "Energy",
                "Consumption"
            ],

            "Amount": [
                "Amount",
                "Bill Amount",
                "Net Amount",
                "Revenue"
            ]
        }

    # --------------------------------------------------

    def get_standard_fields(self):

        return sorted(self.dictionary.keys())

    # --------------------------------------------------

    def aliases(self, standard_field):

        return self.dictionary.get(
            standard_field,
            []
        )

    # --------------------------------------------------

    def find_match(
        self,
        available_columns,
        standard_field
    ):
        """
        Returns matching column name
        from available columns.
        """

        aliases = self.aliases(
            standard_field
        )

        lookup = {
            c.lower(): c
            for c in available_columns
        }

        for alias in aliases:

            if alias.lower() in lookup:
                return lookup[
                    alias.lower()
                ]

        return None

    # --------------------------------------------------

    def add_alias(
        self,
        standard_field,
        alias
    ):

        if standard_field not in self.dictionary:

            self.dictionary[
                standard_field
            ] = []

        if alias not in self.dictionary[
            standard_field
        ]:

            self.dictionary[
                standard_field
            ].append(alias)