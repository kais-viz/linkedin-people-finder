# Company watchlist using Linkedin users current job
A simple Jupyter Notebook script that uses Tom Quirk's [unofficial LinkedIn API](https://github.com/tomquirk/linkedin-api) to gather a list of company that hired people based on specific job titles.

## Requirements
* [LinkedIn API](https://github.com/tomquirk/linkedin-api) python package
* Valid LinkedIn account

## Setup
1) To install .ipynb Jupyter Notebook on Ubuntu, see [How To Set Up Jupyter Notebook with Python 3 on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-jupyter-notebook-with-python-3-on-ubuntu-18-04). To install it on windows, see [Anaconda](https://docs.anaconda.com/anaconda/install/windows/).
2) To install Linkedin's unofficial API, run this command:
```pip install -e git+https://github.com/tomquirk/linkedin-api.git#egg=linkedin_api```

## Future Development
Currently, the script returns a list of company urn's, name, and size margin. In the future, I plan to dig deeper into LinkedIn's HTML source code to be able to grab company pages from companyUrn which will return more useful results such as the company website and an exact number of employees.