from log_flow import log_flow
from prefect.deployments import Deployment

deployment = Deployment.build_from_flow(
    flow=log_flow,
    name="simply_log",
    parameters={"name": "Vicky"},
    infra_overrides={"env": {"PREFECT_LOGGING_LEVEL": "DEBUG"}},
    work_queue_name="test",
)

if __nam__ == '__main__':
    deployment.apply()

