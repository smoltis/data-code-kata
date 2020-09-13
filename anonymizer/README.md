1. Clone Names and Surnames database
```bash
git clone https://github.com/smashew/NameDatabases.git
```
2. Run the app to generate a CSV file to anonymize. 
```bash
python csv_generator.py
```

3. Load the file into Spark/Databricks and run `Anonymize data Spark.py` notebook.

4. The code will produce two files one with real and anonymized values side by side and the other one with anonymous data only.