# Overview

## Background
This project aims to investigate the relationships and correlations between trip duration or trip distance in micro-mobility vehicles of scooters, bicycles, and mopeds, along with various factors in Austin, Texas.
The goals of this project are to identify correlations and trends between variables to help urban planners, companies such as Lime, and policymakers make better-informed decisions about micro-mobility infrastructure and services in the area. The findings from this project may also contribute to improving the usability and accessibility of micro-mobility options for people in Austin.

## Motivations
*   Urban Planning Impact: As micro-mobility vehicles begin to play a bigger role in everyday transportation. These vehicles will influence how the city will plan infrastructure projects such as dedicated bike lanes and parking spots.
*   New Transportation Policies: The continued uptick in micro-mobility vehicle usage each year can create a dilemma in the field of transportation. In other words, policymakers will need data-driven insights, such as this project, to effectively make new rules and regulations on the roadway.
*   Service Optimization for companies: As briefly mentioned in our goals, companies providing micro-mobility vehicle services such as Lime and Bird, can greatly benefit from understanding user behavior, various correlations, and common vehicle patterns. These pieces of information can allow these companies to better optimize their pricing strategies and manage their fleets.

## Data
*   The primary dataset used in our analysis is the ‘Shared Micro-mobility Vehicle Trips’ dataset provided by the city of Austin. This dataset contains individual micro-mobility trips from 2019 to 2022, totalling to 15 million rows each representing a trip. The criteria for a trip, as defined by the city of Austin, has a distance greater than 0.1 miles and less than 500 miles and has a duration that is less than 24 hours.
*   In addition to our primary Micromobility dataset, we also used Austin weather data which was provided by the National Weather Service. The weather data contained the monthly average temperature and precipitation for the year of 2019 - 2021

#Analysis

#Modeling

#Limitations
*   Initial data size was too large.
  This made it difficult for the models to find a common trend or correlation between data points and due to the smaller sample size, the accuracy of our results were naturally lower than the true values. 
*   COVID.
  Some of the problems that potentially arose from this was that some of the data for some vehicles were not as plentiful as we would have liked. Due to the potential shock of the pandemic, the reasoning behind some of our conclusions may be misplaced.
*   Potential input errors.
  Our dataset came with many outliers which required an intensive data filtration process and careful consideration of what variables we would use
