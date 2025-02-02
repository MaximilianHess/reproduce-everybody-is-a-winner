

### Running the experiments
Run the following command to create <em>"elliot_env"</em> environment</li>

</p>
<pre>
 conda create --name elliot_env python=3.8
</pre>

<p>Activate the conda environment</p>
<pre>
  conda activate elliot_env
</pre>
Then run
<pre>
  pip install -r requirements.txt
</pre>

We added the package `ruamel.yaml` to `requirements.txt` as it is required for our experiments. No other package versions from the original environment were changed.  

The  `reproduce_untuned.py` file contains the code to conduct our experiments for the untuned models. By default, it runs the untuned configuration 30 times on the Amazon dataset. To change the dataset the file has to edited manually and another config file has to be selected.

The tuned config files were run with the original code from the authors, `reproducibility_original.py`, in which the path to config file has to be modified manually.


### Running the t-test Notebook  

The **`ttests_untuned_results.ipynb`** notebook contains the code for running the t-test on the experiment results. Since we wanted to minimize interference with the original Elliot environment, you will need a separate environment to run it.  

First, create and activate a simple virtual environment. It was created and tested with Python 3.12.5:  

```bash
python -m venv ttest_env
source ttest_env/bin/activate # MacOS/Linux
ttest_env\Scripts\activate #Windows
```

Install the required dependencies in the new environment:  

```bash
pip install -r requirements-ttest.txt
```

Once the environment is set up, open the Jupyter Notebook and run `ttests_untuned_results.ipynb`


### What is Not Included in the Repository

Due to storage constraints, we did not include the `results` and `weights` (which was empty either way) folders. This means that the files created by Elliot containing the model predictions are not included. However, we have included the individual performance files from each run in the `performance` folder.


