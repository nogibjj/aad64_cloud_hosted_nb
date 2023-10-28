# aad64_cloud_hosted_nb
Cloud-Hosted Notebook Data Manipulation

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
### Ingest:
This section has a few cells to load and glimpse the data. This is just the preliminary section of the notebook that is not necessary to understand the actual data, so it's easily collapsible. 

<p align = 'center'><img width="1219" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/0ab34655-e873-4562-a985-622675a7d6ae"></p>

### EDA:
This section was dedicated to conducting exploratory data analysis. It has many sections and sub-sections, such as overall descriptive statistics (mean, median, mode) of certain variables. There are also more specific plots that have been included in this section, for example, seeing the distribution of the age variable or seeing the distribution of salaries above and below 50K.

<p align = 'center'>![image](https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/d45aa297-659f-43c3-9a78-b3f7fdba4230)</p>

<p align = 'center'>![image](https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/2d042e88-1d90-4332-b8ca-7b3f29064164)</p>


Plotting Relationships:
The EDA section also had an import subsection to see some possible relationships between certain variables. For example, I was interested in learning more about the variations in salary based on certain demographic information, and plotted the following graphs for the same:

<p align = 'center'>![image](https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/684c841a-daa5-498c-92a0-98a78f499a2c)</p>

<p align = 'center'>![image](https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/c169219b-8c3b-4b73-bf11-d9702b3e8251)</p>

### Modelling:
This section is designed to do some further analyses with this data. However, since I do not have domain knowledge on the matter, these analyses were not carried forward. As of now, my conclusions are based on the EDA, which were elaborated upon in the `Conclusion` section. 


## Workflows:

As seen below, my code passes the following CI/CD best practices:

### Linting:
This was done using ruff (`ruff check *.py`).
<p align = 'center'><img width="500" alt="image" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/a1ccf3ec-24c4-434e-bf28-96c4007832f8"></p>

### Formatting: 
Using the black formatter, my project was fully formatted. 
<p align = 'center'><img width="512" alt="image" src="https://github.com/nogibjj/aad64_Pandas-Script/assets/143753050/d15bb152-6e28-4278-8c72-41ccc3318814"></p>

### Testing:
This was done by creating a `test_nb.py` file which was specfically created to hold a unit test for the jupyter notebook I created. This was then run and tested using `nbval` (which was declared and installed using the requirements.txt).

<p align = 'center'><img width="1254" alt="image" src="https://github.com/nogibjj/aad64_cloud_hosted_nb/assets/143753050/55bab811-1396-4a26-9089-81360cc554f7"></p>