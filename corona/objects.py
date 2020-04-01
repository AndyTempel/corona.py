import abc
import sys
from datetime import datetime, timezone

ASCII_LOWER = "abcdefghijklmnopqrstuvwxyz0123456789"
OFFSET = 127397

DATE_ISOFRMT36 = sys.version.startswith("3.6")


class Country:
    def __init__(self, country_name, **data):
        self.name = country_name
        self.id = data.get('_id')  # type: int
        self.iso2 = data.get('iso2')  # type: str
        self.iso3 = data.get('iso3')  # type: str
        self.coordinates = (data.get('lat'), data.get('long'))  # type: tuple
        self.flag = data.get('flag')  # type: str

    @property
    def emoji(self) -> str:
        code = [c for c in self.iso2.lower() if c in ASCII_LOWER]
        points = [ord(c.upper()) + OFFSET for c in code]
        return chr(points[0]) + chr(points[1])


class GenericStatistic(abc.ABC):
    def __init__(self, **data):
        self.cases = data.get('cases')  # type: int
        self.deaths = data.get('deaths')  # type: int
        self.recovered = data.get('recovered')  # type: int
        self.updated = datetime.fromtimestamp(int(data.get('updated')) / 1000.0, tz=timezone.utc)  # type: datetime
        self.active = data.get('active')  # type: int


class ExtendedStatistic(GenericStatistic):
    def __init__(self, **data):
        super().__init__(**data)
        self.today_cases = data.get('todayCases')  # type: int
        self.today_deaths = data.get('todayDeaths')  # type: int
        self.critical = data.get('critical')  # type: int
        self.cases_per_one_million = data.get('casesPerOneMillion')  # type: int
        self.deaths_per_one_million = data.get('deathsPerOneMillion')  # type: int


class WorldStatistic(GenericStatistic):
    def __init__(self, **data):
        super().__init__(**data)
        self.affected_countries = data.get('affectedCountries')  # type: int


class StateStatistic:
    def __init__(self, **data):
        self.state = data.get('state')  # type: str
        self.deaths = data.get('deaths')  # type: int
        self.today_deaths = data.get('todayDeaths')  # type: int
        self.cases = data.get('cases')  # type: int
        self.today_cases = data.get('todayCases')  # type: int
        self.active = data.get('active')  # type: int

    def __repr__(self):
        return "<StateStatistic state={}>".format(self.state)


class CountryStatistic(ExtendedStatistic):
    def __init__(self, **data):
        super().__init__(**data)
        self.country = Country(data.get('country'), **data.get('countryInfo'))  # type: Country

    def __repr__(self):
        return "<CountryStatistic name={}>".format(self.country.name)


class CountryProvinceHead(abc.ABC):
    def __init__(self, **data):
        self.country = data.get('country')  # type: str
        self.province = data.get('province') or ""  # type: str


class TimelineSeries(abc.ABC):
    def __init__(self, **data):
        self.cases_timeline = data.get('cases')  # type: dict
        self.deaths_timeline = data.get('deaths')  # type: dict
        self.recovered_timeline = data.get('recovered')  # type: dict


class JHUCSSE(CountryProvinceHead):
    def __init__(self, **data):
        super().__init__(**data)
        self.updated_at = datetime.strptime(data.get('updatedAt'), "%Y-%m-%d %H:%M:%S") if DATE_ISOFRMT36 else \
            datetime.fromisoformat(data.get('updatedAt'))  # type: datetime
        stats = data.get('stats')
        self.confirmed = stats.get('confirmed')  # type: int
        self.deaths = stats.get('deaths')  # type: int
        self.recovered = stats.get('recovered')  # type: int
        coords = data.get('coordinates')
        self.coordinates = (float(coords.get('latitude')), float(coords.get('longitude')))  # type: tuple

    def __repr__(self):
        return "<JHUCSSE country={} province={}>".format(self.country, self.province)


class Historic(CountryProvinceHead, TimelineSeries):
    def __init__(self, **data):
        super().__init__(**data)
        super(CountryProvinceHead, self).__init__(**data.get('timeline'))

    def __repr__(self):
        return "<Historic country={} province={}>".format(self.country, self.province)
