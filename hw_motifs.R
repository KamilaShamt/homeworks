motifs2 <- matrix(c(
  "a", "C", "g", "G", "T", "A", "A", "t", "t", "C", "a", "G",
  "t", "G", "G", "G", "C", "A", "A", "T", "t", "C", "C", "a",
  "A", "C", "G", "t", "t", "A", "A", "t", "t", "C", "G", "G",
  "T", "G", "C", "G", "G", "G", "A", "t", "t", "C", "C", "C",
  "t", "C", "G", "a", "A", "A", "A", "t", "t", "C", "a", "G",
  "A", "C", "G", "G", "C", "G", "A", "a", "t", "T", "C", "C",
  "T", "C", "G", "t", "G", "A", "A", "t", "t", "a", "C", "G",
  "t", "C", "G", "G", "G", "A", "A", "t", "t", "C", "a", "C",
  "A", "G", "G", "G", "T", "A", "A", "t", "t", "C", "C", "G",
  "t", "C", "G", "G", "A", "A", "A", "a", "t", "C", "a", "C"
), nrow = 10, byrow = TRUE)

# Переводим все буквы в верхний регистр
motifs2 <- apply(motifs2, 2, toupper)

count_matrix <- apply(motifs2, 2, function(col) table(factor(col, levels = c("A", "C", "G", "T"))))
count_matrix

profile_matrix<- apply(count_matrix, 2, function(col) {col / sum(col)})
profile_matrix


scoreMotifs <- function(motifs) {
  motifs <- matrix(toupper(motifs), nrow = nrow(motifs))  # Приводим к верхнему регистру
  sum(apply(motifs, 2, function(col) length(col) - max(table(col))))
}
scoreMotifs(motifs2)


getConsensus <- apply(profile_matrix, 2, function(col) {
  nucleotides <- c("A", "C", "G", "T")
  nucleotides[which.max(col)]
})
consensus_string <- paste(getConsensus, collapse = "")
consensus_string


col1 <- motifs2[, 1]
freqs <- table(factor(col1, levels = c("A", "C", "G", "T")))
barplot(freqs, 
        col = "skyblue", 
        main = "Частоты нуклеотидов в 1-м столбце",
        xlab = "Нуклеотид",
        ylab = "Частота")
