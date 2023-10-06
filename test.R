library(ggplot2)
library(dplyr)

getwd()
y2020 <- read.csv('Trips2020.csv')

y2020 <-  y2020 %>% mutate(Month2 = recode(Month, 'Jan','Feb','Mar','Apr',
                                         'May','Jun','Jul','Aug','Sep','Oct',
                                         'Nov','Dec'), ordered = TRUE)

y2020 <-  y2020 %>% mutate(DOW = recode(Day.of.Week, 'Sun','Mon','Tues',
                                           'Wed','Thurs','Fri', 'Sat'), ordered = TRUE)
level_order <- c('Jan','Feb','Mar','Apr',
                 'May','Jun','Jul','Aug','Sep','Oct',
                 'Nov','Dec')


ggplot(data = y2020, aes(x = Month2, y = Trip.Distance, fill = Vehicle.Type)) + 
  geom_bar(aes(y = Trip.Distance, x = factor(Month2, levels = level_order)), stat = 'summary', fun = mean) + 
  scale_fill_manual(values = c('red','green','blue')) + labs(x = 'Month')

ggplot(data = y2020, aes(x = DOW, y = Trip.Distance, fill = Vehicle.Type)) + 
  geom_bar(aes(y = Trip.Distance, x = factor(DOW)), stat = 'summary', fun = mean) + 
  scale_fill_manual(values = c('red','green','blue')) + labs(x = 'Days of the Week')


table(y2020$Day.of.Week)

unique(y2020$Day.of.Week)
