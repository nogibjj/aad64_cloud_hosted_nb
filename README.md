# aad64_cloud_hosted_nb
Cloud-Hosted Notebook Data Manipulation

[![Install](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/install.yml)
[![Format](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/aad64_cloud_hosted_nb/actions/workflows/lint.yml)

## Structure of the Project:
```
aad64_cloud_hosted_nb/
├── .github/
│   └── workflows/
│       ├── format.yml
│       ├── install.yml
│       ├── lint.yml
│       └── test.yml
├── .gitignore
├── Week_9.ipynb
├── test_nb.py
├── Makefile
├── requirements.txt
└── README.md
```

## Jupyter Notebook:
This notebook was created using `Google Colab` and then uploaded to my git repository. 

### Ingest:
This section has a few cells to load and glimpse the data. This is just the preliminary section of the notebook that is not necessary to understand the actual data, so it's easily collapsible. 

<p align = 'center'><img width="1219" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/0ab34655-e873-4562-a985-622675a7d6ae"></p>

### EDA:
This section was dedicated to conducting exploratory data analysis. It has many sections and sub-sections, such as overall descriptive statistics (mean, median, mode) of certain variables. There are also more specific plots that have been included in this section, for example, seeing the distribution of the age variable or seeing the distribution of salaries above and below 50K.

<p align = 'center'><img width="1028" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/9575f0f2-60aa-48b8-844d-567b15b187ce"></p>

<p align = 'center'><img width="1040" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/e16590b1-1758-4402-8082-0a253d6ea336"></p>


Plotting Relationships:
The EDA section also had an import subsection to see some possible relationships between certain variables. For example, I was interested in learning more about the variations in salary based on certain demographic information, and plotted the following graphs for the same:

<p align = 'center'><img width="855" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/1587e423-8254-4514-afd4-3cbb6ad631c4"></p>

<p align = 'center'><img width="1037" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/171a331a-f5b4-4b31-9785-f47415186223"></p>

### Modelling and Conclusion:
This section is designed to do some further analyses with this data. However, since I do not have domain knowledge on the matter, these analyses were not carried forward. As of now, my conclusions are based on the EDA, which were elaborated upon in the `Conclusion` section. 


## Workflows:

As seen below, my code passes the following CI/CD best practices. This is also highlighted by the status badges at the top of the README.

### Linting:
This was done using ruff (`ruff check *.py`).
<p align = 'center'><img width="500" alt="image" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/a1ccf3ec-24c4-434e-bf28-96c4007832f8"></p>

### Formatting: 
Using the black formatter, my project was fully formatted. 
<p align = 'center'><img width="512" alt="image" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/d15bb152-6e28-4278-8c72-41ccc3318814"></p>

### Testing:
This was done by creating a `test_nb.py` file which was specfically created to hold a unit test for the jupyter notebook I created. This was then run and tested using `nbval` (which was declared and installed using the requirements.txt).

<p align = 'center'><img width="1254" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/55bab811-1396-4a26-9089-81360cc554f7"></p>
