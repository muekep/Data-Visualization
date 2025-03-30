#installing and load the necessary libraris
install.packages("ggplot2")
library(ggplot2)
install.packages('dplyr')
library(dplyr)
# Read the data from  the folder
data <- read_csv('C:/Users/Paul/Nexford/Netflix_shows_movies.csv')
#creating the barchart for rating against type of cast
data %>%
group_by(rating, type) %>%
summarise(count = n()) %>%
ggplot(aes(x = rating, y = count, fill = type)) +
geom_bar(stat = 'identity', position = 'dodge') +
labs(title = 'ggplot2 Grouped Bar Chart: rating vs type')
