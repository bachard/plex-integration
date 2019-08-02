from plexapi.library import MovieSection
from plexapi.server import PlexServer

from datadog_checks.base import AgentCheck, ConfigurationError


class PlexCheck(AgentCheck):

    def check(self, instance):
        baseurl = instance.get("baseurl")
        token = instance.get("token")
        
        if not token:
            raise ConfigurationError("Configuration error, token is missing in plex.yaml")
        
        try:
            plex = PlexServer(baseurl=baseurl, token=token)
        except Exception as e:
            self.service_check("plex.server", self.CRITICAL, message=str(e))
        else:
            self.service_check("plex.server", self.OK)

        movies_playing_count = 0

        for section in plex.library.sections():
            if section.TYPE == MovieSection.TYPE:
                for movie in section.all():
                    # print(movie.title, movie.isWatched, movie.viewCount)
                    if movie.isWatched:
                        movies_playing_count += 1

        self.gauge('plex.movies.playing', movies_playing_count)
