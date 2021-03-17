import great_expectations as ge
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult

config = '''
class_name: SimpleSqlalchemyDatasource
credentials:
  drivername: postgresql
  host: hp
  port: 5434
  username: postgres
  password: postgres
  database: test
introspection:
  whole_table: {}
'''
context = ge.get_context()
#context.test_yaml_config(
#    name="chkpt-1",
#    yaml_config=config,
# )

checkpoint_run_result: CheckpointResult = context.run_checkpoint(
    checkpoint_name="chkpt-1",
)
print(checkpoint_run_result)
