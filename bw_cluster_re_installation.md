# Running RE Simulation on the BwUniCluster 2.0

The following tutorial describes all steps that are needed to run RE simulations on the [BwUniCluster 2.0](https://wiki.bwhpc.de/e/Category:BwUniCluster_2.0).

The steps are:

1. Getting access to the cluster.
2. Installation of Anaconda in your home directory of the cluster.
3. Setting up ssh 
4. 

This procedure has been tested with Anaconda3 on a Red Hat Enterprise Linux 8.2.

## 1. Getting access to the cluster

See <https://wiki.bwhpc.de/e/BwUniCluster_2.0_User_Access>.

## 2. Installation of Anaconda

While there is a preinstalled python on the cluster, it has some advantages to use your own python. In this way you have full control over installed packages. There are different possibilities to set up a python distribution. Here, we us [Anaconda](https://www.anaconda.com), a package repository for python. 

1. [Login to the cluster](https://wiki.bwhpc.de/e/BwUniCluster_2.0_User_Access#Login).
2. Download the install package: `wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
` (The version and address might differ in the future. Additionally, you have to make sure to use the file that fits the operating system on the cluster.) 
2. Install the package: `bash Anaconda3-2021.11-Linux-x86_64.sh` (this installs anaconda in your home directory).
3. After installing you might have to, first, init the conda package by `conda init <SHELL_NAME>` (e.g. `conda init bash` on the cluster), possibly from the bin-directory of anaconda) and, second, to reload your shell init script (e.g. reloading `<home>/.bashrc` by `source ~/.bashrc` one the cluster). Now you should be able to execute anaconda commands.

### Anaconda in a nutshell^[See [here](https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533#5193) for further details.]:
   
+ Anaconda allows you to install different python environments and to install packages into these different environments. By default the anaconda installation comes with an environment that is named `base`. 
+ The different environments can  be activated by `conda activate <ENV-NAME>`.
+ You can check whether everything works as expected by, first, activating the `base` environment and than check with `which python`, whether the python of your anaconda is active (the command should echo something like `<YOUR-HOME-DIR>/anaconda3/bin/python`.
+ You can create additional environments with `conda create`. For instance, `conda create -n py38 python=3.8` will create a python environment of version 3.8 with the name `py38` into `<ANACONDA-HOME>/envs/`. (You can list all installed environments with `conda env list`.)
+ You can remove an environment with `conda env remove -n <ENV_NAME>`. (This is not possible if the environment you wish to remove is active. This will delete the full directory containing the environment.)
+ You can install packages **into the currently active environment** from the anaconda repository (e.g. by `conda install <PACKAGE-NAME>`) or with the python package manager pip from PyPI (e.g. by `pip install <PACKAGE-NAME>`). 

## 3. Setting up ssh for installing the Python RE packages

In order to install the RE packages we have to configure ssh for the authentication on github. (I had to use a slightly different approach than the one described in the [github docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)):

1. Create a directory `.ssh` (if there isn't one already): `mkdir .ssh`.
2. Change to that directory: `cd .ssh`
3. Create key pairs: `ssh-keygen -C "<YOUR-EMAIL>"`
4. Create a config file: `touch config`.
5. Add the following lines to this file by either using some of the available editors (e.g. emacs, vim) or by copying a locally created file to the server (by using `scp` or [FileZilla](https://wiki.bwhpc.de/e/BwUniCluster_2.0_User_Access#Client_application:_FileZilla)) or by using command line commands (see e.g. [here](https://indico.scc.kit.edu/event/278/attachments/978/1384/03_2017-04-05_bwHPC_course_-_linux_intro.pdf) on page 10).

```
Host github.com 
    HostName github.com
    IdentityFile ~/.ssh/<NAME-OF-PRIVATE-KEY>
    User <YOUR-GITHUB-USERNAME>
```
6. Copy your public key to your github account (as described [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)).
7. Test your ssh-connection with `ssh -T git@github.com`

## 4. Installing the RE python packages

1. Activate the anaconda environment where you want to install the packages: `conda activate <ENV-NAME>`.
2. Install the python package with `pip` from github: 
  + `pip install git+ssh://git@github.com/debatelab/re-python.git`
  + `pip install git+ssh://git@github.com/debatelab/re-model-description.git`
3. If you want to update these with newer version from github, reinstall them by, first, deleting the packages (`pip uninstall remodeldescription` and `pip uninstall rethon`) before installing them anew.

## 5. Starting simulations

To run you simulations you have to use the [slurm workload manager](https://wiki.bwhpc.de/e/BwUniCluster_2.0_Slurm_common_Features). There are different possibilities to initiate these jobs. For instance, you can put the python code you want to execute into a python script and specify all necessary parameters for slurm into a shell script, which additionally executes the python script. This batch script should be given to the slurm manager by using `sbatch`.

E.g. the bash script could look like the following:

```bash
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --time=4
#SBATCH --mem=100
#SBATCH --job-name=test_re
#SBATCH --mail-user=sebastian.cacean@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --output=/home/kit/itz/ii8929/re_simulations/test/output.txt
#SBATCH --error=/home/kit/itz/ii8929/re_simulations/test/error.txt

# init conda
# Background: There seem to be some problem of using conda via the slurm manager. The error log
# nags about the lack of a proper initialization of conda. Apparently, whatever is initialized via
# `~/.bashrc` is not given to the subshell that is created by `sbatch` 
# (<https://stackoverflow.com/questions/55507519/python-activate-conda-env-through-shell-script#55507956>).
# I simply c&p-ed the corresponding files of `~/.bashrc` into this scripts.

__conda_setup="$('/home/kit/itz/ii8929/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kit/itz/ii8929/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kit/itz/ii8929/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kit/itz/ii8929/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup

# activting conda env
conda activate py38
# executing python script
python <YOUR-PYTHON-SCRIPT.py
```

And can be given to slurm e.g. with `sbatch --partition=<PARTITION-NAME> <SCRIPTNAME>`.
