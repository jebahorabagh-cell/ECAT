"""
------------------------------------------------------------
ECAT - Business Rules
Build : 1.1.1
------------------------------------------------------------

All organization-specific rules are stored here.

If feeder names or location codes change in future,
only this file needs to be updated.
"""

# ==========================================================
# Division
# ==========================================================

DIVISION_NAME = "Jabalpur City Division East"

# ==========================================================
# Feeder Mapping
# ==========================================================

FEEDERS = {
    1444201: "HROSE DC(T)",
    1444202: "RIDGE DC(T)",
    1444203: "SADAR DC(T)",
    1444204: "GHAMAPUR DC(T)",
    1444205: "CK HOUSE DC(T)",
    1444206: "RANJHI DC(T)",
    1444207: "DWARKA NAGAR DC(T)",
    1444208: "KATANGA DC(T)",
    1444209: "CIVIL LINE DC(T)",
    1444210: "PACHPEDI DC(T)",
    1444211: "UNIVERSITY DC(T)",
    1444212: "PHOOTATAL DC(T)",
    1444213: "HANUMANTAL DC(T)",
    1444214: "PREMSAGAR DC(T)",
    1444215: "BEOHARBAGH DC(T)",
    1444216: "PASIYANA DC(T)",
    1444217: "OMTI DC(T)",
    1444218: "BAHORABAGH DC(T)",
    1444219: "CHANDNI CHOWK DC(T)",
    1444220: "INDIRA MARKET DC(T)",
    1444221: "CLOCK TOWER DC(T)"
}

# ==========================================================
# Display Order
# ==========================================================

FEEDER_ORDER = [
    1444201,
    1444202,
    1444203,
    1444204,
    1444205,
    1444206,
    1444207,
    1444208,
    1444209,
    1444210,
    1444211,

    1444212,
    1444213,
    1444214,
    1444215,
    1444216,
    1444217,
    1444218,
    1444219,
    1444220,
    1444221
]

# ==========================================================
# Zones
# ==========================================================

ZONE_1 = FEEDER_ORDER[:11]

ZONE_2 = FEEDER_ORDER[11:]

ZONE_NAMES = {
    "ZONE_1": "ZONE 1 SUMMARY",
    "ZONE_2": "ZONE 2 SUMMARY",
    "DIVISION": "DIVISION SUMMARY"
}


# ==========================================================
# Helper Functions
# ==========================================================

def feeder_name(loc_code):
    """
    Returns feeder name from location code.
    """

    try:
        return FEEDERS[int(loc_code)]
    except Exception:
        return f"Unknown ({loc_code})"


def is_zone1(loc_code):

    return int(loc_code) in ZONE_1


def is_zone2(loc_code):

    return int(loc_code) in ZONE_2


def feeder_sequence():

    """
    Returns feeders in report order.
    """

    return FEEDER_ORDER.copy()


def zone_name(zone):

    return ZONE_NAMES.get(zone, zone)
    

