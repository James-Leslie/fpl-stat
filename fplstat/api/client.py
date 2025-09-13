import requests


class FPLstat:
    """
    `FPLstat` client, the main entry point for interacting with the Fantasy Premier
    League API.

    ## Example
    ```python
    from fplstat import FPLstat

    client = FPLstat()
    ```
    """

    BASE_URL = "https://fantasy.premierleague.com/api"

    def __init__(self):
        self.session = requests.Session()
        self._cache = {}

    def get_bootstrap(self, use_cache=True):
        if use_cache and "bootstrap" in self._cache:
            return self._cache["bootstrap"]

        response = self.session.get(f"{self.BASE_URL}/bootstrap-static/")
        response.raise_for_status()
        data = response.json()

        if use_cache:
            self._cache["bootstrap"] = data
        return data

    def get_elements(self):
        """Convenience method that extracts just elements (players)"""
        bootstrap = self.get_bootstrap()
        return bootstrap["elements"]
