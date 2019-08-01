from datadog_checks.plex import PlexCheck


def test_check(aggregator, instance):
    check = PlexCheck('plex', {}, {})
    check.check(instance)

    aggregator.assert_all_metrics_covered()
