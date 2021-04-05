FROM  continuumio/miniconda3
LABEL Author, Etienne Lamare

ENV APP_HOME /Environnement_Retrieve_Luis_intent_and_simple_testing
WORKDIR $APP_HOME
COPY . $APP_HOME

#---------------- Prepare the envirennment
RUN conda update --name base conda &&\
    conda env create --file environment.yaml
SHELL ["conda", "run", "--name", "Environnement_Retrieve_Luis_intent_and_simple_testing", "/bin/bash", "-c"]

ENTRYPOINT ["conda", "run", "--name", "Environnement_Retrieve_Luis_intent_and_simple_testing", "python", "main.py"]