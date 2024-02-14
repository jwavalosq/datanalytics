source("http://www.openintro.org/stat/data/arbuthnot.R")

class(arbuthnot)
#[1] "data.frame"

str(arbuthnot)
#'data.frame':	82 obs. of  3 variables:
#$ year : int  1629 1630 1631 1632 1633 1634 1635 1636 1637 1638 ...
#$ boys : int  5218 4858 4422 4994 5158 5035 5106 4917 4703 5359 ...
#$ girls: int  4683 4457 4102 4590 4839 4820 4928 4605 4457 4952 ...

dim(arbuthnot)
#[1] 82  3

head(arbuthnot)
#  year boys girls
#1 1629 5218  4683
#2 1630 4858  4457
#3 1631 4422  4102
#4 1632 4994  4590
#5 1633 5158  4839
#6 1634 5035  4820

tail(arbuthnot)
#   year boys girls
#77 1705 8366  7779
#78 1706 7952  7417
#79 1707 8379  7687
#80 1708 8239  7623
#81 1709 7840  7380
#82 1710 7640  7288

head(arbuthnot, 10)
#   year boys girls
#1  1629 5218  4683
#2  1630 4858  4457
#3  1631 4422  4102
#4  1632 4994  4590
#5  1633 5158  4839
#6  1634 5035  4820
#7  1635 5106  4928
#8  1636 4917  4605
#9  1637 4703  4457
#10 1638 5359  4952

str(arbuthnot$boys)
#int [1:82] 5218 4858 4422 4994 5158 5035 5106 4917 4703 5359 ...

class(boys) #This line gives an error:
#Error: object 'boys' not found

class(arbuthnot$boys)
#[1] "integer"

boys = "Blue"   
boys = "male" 
girls = "female" 

class(boys)
#[1] "character"

number = 8 

vect = c(1,2,3,4,6,8,0)
(vect)
#[1] 1 2 3 4 6 8 0

names(arbuthnot)
#[1] "year"  "boys"  "girls"

str(arbuthnot)
#'data.frame':	82 obs. of  3 variables:
#$ year : int  1629 1630 1631 1632 1633 1634 1635 1636 1637 1638 ...
#$ boys : int  5218 4858 4422 4994 5158 5035 5106 4917 4703 5359 ...
#$ girls: int  4683 4457 4102 4590 4839 4820 4928 4605 4457 4952 ...

summary(arbuthnot)
#year           boys          girls     
#Min.   :1629   Min.   :2890   Min.   :2722  
#1st Qu.:1649   1st Qu.:4759   1st Qu.:4457  
#Median :1670   Median :6073   Median :5718  
#Mean   :1670   Mean   :5907   Mean   :5535  
#3rd Qu.:1690   3rd Qu.:7576   3rd Qu.:7150  
#Max.   :1710   Max.   :8426   Max.   :7779

arbuthnot$boys
#[1] 5218 4858 4422 4994 5158 5035 5106 4917 4703 5359 5366 5518 5470 5460 4793 4107 4047 3768 3796
#[20] 3363 3079 2890 3231 3220 3196 3441 3655 3668 3396 3157 3209 3724 4748 5216 5411 6041 5114 4678
#[39] 5616 6073 6506 6278 6449 6443 6073 6113 6058 6552 6423 6568 6247 6548 6822 6909 7577 7575 7484
#[58] 7575 7737 7487 7604 7909 7662 7602 7676 6985 7263 7632 8062 8426 7911 7578 8102 8031 7765 6113
#[77] 8366 7952 8379 8239 7840 7640

str(arbuthnot)
#'data.frame':	82 obs. of  3 variables:
#$ year : int  1629 1630 1631 1632 1633 1634 1635 1636 1637 1638 ...
#$ boys : int  5218 4858 4422 4994 5158 5035 5106 4917 4703 5359 ...
#$ girls: int  4683 4457 4102 4590 4839 4820 4928 4605 4457 4952 ...

summary(arbuthnot$boys)
#Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#2890    4759    6073    5907    7576    8426

name = "srikar"
class(name)
#[1] "character"

class(TRUE)
#[1] "logical"

arbuthnot$girls
#[1] 4683 4457 4102 4590 4839 4820 4928 4605 4457 4952 4784 5332 5200 4910 4617 3997 3919 3395 3536
#[20] 3181 2746 2722 2840 2908 2959 3179 3349 3382 3289 3013 2781 3247 4107 4803 4881 5681 4858 4319
#[39] 5322 5560 5829 5719 6061 6120 5822 5738 5717 5847 6203 6033 6041 6299 6533 6744 7158 7127 7246
#[58] 7119 7214 7101 7167 7302 7392 7316 7483 6647 6713 7229 7767 7626 7452 7061 7514 7656 7683 5738
#[77] 7779 7417 7687 7623 7380 7288

length(arbuthnot$girls)
#[1] 82

sum(arbuthnot$girls)
#[1] 453841

summary(arbuthnot$girls)
#Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
#2722    4457    5718    5535    7150    7779 

arbuthnot[8,2]
#[1] 4917

1:3
#[1] 1 2 3

arbuthnot[c(5,8),1:2]
#  year boys
#5 1633 5158
#8 1636 4917

arbuthnot[c(5,8),]
#  year boys girls
#5 1633 5158  4839
#8 1636 4917  4605

arbuthnot[ 2:5 , 2:3]
#  boys girls
#2 4858  4457
#3 4422  4102
#4 4994  4590
#5 5158  4839

 
plot(x = arbuthnot$year, y = arbuthnot$girls) #Rplot01-Girls_Year.jpeg
plot(x = arbuthnot$year, y = arbuthnot$boys) #Rplot02-Boys_Year.jpeg
plot(x = arbuthnot$year, y = arbuthnot$girls, type = "l", col = "red") #Rplot03-Girls_Year-line-red.jpeg

arbuthnot$total = arbuthnot$girls + arbuthnot$boys
arbuthnot$test = NA

plot(x = arbuthnot$year, y = arbuthnot$total, type="l", xlab ="Year", ylab="count") #Rplot04-TotalCount_Year-line-xylabeled.jpeg



#Based on the assignment for Lab1 instructions on Canvas: 
  
#"Line plot of the boys, girls and total all on the same plot and in separate color.  Do not forget the Title, axes labels, and Chart legend."

#Here's the following script to get the requested plot: 

plot(x = arbuthnot$year, y = arbuthnot$total, type = "l", col = "green", ylim = c(0, max(arbuthnot$total)),
     main = "Number of Baptisms over years by gender and total",
     xlab = "Year",
     ylab = "Number of Baptisms")
lines(arbuthnot$year, arbuthnot$boys, col = "blue")
lines(arbuthnot$year, arbuthnot$girls, col = "pink")
legend("bottomright", legend = c("Boys", "Girls", "Total"), col = c("blue", "pink", "green"), lty = 1)
#Rplot05-Total_Girls_Boys.jpeg




