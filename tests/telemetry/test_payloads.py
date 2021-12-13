# import pytest


# from ddtrace.internal.telemetry.data.metrics import Series
# from ddtrace.internal.telemetry.data.metrics import get_hostname

# from ddtrace.internal.telemetry.data.payload import AppGenerateMetricsPayload

# def test_generate_metrics_payload_to_dict():
#     """validates the return value of AppGenerateMetricsPayload.to_dict"""
#     series_array = [Series("test.metric", "count", False, 10)]
#     payload = AppGenerateMetricsPayload(series_array)

#     assert len(payload.series) == 1
#     assert payload.to_dict() == {
#         "namespace": "tracers",
#         "lib_language": "python",
#         "lib_version": get_version(),
#         "series": [
#             {
#                 "metric": "test.metric",
#                 "points": [],
#                 "tags": {},
#                 "type": "count",
#                 "common": False,
#                 "interval": 10,
#                 "host": get_hostname(),
#             },
#         ],
#     }
