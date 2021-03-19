import great_expectations as ge
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
import sys

context = ge.get_context()
data_asset_name = sys.argv[1]
checkpoint_run_result: CheckpointResult = context.run_checkpoint(
    checkpoint_name="chkpt-1", validations=[
        {"batch_request":
            {
                "datasource_name": "pg",
                "data_connector_name": "pg_connector",
                "data_asset_name": data_asset_name
            },
            "expectation_suite_name": "patient.warning"
        }
    ]
)
print(checkpoint_run_result)
