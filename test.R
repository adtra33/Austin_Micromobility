library(ggplot2)

getwd()
readf <- read.csv('Trips2020.csv')
table(readf$Month)

y2020 <-  readf %>% mutate(Month2= recode(Month, 'Jan','Feb','Mar','Apr',
                                         'May','Jun','Jul','Aug','Sep','Oct',
                                         'Nov','Dec'))

ggplot(data = y2020, aes(x = Month2, y = Trip.Distance)) + 
  geom_bar(aes(y = Trip.Distance), stat = 'summary', fun = mean)


