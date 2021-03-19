# great_expectations_sample
Great expectations sample project with postgresql

Using a command line parameter to supply the table/ view name. Can be used to create a dynamic command at runtime

Run with ```python /path/to/uncommitted/chkpt-1.py patient```

This also created the docs and results

For any ge cli seems you have to be one folder above the ge folder and the name of top folder has to be great_expectations

```cd .. && mv great_expectations_sample great_expectations```

The notebooks dont work  probably  due to using SimpleSqlAlchemy datasource and not the v2 SqlAlchemydatasource

```great_expectations suite edit patient.warning```

You can still view docs/ results with command below ; Or simply open the html page created in the docs folder in the browser

```great_expectations docs build```


