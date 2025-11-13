library(readxl)

# Загрузка данных
patients <- read_excel("./Пациенты.xlsx")

# Обработка переменной Пол
patients$Пол <- toupper(patients$Пол)
patients$Пол <- factor(patients$Пол, levels = c("М", "Ж"))

# Создание возрастных групп
patients$возраст_группа <- cut(patients$Возраст,
                               breaks = c(0, 60, 100),
                               labels = c("0-60","61-100"))

# Расчет среднего и стандартного отклонения для гемоглобина по возрастным группам
final_result <- aggregate(гемоглобин ~ возраст_группа, data = patients,
                          FUN = function(x) c(Mean = mean(x), SD = sd(x)))
final_result <- do.call(data.frame, final_result)
colnames(final_result) <- c("Возрастная группа", "Среднее значение", "Стандартное отклонение")

# Создание папки для результатов
if (!dir.exists("Result")) {
  dir.create("Result")
}

# Сохранение результата в CSV в папку output
write.csv(final_result, file = "Result/анализ_гемоглобина.csv", row.names = FALSE)
