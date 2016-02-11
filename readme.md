# Warren

### The Super-smart Investment Advisor

Our ([@iamdurgadas](https://github.com/kamathd), [@sheldon_ferns](https://twitter.com/sheldon_ferns) and Akhil Rane) entry to the IBM Bluemix hackathon.

Warren uses several Watson cognitive services to recommend stock options.

- The Flask based API proxy depends on a bunch of Python modules. Install them, replace the Bluemix API tokens/creds because the preset ones won't work. Then
```
python ./api.py
```
- Install the dependencies for the frontend
```
bower install Chart.js angular angular-bootstrap animate.css bootstrap-switch checkbox3 font-awesome highcharts jqcloud2 matchHeight typeahead.js ace-builds angular-animate angular-jqcloud bootstrap bootstrap3-typeahead datatables fontawesome jQCloud jquery select2
```
- Replace all API endpoint references to your instance. Then, make httpd+php point to ./ui/html

