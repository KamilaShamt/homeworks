#install.packages("readxl")
#getwd() 
library(readxl) 
patients <- read_excel("./common/Пациенты.xlsx")
head(patients)
summary(patients)
dim(patients)
str(patients)
patients$Пол <- toupper(patients$Пол)
patients$Пол <- factor(patients$Пол, levels = c("М", "Ж"))
str(patients)
levels(patients$Пол)
patients$гемоглобин[c(2,4,10)]<-NA
patients$настроение<-NA
sum(is.na(patients))
which(is.na(patients$гемоглобин))
which(is.na(patients$настроение))
patients[is.na(patients$гемоглобин), ]
patients$настроение <- NULL
patients_clean <- na.omit(patients)

patients$гемоглобин[is.na(patients$гемоглобин)]  <- median(
  patients$гемоглобин, na.rm = TRUE)


write.csv(result, "result.csv")