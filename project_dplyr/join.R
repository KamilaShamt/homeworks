library(dplyr)

# Загрузка данных
sample_metadata <- read.csv("data/sample_metadata.csv")
mass_spec_results <- read.csv("data/mass_spec_results.csv")

# Anti left join (только из левой, которых нет в правой)
anti_left <- anti_join(sample_metadata, mass_spec_results, by = "sample_id")
write.csv(anti_left, "data/anti_left.csv", row.names = FALSE)

# Anti right join (только из правой, которых нет в левой)
anti_right <- anti_join(mass_spec_results, sample_metadata, by = "sample_id")
write.csv(anti_right, "data/anti_right.csv", row.names = FALSE)

# Anti outer join (уникальные для каждой стороны образцы)
anti_outer <- bind_rows(anti_left, anti_right)
write.csv(anti_outer, "data/anti_outer.csv", row.names = FALSE)