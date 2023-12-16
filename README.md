# Customer Feedback Analysis System

A project for analyzing and visualizing customer feedback data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Libraries & Tools](#libraries--tools)
- [Project Roadmap](#project-roadmap)

## Installation

Follow these steps to install and set up the project:

1. Clone the repository: `git clone https://github.com/ellisperez47/Customer_Feedback_Analysis_System.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure settings: Edit the `config.ini` file with your API keys.

## Usage

To use the Customer Feedback Analysis System:

1. Run the main script: `python main.py --input inputfile.txt --output outputfile.txt`
2. View the generated data visualizations in the `visualizations` folder.

## Contributing

We welcome contributions to improve this project. Follow these steps to contribute:

1. Fork the project.
2. Create a new branch: `git checkout -b feature/new-feature`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to your fork: `git push origin feature/new-feature`
5. Submit a pull request.

## License

This project is licensed under the [GNU General Public License (GPL)](link-to-license-file). See the [LICENSE](link-to-license-file) file for details.

## Acknowledgments

- Special thanks to Dan Ng for valuable feedback, Cris for the inspiration, and my family for all of their love and support.

## Libraries & Tools

This project relies on the following libraries and tools:

- [spaCy](https://spacy.io/usage): A powerful NLP library for Python.
- [TextBlob](https://textblob.readthedocs.io/en/dev/): An easy-to-use NLP library.
- [Pandas](https://pandas.pydata.org/docs/): A versatile data manipulation and analysis library.
- [NumPy](https://numpy.org/doc/): A fundamental library for numerical computing.
- [Matplotlib](https://matplotlib.org/stable/contents.html): A Python library for creating visualizations.
- [Seaborn](https://seaborn.pydata.org/introduction.html): A data visualization library based on Matplotlib.
- [Microsoft Power BI](https://docs.microsoft.com/en-us/power-bi/): A business intelligence tool for data visualization.
- [GitHub](https://github.com/): A platform for version control and collaboration.
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/): A versatile code editor.
- [Databricks Community Edition](https://databricks.com/try-databricks): An environment for data engineering and analytics.

These tools and libraries are essential for various aspects of this project, from data processing to natural language processing and data visualization.

## Project Roadmap
Data Collection and Dataset Preparation
- [x] Data Collection
	- Data was collected from Google Places API to gather customer reviews and ratings for resturants.
	- The collected data was sotred in CSV files for further analysis.
- [x] Data Cleaning
	- Basic data cleaning was performed on the collected data to ensure its quality.
	- Missing values were handled, duplicate entries were removed, and text with fewer than 3 words was filtered out.
	- The cleaned data was saved to separate CSV files.
- [x] Dataset Prepration
	- A separate Python script was created to prepare the data for analysis.
	- The script loaded the cleaned data, organized it into a clean DataFrame, and defined columns and data types.
	- The resulting data was saved in a structured format for analysis.
- [x] Data Security Steps
	- Data security measures were taken to protect sensitive customer information.
	- Sensitive data such as customer names and contact details were anonymized or removed from the dataset.
	- Access to the data and project files was restricted to authorized team members only.
Data Processing and Exploration
- [] Data Preprocessing
- [] Data Loading
- [] Data Exploration 
Exploratory Data Analysis
- [] Univariate Analysis
- [] Bivariate Analysis
- [] Mulitvariate Analysis
- [] Insights and Conclusions
Basic NLP Implementation
Building & Testing a Simple Sentimental Analysis Model
Refining Sentiment Analysis Model
Text Summarization Implementation
Improving Text Summarization Model and Keyword Extraction
Integration of NLP Models and Initial Data Visualization
Power Bi Visualizations and Dashboard Creation

