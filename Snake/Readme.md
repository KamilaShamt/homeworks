
# сборка образа

docker build -t ms-pipeline .


# запуск пайплайна

docker run --rm -v "$PWD":/workflow ms-pipeline


# команды для графов

snakemake --rulegraph | dot -Tpng > rulegraph.png
snakemake --filegraph | dot -Tpng > filegraph.png