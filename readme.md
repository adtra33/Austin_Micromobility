---
title: "Micromobility in Austin, Texas"
output: html_document
date: "2023-10-03"
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```


# Short Project Description
This project aims to investigate the relationships and correlations between trip duration or trip distance in micromobility vehicles (e.g., electric scooters or bikes) and various factors in Austin, Texas. The variables of interest include year, month, day of the week, hour of the day, temperature, wind speed, and precipitation, Council District Start, Council District End, and Council District Street Condition Percent Satisfactory.

# Goals
Identify correlations and trends between variables to help urban planners, companies such as Lime, and policymakers make better informed decisions about micromobility infrastructure and services in the area. The findings from this project may also contribute to improving the usability and accessibility of micromobility options for people in Austin.

# Link to The Data
<https://data.austintexas.gov/Transportation-and-Mobility/Shared-Micromobility-Vehicle-Trips/7d8e-dm7r>

# Some Information About The Data: 
This dataset contains shared micromobility vehicle trip data from 1970 to 2022 reported to the City of Austin Transportation Department as part of the Shared Small Vehicle Mobility Systems operating rules. The trips included in this dataset have durations less than 24 hours and have trip distances greater than or equal to 0.1 miles and less than 500 miles. Additional weather data and data on 'Council District Street Condition Percent Satisfactory' will be merged with the original micromobility vehicle trip data linked above. This additional data will be considered to analyze the potential effects of these variables, which were not originally included in the shared micromobility vehicle trip data.

# Two Hypotheses:
The mean trip distances for micromobility vehicles are not equal across different months of the year in 2020.
The mean trip distances for micromobility vehicles are not equal across different days of the week in 2020.

# References:
Data is provided by Austin Transportation and The City of Austin, Texas at <https://data.austintexas.gov>
Weather data is provided by <https://www.weather.gov/wrh/Climate?wfo=ewx>
Council District Street Condition Percent Satisfactory data is provided by <https://data.austintexas.gov/City-Infrastructure/Street-Conditions-by-Council-District-DRAFT/un9d-25i8>

# Visualizations:
```{r}
library(ggplot2)
library(dplyr)

# Data from original micromobility dataset for the year 2020
y2020 <- read.csv('Trips2020.csv')

# Create a new column 'Month2' by recoding the 'Month' column with an ordered factor.
y2020 <-  y2020 %>% mutate(Month2 = recode(Month, 'Jan','Feb','Mar','Apr',
                                         'May','Jun','Jul','Aug','Sep','Oct',
                                         'Nov','Dec'), ordered = TRUE)

# Create another new column 'DOW' by recoding the 'Day.of.Week' column with an ordered factor.
y2020 <-  y2020 %>% mutate(DOW = recode(Day.of.Week + 1, 'Sun','Mon','Tues',
                                           'Wed','Thurs','Fri', 'Sat'), ordered = TRUE)
# Define the order of months for plotting.
level_order_months <- c('Jan','Feb','Mar','Apr',
                 'May','Jun','Jul','Aug','Sep','Oct',
                 'Nov','Dec')

# Define the order of days of the week for plotting.
level_order_dow <- c('Sun', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat')

# Bar plot to visualize average 'Trip.Distance' by 'Month2' (months in order) and 'Vehicle.Type'.
ggplot(data = y2020, aes(x = Month2, y = Trip.Distance, fill = Vehicle.Type)) + 
  geom_bar(aes(y = Trip.Distance, x = factor(Month2, levels = level_order_months)), stat = 'summary', fun = mean) + 
  scale_fill_manual(values = c('red','green','blue')) + labs(x = 'Month', y = 'Trip Distance') +
  labs(title = "Average Trip Distance by Month and Vehicle Type") + labs(fill = "Vehicle Type")

# Bar plot to visualize average 'Trip.Distance' by 'DOW' (day of the week) and 'Vehicle.Type'.
ggplot(data = y2020, aes(x = DOW, y = Trip.Distance, fill = Vehicle.Type)) + 
  geom_bar(aes(y = Trip.Distance, x = factor(DOW, levels = level_order_dow)), stat = 'summary', fun = mean) + 
  scale_fill_manual(values = c('red','green','blue')) + labs(x = 'Days of the Week', y = 'Trip Distance') +
  labs(title = "Average Trip Distance by Day of the Week and Vehicle Type") + labs(fill = "Vehicle Type")
```
=======
