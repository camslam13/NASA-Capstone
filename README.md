# NASA-Capstone

This is a testing repo to get familiar with image recognition. It does not work 100% but a good start. Please clone this repo so the code does not get messed up with any changes. 

## Install
You will need the following things:

* Conda(optional but makes everything easier.)
  You can install anaconda here: [Download Anaconda](https://www.anaconda.com/products/distribution)
  
* Python version 3.8.18
* Tensorflow(can download through pip 2.x and higher gives you most of the other imports you need *Don't download keras if you have tensorflow 2.x or higher will cause probelms)
* scipy(can download through pip)
* Pillow(can download through pip)
* jupyter(in the extensions within vscode)

  ## How to use
  * If you are using conda you'll want to create an env. You can do this by

  conda create --name <environment_name> python=<python_version>

  * You can activate the env by typing "conda activate nameOfEnv".

  * Then you will want to select a python interpreter within vscode can do ctrl+shift+p.(if you created an env it should pop up there)

  * Within the JupyterNotbook you'll want to select the kernel as the one you created.

  * The two ipynb files are the actual code of the model and the tester.

  * The trainModel is where we load our datasets into the model to train it on what is a 
  rock vs sand. 

  * The testModel is where you can test an image to see if it comes back as rock or 
    sand. Just update the path to image under the load a test image method. 

  *  myModel.h5 is the actual trained model after you run trainModel there is a save   
     statement that saves it as a certain name. 
  
