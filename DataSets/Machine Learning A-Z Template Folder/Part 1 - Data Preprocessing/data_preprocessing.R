# Data Preprocessing

# Importing dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, 
                                             FUN = function(x) mean(x, na.rm = TRUE)), dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, 
                                             FUN = function(x) mean(x, na.rm = TRUE)), dataset$Salary)

# Encoding categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(0, 1, 2))
dataset$Purchased = factor(dataset$Purchased,
                           levels = c('Yes', 'No'),
                           labels = c(1, 0))

# Splitting the dataset into Train set and Test set which needs the package 'caTools'
# first install the package 'caTools' by running install.packages('caTools') then select it
library(caTools)   # importing/activating the package
set.seed(123)
# split creates a list of boolean values. If True it is train, else it is false
split = sample.split(dataset$Purchased, SplitRatio = 0.6)
train_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature scaling;    remember that categorical columns can't be scaled in R, only numeric cols
train_set[, 2:3] = scale(train_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])

