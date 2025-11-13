Состав репозитория Docker:
Пациенты.xlsx — база данных с исходной информацией,
run_analysis.R — основной R-скрипт для анализа данных,
Dockerfile — инструкция по созданию образа контейнера,
Result/ — директория для итогового csv файла (анализ_гемоглобина.csv).


run_analysis.R содержит следующий код:
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
# Сохранение результата в CSV в папку Result
write.csv(final_result, file = "Result/анализ_гемоглобина.csv", row.names = FALSE)

Dockerfile содержит следующий код:
FROM rocker/r-base:latest
RUN apt-get update && apt-get install -y libxml2-dev libcurl4-openssl-dev libssl-dev
RUN R -e "install.packages('readxl', repos='https://cloud.r-project.org')"
WORKDIR /app
RUN mkdir /app/Result
COPY run_analysis.R /app/run_analysis.R
COPY Пациенты.xlsx /app/Пациенты.xlsx
CMD ["Rscript", "/app/run_analysis.R"]


Для создания Docker-образ использован код:
bash
docker build -t hemoglobin-analyze .

Для запуска контейнер с монтированием папки Result использован код:
bash
docker run --rm -v $(pwd)/Result:/app/Result hemoglobin-analyze



