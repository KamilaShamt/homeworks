install.packages("httr")
install.packages("jsonlite")


#10. (R): Получите информацию о 10 белках разной длины. Постройте в R столбчатую диаграмму (barplot), отображающую длину каждого белка.

library(httr); library(jsonlite)

u <- GET("https://rest.uniprot.org/uniprotkb/search",
         query = list(query = "organism_id:9606", format="json", size=10))
j <- fromJSON(content(u, "text"), flatten = TRUE)

acc <- j$results$primaryAccession
len <- as.integer(j$results$sequence.length)

names(len) <- acc

par(mar=c(8,5,4,2))
barplot(len, las=2, main="Длины первых 10 белков (Homo sapiens)", ylab="Длина, aa", cex.names=0.8)
print(data.frame(accession=acc, length=len))

#13. (R): Сделайте запрос к Proteins API, чтобы получить данные о белке в формате FASTA. Сохраните результат в файл с расширением .fasta

library(httr)

acc <- "P04637"  
r <- GET(paste0("https://www.ebi.ac.uk/proteins/api/proteins/", acc),
         add_headers(Accept = "text/x-fasta"))
writeLines(content(r, "text", encoding="UTF-8"), paste0(acc, ".fasta"))
