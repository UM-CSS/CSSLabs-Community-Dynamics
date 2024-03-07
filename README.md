# User Guide for CSS Community Dynamics Lab Notebooks

## Contents
0. [Getting the Code and Data](#download)
1. [Enviornment Setup](#setup)
2. [Using Lab Exercises](use)
    - [Short Summaries of each Lab](#summary)
    - [Lab 0: Intro to Reddit data and trends](#zero)
    - [Lab 1: Evolving community dynamics](#one)
    - [Lab 2: Other Shocks to Communities](#two)
4. [Suggested Readings](#readings)
5. [License](#license)    

## 0. Getting the Code and Data <a name="download"></a>
To use these labs, you will need to download the code and the data. 

#### Instructions
- Go to this link: https://github.com/UM-CSS/CSSLabs_Community_Dynamics
- If you are familiar with `git`, we recommend you clone the repo.
- If you are unfamiliar with `git`, the easiest option is to follow these steps:
    - Press the ![Clone or download](images/clone_or_download.png "Clone or download") button on the right side of each repository.
    - Choose `Download ZIP` and save the file somewhere memorable.
    - Go to where the file is saved and unzip it.

## 1. Environment Setup <a name="setup"></a>
You will need some software to be able to run this code. We recommend the following:
1. Install [Docker Desktop](https://docs.docker.com/desktop/) on the laptop or desktop computer.  Here are direct links for various operating systems: [Mac OS](https://docs.docker.com/desktop/install/mac-install/), [Windows](https://docs.docker.com/desktop/install/windows-install/), [Linux](https://docs.docker.com/desktop/install/linux-install/). 
2. We are using [Jupyter notebook on Docker Stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/) to avoid steps to install various components. With the Docker Desktop installed in above step, now we can load a docker container directly by:
    - Open a terminal on Mac OS or the Commandline Prompt on Windows, and **navigate to the folder where you downloaded the notebook in step 0**.

        - If you are a Mac user, run the following command:
        ```bash
        docker run -v $(pwd):/home/jovyan/CSSLabs-Community-Dynamics -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```

        - If you are a Windows Command shell user, use this command:
        ```bash
        docker run -v %cd%:/home/jovyan/CSSLabs-Community-Dynamics -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```

        - If you are a Windows PowerShell user, use the following command:
        ```bash
        docker run -v ${PWD}:/home/jovyan/CSSLabs-Community-Dynamics -p 8888:8888 quay.io/jupyter/scipy-notebook:2024-01-05
        ```
    
    - The above step will first pulling the docker container from the remote repository.  You should see a list of layers of this container being pulled off the remote repo. Notice, the image pulling steps only happens when this is done for the first time.  Once the pulling is completed, it will run the container on your local operating system, and expose a port 8888 on your local host, with a token, i.e. ```b045...61e4``` in the following case.  

    ```
    ...
    aef40af6dc3e: Pull complete 
    3c01e088ac39: Pull complete 
    Digest: sha256:162744a05b15a0bcad1064238af48b0e4e6bcb56f1e4cc607f34343ee3a0f728
    Status: Downloaded newer image for quay.io/jupyter/scipy-notebook:2024-01-05
    Entered start.sh with args: jupyter lab
    Running hooks in: /usr/local/bin/start-notebook.d as uid: 1000 gid: 100

    ...

    [I 2024-01-05 21:07:36.315 ServerApp] Serving notebooks from local directory: /home/jovyan
    [I 2024-01-05 21:07:36.315 ServerApp] Jupyter Server 2.12.2 is running at:
    [I 2024-01-05 21:07:36.315 ServerApp] http://bda4c6f01885:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    [I 2024-01-05 21:07:36.315 ServerApp]     http://127.0.0.1:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    [I 2024-01-05 21:07:36.315 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 2024-01-05 21:07:36.317 ServerApp] 
        
        To access the server, open this file in a browser:
            file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
        Or copy and paste one of these URLs:
            http://bda4c6f01885:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
            http://127.0.0.1:8888/lab?token=b045793e8e725f79808eb241136cf80294ba94d86c8f61e4
    ```

3. If you see the above terminal completed with above output and waiting for input, congratulations! you have successfully installed docker container that  you need. If not, there is something wrong with your installation, and please ask one of the instructors for help.  Use a web browser to access the above URL with the token from your local machine, i.e. you have to copy the similar string from your output with your TOKEN string and replace following one. If not, you might be given a prompt to copy/paste the token on the first webpage. 
    ```
    http://127.0.0.1:8888/lab?token=xxx
    ```

4. In the jupyter lab environment we have created above, you should see a list of files and folders on the left of the webpage, and Notebook, Console, and Others to the right side of the page. Navigate through the left file browser to the `CSSLabs-Community-Dynamics` folder.  In this folder is a list of lab files ending in `.ipynb`, stands for Interactive (i) Python (py) Notebook (nb). Click on any of these and they should open in a new Notebook tab with the lab code and instructions.
    - **Note** if you get an error or the top of the new page does not look like this 
        - ![notebook top](images/notebook_top.png "notebook top"), 
        - Then you have probably made a mistake in downloading the files. Go back to the "[Getting the Code and Data](#download)" instructions. 
5. If you are new to Jupyter Notebooks, everything you need for these labs is in the great [introduction to their basic use](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb).


## 2. Using Lab Exercises <a name="use"></a>
**N.B.** Students will understand this lab better if they have already completed the NLP labs, which teach how to work with and think about text data in python. The NLP labs are *not* required prerequisites.

### Short Summaries of each Lab <a name="summary"></a>
- Lab 0 introduces students to reddit data and thinking about trends over time.
- Lab 1 explores changing community dynamics using the r/TwoXChromosomes controversy.
- Lab 2 investigates the impact on Reddit communities following their designation as default subreddits, analyzing changes in activity and community dynamics.
 
### Lab 0: Intro to Reddit Data <a name="zero"></a>

### Lab 1: Evolution of Community Norms <a name="one"></a>

### Lab 2: Other Shocks to Communities <a name="two"></a>



## Suggested Readings <a name="readings"></a>

#### Popular and short writing
- Hern, Alex. 2014. "[Reddit women protest at new front-page position](https://www.theguardian.com/technology/2014/may/13/reddit-women-protest-front-page-subforum-subreddit-position)." *The Guardian*, 13 May.

#### Academic publications
- Palmer, Alexis, Melissa Robinson, and Kristy Philips. 2017. “[Illegal Is Not a Noun: Linguistic Form for Detection of Pejorative Nominalizations](http://www.aclweb.org/anthology/W17-3014).” Pp. 91–100 in *Proceedings of the First Workshop on Abusive Language Online.* Vancouver.
- Danescu-Niculescu-Mizil, Cristian, et al. 2013. "[A computational approach to politeness with application to social factors](https://www.cs.cornell.edu/~cristian/Politeness.html)." *Proceedings of ACL*.
- Chandrasekharan, Eshwar. 2017. "[You Can't Stay Here: The Efficacy of Reddit's 2015 Ban Examined Through Hate Speech](https://dl.acm.org/citation.cfm?id=3171581.3134666)." *Proceedings of the ACM on Human-Computer Interaction*, Volume 1 Issue CSCW. 


## License <a name="license"></a> 
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).














