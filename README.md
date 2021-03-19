# great_expectations_sample
Great expectations sample project with postgresql

Expects (Ofcourse you can update to your setup in uncommitted/config_variables.yml)
- postgresql running on port 5434;
- environment variable POSTGRES_PASSWORD; You can do this in non-windows OS ```export POSTGRES_PASSWORD=****```
- table called patient with definition as below 
```
                        Table "public.patient"
   Column   |          Type          | Collation | Nullable | Default 
------------+------------------------+-----------+----------+---------
 id         | integer                |           |          | 
 first_name | character varying(100) |           |          | 
 last_name  | character varying(100) |           |          | 
 mpi        | character varying(100) |           |          | 
 
 ```
Using a command line parameter to supply the table/ view name. Can be used to create a dynamic command at runtime

Run with ```python /path/to/uncommitted/chkpt-1.py patient```

This also created the docs and results

The notebooks dont work  probably  due to using SimpleSqlAlchemy datasource and not the v2 SqlAlchemydatasource

```great_expectations suite edit patient.warning```

You can still view docs/ results with command below ; Or simply open the html page created in the docs folder in the browser

```great_expectations docs build```


