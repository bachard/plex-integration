# Agent Check: plex

## Overview

This check monitors [plex][1] through the Datadog Agent.

## Setup

### Installation

To install the plex check on your host:

1. Install the [developer toolkit](https://docs.datadoghq.com/developers/integrations/new_check_howto/#developer-toolkit) on any machine.
2. Run `ddev release build plex` to build the package.
3. [Download the Datadog Agent](https://app.datadoghq.com/account/settings#agent).
4. Upload the build artifact to any host with an Agent andrun `datadog-agent integration install -w path/to/plex/dist/<ARTIFACT_NAME>.whl`.

### Configuration

1. Edit the `plex.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your plex performance data. See the [sample plex.d/conf.yaml][2] for all available configuration options.

2. [Restart the Agent][3].

### Validation

[Run the Agent's status subcommand][4] and look for `plex` under the Checks section.

## Data Collected

### Metrics

plex does not include any metrics.

### Service Checks

plex does not include any service checks.

### Events

plex does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][5].

[1]: **LINK_TO_INTEGRATION_SITE**
[2]: https://github.com/DataDog/integrations-core/blob/master/plex/datadog_checks/plex/data/conf.yaml.example
[3]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#start-stop-and-restart-the-agent
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#agent-status-and-information
[5]: https://docs.datadoghq.com/help
