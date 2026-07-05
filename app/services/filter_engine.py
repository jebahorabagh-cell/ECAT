"""
------------------------------------------------------------
ECAT
Filter Engine
Build 1.2.0
------------------------------------------------------------
"""


class FilterEngine:

    def apply(self, df, request):

        print("\n========== FILTER ENGINE ==========")

        original_rows = len(df)

        print(f"Original Rows : {original_rows}")

        # -----------------------------
        # Consumer Status
        # -----------------------------

        status = request.get("status")

        if status:

            if "Consumer Status" in df.columns:

                df = df[
                    df["Consumer Status"]
                    .astype(str)
                    .str.upper()
                    ==
                    status.upper()
                ]

                print(
                    f"After Status ({status}) : {len(df)} rows"
                )

        # -----------------------------
        # Tariff
        # -----------------------------

        tariff = request.get("tariff")

        if tariff:

            if "Tariff Category" in df.columns:

                df = df[
                    df["Tariff Category"]
                    .astype(str)
                    .str.upper()
                    ==
                    tariff.upper()
                ]

                print(
                    f"After Tariff ({tariff}) : {len(df)} rows"
                )

        print("\n===================================")

        return df