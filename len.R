rm(list = ls())
require(reshape2)
library(datasets)
library(ggplot2)

x1 <- data.frame(group = "54", value =c(0.892585,0.886151,0.903666,0.898129,0.889508))
x2 <- data.frame(group = "108", value =c(0.944809,0.943982,0.953002,0.949844,0.946083))
x3 <- data.frame(group = "162", value =c(0.963004,0.961318,0.970640,0.967613,0.963675))
x4 <- data.frame(group = "216", value =c(0.963388,0.963845,0.972177,0.968332,0.965252))

plot.data <- rbind(x1, x2, x3, x4)

p10 <- ggplot(plot.data, aes(x=group, y=value, fill=group)) +
  geom_boxplot()
p10 <- p10 + scale_y_continuous(name="AUC value")
p10
