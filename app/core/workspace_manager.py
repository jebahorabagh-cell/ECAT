"""
------------------------------------------------------------
ECAT
Workspace Manager
Build 1.0.11
------------------------------------------------------------
"""


class WorkspaceManager:
    """
    Manages all pages inside ECAT.
    """

    def __init__(self):

        self.pages = {}

        self.current = None

    # --------------------------------------------------

    def register(
        self,
        name,
        page
    ):

        self.pages[name] = page

    # --------------------------------------------------

    def show(
        self,
        name
    ):

        if self.current:

            self.current.pack_forget()

        self.current = self.pages.get(name)

        if self.current:

            self.current.pack(
                fill="both",
                expand=True
            )

    # --------------------------------------------------

    def names(self):

        return list(self.pages.keys())