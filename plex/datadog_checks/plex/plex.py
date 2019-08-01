from plexapi.server import PlexServer

from datadog_checks.base import AgentCheck, ConfigurationError


class PlexCheck(AgentCheck):
    def check(self, instance):
        token = instance.get("token")
        
        if not token:
            raise ConfigurationError("Configuration error, token is missing in plex.yaml")
        
        try:
            # this should run on the same host as the Plex Server
            PlexServer(token=token)
        except Exception as e:
            self.service_check("plex.server", self.CRITICAL, message=str(e))
        else:
            self.service_check("plex.server", self.OK)
