# User Guide for CSS Community Dynamics Lab Notebooks

## Contents
0. [Getting the Code and Data](#download)
1. [Enviornment Setup](#setup)
2. [Using Lab Exercises](use)
    - [Short Summaries of each Lab](#summary)
    - [Lab 0: Intro to python & text](#zero)
    - [Lab 1: Data munging](#one)
3. [Suggested Readings](#readings)
4. [License](#license)    

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
1. Download Anaconda version 3.6 or later from [this link](https://www.anaconda.com/download/).
    - Anaconda is an "installer" or "package manager" for python. It installs many of the tools, packages, and libraries that are commonly used in python data analysis. It can also be used to install and update additional packages. It is particularly nice because it makes sure that everything works together, which can be hard to do when installing each thing separately. 
2. Install Anaconda on your computer (there are instructions on their website if you have difficulty).
3. Once Anaconda is installed, you should be able to start the programs it includes just like you would start other programs. Test this now:
    - Search for a program called `anaconda navigator` and launch it. When it opens, you should see the option to launch `jupyter notebook`.
        - Alternatively, you can often search for `jupyter notebook` and launch that directly 
    - When jupyter launches, two things will happen:
        1. A terminal / command prompt will open. Do not close this: jupyter is running your code here. You can, however, safely ignore or minimize this window.
        2. A new tab or window should open in your browser with something like this in the top left: 
            - ![notebook home](images/notebook_home.png "notebook home") 
            - If you see this, congratulations: you have successfully installed everything you need. If not, there is something wrong with your installation.
4. In the jupyter notebook tab, you should see a list of files and folders on your computer. Navigate through these folders to the `CSSLabs_Community_Dynamics` folder.
    - **Note** if you do not see this folder, it may be that you saved it somewhere jupyter cannot get to. The easiest solution is to move it to somewhere jupyter can see, such as "my documents." 
5. In this folder is a list of labs, each ending in `.ipynb`. Click any of these and they should open in a new tab with the lab code and instructions.
    - **Note** if you get an error or the top of the new page does not look like this 
        - ![notebook top](images/notebook_top.png "notebook top"), 
        - Then you have probably made a mistake in downloading the files. Go back to the "[Getting the Code and Data](#download)" instructions. 
6. If you are new to Jupyter Notebooks, everything you need for these labs is in the great [introduction to their basic use](http://nbviewer.jupyter.org/github/jupyter/notebook/blob/master/docs/source/examples/Notebook/Notebook%20Basics.ipynb).
7. **Optional notebook extensions**: The labs were designed to work with the `collapsible headings` extension. They work fine without it, but look a little nicer if you have it installed. Full installation instructions are [at the bottom of this link](https://github.com/ipython-contrib/jupyter_contrib_nbextensions). Here's the short version:
    1. In `anaconda prompt` or your terminal, run this command: `conda install -c conda-forge jupyter_contrib_nbextensions`
    2. In the same prompt, run `jupyter nbextensions_configurator enable`
    3. In the same prompt, run `jupyter nbextension enable collapsible_headings/main`
    2. Restart Jupyter Notebook.


## 2. Using Lab Exercises <a name="use"></a>
**N.B.** Students will understand this lab better if they have already completed the NLP labs, which teach how to work with and think about text data in python. The NLP labs are *not* required prerequisites.

### Short Summaries of each Lab <a name="summary"></a>
- Lab 0 introduces students to reddit data and thinking about trends over time.
- Lab 1 explores changing community dynamics using the r/TwoXChromosomes controversy.

### Lab 0: Intro to reddit data <a name="zero"></a>
- 

### Lab 1: Data munging <a name="one"></a>
-

## Suggested Readings <a name="readings"></a>

#### Popular and short writing
- Hern, Alex. 2014. "[Reddit women protest at new front-page position](https://www.theguardian.com/technology/2014/may/13/reddit-women-protest-front-page-subforum-subreddit-position)." *The Guardian*, 13 May.

#### Academic publications
- Palmer, Alexis, Melissa Robinson, and Kristy Philips. 2017. “[Illegal Is Not a Noun: Linguistic Form for Detection of Pejorative Nominalizations](http://www.aclweb.org/anthology/W17-3014).” Pp. 91–100 in *Proceedings of the First Workshop on Abusive Language Online.* Vancouver.
- anescu-Niculescu-Mizil, Cristian, et al. 2013. "[A computational approach to politeness with application to social factors](https://www.cs.cornell.edu/~cristian/Politeness.html)." *Proceedings of ACL*.


## License <a name="license"></a> 
[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nc-nd/4.0/).














