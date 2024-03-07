# Education and economic development

## Introduction
This project explores the relationship between education and economic development. 
The analysis focuses on understanding how various factors, including literacy rates, government spending on education, and primary school graduates, influence GDP growth.

## Data Used:
- **GDP Change:** Dataset containing information on GDP growth rates per country over time.
- **Education Rates:** Dataset providing information on education completion levels across different regions and time periods.
- **Literacy Rates:** Additional dataset including literacy rate data for various regions and time periods.
- **Unemployment Rates:** Dataset containing unemployment rate data for various regions and time periods.
- **Government Spending on Education:** Dataset containing information on government expenditures allocated to education for various regions and time periods.


**Challenges:**
Challenges arose when attempting to merge datasets with mismatched country and year values.
Handling null and infinite values presented difficulties during statistical calculations, requiring special attention to avoid errors.
Negative values posed challenges when applying transformations such as logarithmic and square root functions. In the end adding a constant value method was chosen.

## Education and Economic Development Questions:

1. **Impact of Education on Economic Growth:**
   - *Question:* How does the level of education attainment affect economic growth?
   - *Conclusion:*  Higher levels of education attainment are positively associated with economic growth. Nonetheless, the model's R-squared value indicates relatively low predictive accuracy, indicating the presence of other influential factors.

2. **Relationship between Literacy Rates and GDP Growth:**
   - *Question:* Is there a correlation between literacy rates and GDP growth?
   - *Conclusion:* A positive correlation is observed between literacy rates and GDP growth. Nonetheless, the model's R-squared value indicates relatively low predictive accuracy, indicating the presence of other influential factors.

3. **Effectiveness of Government Spending on Education:**
   - *Question:* Does increased government spending on education lead to higher GDP growth?
   - *Conclusion:* There is evidence to suggest that higher government spending on education positively influences GDP growth. Nonetheless, the model's R-squared value indicates relatively low predictive accuracy, indicating the presence of other influential factors.


## Methodology Description:
1. **Data Cleaning:**
   - **Dropping Columns:** Removed unnecessary columns from the dataset to focus on relevant variables for analysis.
   - **Handling Null and Inf Values:** Cleared null and infinite values from the dataset to prevent errors during analysis.
   - **Excluding Extreme Values with Z-Score:** Identified and excluded extreme values using Z-score method to ensure robust statistical analysis.
   
2. **Analysis:**
   - **OLS Regression Analyses:** Conducted Ordinary Least Squares (OLS) regression analyses to investigate the relationship between variables.
   
3. **Transformation for Better Fit:**
   - **Transformation Techniques:** Applied transformation techniques such as logarithmic or square root transformations to improve the fit of the data to statistical models and assumptions.

 ## Conclusion:

While statistically significant relationships were identified between education indicators and economic outcomes, the explanatory power of our models was limited, with R-squared values indicating low predictive accuracy. 
Additional variables are required to further investigate these relationships effectively.

## Data Sources:

1. Education Data:
   - Barro-Lee Educational Attainment Dataset: [Link](https://barrolee.github.io/BarroLeeDataSet/OUPdownload.html)
   - Description: The Barro-Lee dataset provides comprehensive information on educational attainment levels across different countries and time periods.

2. GDP Data:
   - Kaggle Countries GDP Dataset: [Link](https://www.kaggle.com/datasets/rinichristy/countries-gdp-19602020?resource=download)
   - Description: The Kaggle dataset offers GDP data for various countries from 1960 to 2020.

3. Real GDP Growth:
   - Our World in Data: Real GDP Growth Dataset: [Link](https://ourworldindata.org/grapher/real-gdp-growth)
   - Description: The Our World in Data platform offers real GDP growth data, providing insights into economic growth rates across different countries and regions.

4. Unemployment Rate:
   - Our World in Data: Unemployment Rate Dataset: [Link](https://ourworldindata.org/grapher/unemployment-rate?time=earliest)
   - Description: The Our World in Data platform provides data on unemployment rates globally.
