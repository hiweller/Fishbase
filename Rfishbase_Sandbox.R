setwd('/Users/hannah/Dropbox/Westneat Lab/OpenCV Sandbox/')
library('rfishbase')

lethrinids <- read.csv('lethrinid_test.csv')
speciesnames <- lethrinids$Scientific.Name
fbdata <- species(speciesnames)
fbdata$PicPreferredName
fbdata$PicPreferredNameM
fbdata$PicPreferredNameF
fbdata$PicPreferredNameJ
pics <- list_fields('Pic')
merge(fbdata, pics)
