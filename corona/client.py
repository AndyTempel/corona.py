from typing import List

from corona.http import HttpClient
from corona.objects import WorldStatistic, StateStatistic, CountryStatistic, JHUCSSE, TimelineSeries, Historic
from corona.router import Router


class Client:
    def __init__(self, router: Router = None):
        self.router = router if router else Router()  # type: Router
        self.http = HttpClient()

    @classmethod
    def bot(cls, bot, router: Router = None):
        """
        Plugs this Client object into your discord.py Bot object. Access it by 'bot.corona'

        :param bot: Your discord.py bot object
        :param router: Optional. Router
        :return: Client
        """
        cli = cls(router)
        setattr(bot, "corona", cli)
        return cli

    async def world(self) -> WorldStatistic:
        """
        Gets current total from all around the world.

        :return: WorldStatistic
        """
        data = await self.http.request(self.router.world)
        return WorldStatistic(**data)

    async def world_timeline(self) -> TimelineSeries:
        """
        Get timeline series for total all around the world.

        :return: TimelineSeries
        """
        data = await self.http.request(self.router.historical_all)
        return TimelineSeries(**data)

    async def us_states(self) -> List[StateStatistic]:
        """
        Gets current statistics from USA state by state.

        :return: List[StateStatistic]
        """
        data = await self.http.request(self.router.us_all)
        return [StateStatistic(**x) for x in data]

    async def countries(self) -> List[CountryStatistic]:
        """
        Gets current statistics country by country.

        :return: List[CountryStatistic]
        """
        data = await self.http.request(self.router.countries)
        return [CountryStatistic(**x) for x in data]

    async def countries_sorted(self, sort_by: str) -> List[CountryStatistic]:
        """
        Gets current statistics country by country. Sorted.

        :param sort_by: One of: cases, todayCases, deaths, todayDeaths, recovered, active, critical, casesPerOneMillion, deathsPerOneMillion
        :return: List[CountryStatistic]
        """
        data = await self.http.request(self.router.countries_sort_by(sort_by))
        return [CountryStatistic(**x) for x in data]

    async def country(self, country: str) -> CountryStatistic:
        """
        Get statistics for the specified country.

        :param country: ISO2, ISO3, ID or Country name
        :return: CountryStatistic
        """
        data = await self.http.request(self.router.countries_by_country(country))
        return CountryStatistic(**data)

    async def jhu_csse(self) -> List[JHUCSSE]:
        """
        Get data from John Hopkins University portal.

        :return: List[JHUCSSE]
        """
        data = await self.http.request(self.router.jhu_csse)
        return [JHUCSSE(**x) for x in data]

    async def timeline_all(self) -> List[Historic]:
        """
        Get timeline for all countries, separate.

        :return: List[Historic]
        """
        data = await self.http.request(self.router.historical)
        return [Historic(**x) for x in data]

    async def timeline_by_country(self, country: str) -> Historic:
        """
        Get timeline for a specific country.

        :param country: ISO2, ISO3, ID or Country name
        :return: Historic
        """
        data = await self.http.request(self.router.historical_by_country(country))
        return Historic(**data)

    async def timeline_by_province(self, country: str, province: str) -> Historic:
        """
        Get timeline for a specific province in country.

        :param country: ISO2, ISO3, ID or Country name
        :param province: Province name
        :return: Historic
        """
        data = await self.http.request(self.router.historical_by_provice(country, province))
        return Historic(**data)


