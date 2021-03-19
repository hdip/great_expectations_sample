import great_expectations as ge
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
import sys
import datetime

context = ge.get_context()
batch = 'batch-' + str(datetime.datetime.now().strftime('%Y%m%d%H%m%S'))
data_asset_name = sys.argv[1]
checkpoint_run_result: CheckpointResult = context.run_checkpoint(run_id=batch,
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
