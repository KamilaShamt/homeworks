FROM r-base:latest

# установка dplyr
RUN R -e "install.packages('dplyr', repos='https://cloud.r-project.org')"

# скопировать R скрипт внутрь образа
COPY join.R /app/join.R

WORKDIR /app

# выполнение скрипта
CMD R -e "cat('dplyr version: ', as.character(packageVersion('dplyr')), '\n')" \
    && Rscript /app/join.R