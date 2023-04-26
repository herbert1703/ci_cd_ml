from omegaconf import DictConfig
import papermill as pm
from omegaconf import DictConfig,OmegaConf
import hydra 
import sys
import glob

@hydra.main(
    config_path="../config",
    config_name="main",
)
def run_notebook(config: DictConfig):
    pm.execute_notebook(
        str(config.notebooks.dirinp),
        str(config.notebooks.dirout),
        parameters=dict(columns=list(config.process.features)),
    )

if __name__ == "__main__":
    run_notebook()

