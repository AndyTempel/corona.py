class Router:
    BASE_URL = "https://corona.lmao.ninja/"

    def __init__(self, base_url: str = BASE_URL):
        self.us = object()
        self.base = base_url
        self.world = base_url + "all"
        self.us_all = base_url + "states"
        self.countries = base_url + "countries"
        self.countries_by_country = self._country
        self.countries_sort_by = self._country_sort

        # v2 API
        self.jhu_csse = base_url + "v2/jhucsse"
        self.historical = base_url + "v2/historical"
        self.historical_all = base_url + "v2/historical/all"
        self.historical_by_country = self._historical_by_country
        self.historical_by_provice = self._historical_by_province

    def _country(self, country_code: str) -> str:
        return self.base + "countries/{}".format(country_code)

    def _country_sort(self, parameter: str) -> str:
        if parameter not in ["cases", "todayCases", "deaths", "todayDeaths", "recovered", "active", "critical",
                             "casesPerOneMillion", "deathsPerOneMillion"]:
            raise ValueError("Parameter must be one of: cases, todayCases, deaths, todayDeaths, recovered, active, "
                             "critical, casesPerOneMillion, deathsPerOneMillion")
        return self.base + "countries?sort={}".format(parameter)

    def _historical_by_country(self, country_code: str) -> str:
        return self.base + "v2/historical/{}".format(country_code)

    def _historical_by_province(self, country_code: str, province_name: str) -> str:
        return self.base + "v2/historical/{}/{}".format(country_code, province_name)
