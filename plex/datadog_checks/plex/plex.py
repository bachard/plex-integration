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

    def _report_media_in_use(self):
        media_in_use = len(plex.sessions())
        self.gauge('plex.media.in_use', media_in_use)
