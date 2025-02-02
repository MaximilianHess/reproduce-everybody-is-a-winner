

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

<p>Change to the <em>"hyperparameter_tuning"</em> directory and run this line to install the required packages</p>
<pre>
  pip install -r requirements.txt
</pre>

We added the package `ruamel.yaml` to `requirements.txt` as it is required for our experiments. No other package versions from the original environment were changed.  

The `reproducibility.py` file contains the code to conduct our experiments. By default, it runs the untuned configuration 30 times on the Amazon dataset.  


### Running the t-test Notebook  

The **`ttests_untuned_results.ipynb`** notebook contains the code for running the t-test on the experiment results. Since we wanted to minimize interference with the original Elliot environment, you will need a separate environment to run it.  

First, create and activate a simple virtual environment:  

```bash
python -m venv ttest_env
source ttest_env/bin/activate
```

Install the required dependencies in the new environment:  

```bash
pip install -r ttest_requirements.txt
```

Once the environment is set up, open the Jupyter Notebook and run `ttests_untuned_results.ipynb`


### What is not included in the repo

Due to storage constraints we did not include the results file created by Elliot which contains the predictions of the models. However we included the individual performance files from each run which enable 