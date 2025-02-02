import os
from ruamel.yaml import YAML
from elliot.run import run_experiment
import pandas as pd


def sample_datasets(random_state):
    df = pd.read_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/amazon_music/dataset copy.tsv", sep = "\t")
    df = df.sample(frac = 0.65, random_state=random_state)
    df.to_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/amazon_music/dataset.tsv", index=False, sep="\t")
    df = pd.read_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/movielens_1m/dataset copy.tsv", sep = "\t")
    df = df.sample(frac = 0.09, random_state=random_state)
    df.to_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/movielens_1m/dataset.tsv", index=False, sep="\t")
    df = pd.read_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/epinions/dataset copy.tsv", sep = "\t")
    df = df.sample(frac = 0.12, random_state=random_state)
    df.to_csv("/data/raid5/data/maximilian_hess/RecSys2023_hyperparameter_tuning/data/epinions/dataset.tsv", index=False, sep="\t")

yaml_file = "config_files/Untuned_amazon.yml"

base_path = "./"
num_configs = 30
yaml = YAML()
yaml.allow_duplicate_keys = True
with open(yaml_file, "r") as file:
    data = yaml.load(file)

for i in range(1, num_configs + 1):

# Create a unique suffix for each configuration

    run_suffix = f"Untuned_amazon/run_{i}"
    # Dynamically update paths in the 'experiment' section

    sample_datasets(random_state = i)

    data["experiment"]["path_output_rec_result"] = os.path.join(base_path, f"results/{run_suffix}")
    data["experiment"]["path_output_rec_weight"] = os.path.join(base_path, f"weights/{run_suffix}")
    data["experiment"]["path_output_rec_performance"] = os.path.join(base_path, f"performance/{run_suffix}")
    data["experiment"]["path_log_folder"] = os.path.join(base_path, f"logs/{run_suffix}")

    with open(yaml_file, "w") as outfile:
        yaml.dump(data, outfile)

    run_experiment("config_files/Untuned_amazon.yml")




