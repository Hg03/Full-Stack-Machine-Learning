# Full stack Machine Learning Project 🎰 🚀

![img](https://ml-ops.org/img/ml-engineering.jpg)

image taken from [ml-ops.org](https://ml-ops.org/)

# Steps involved 📶 📶

## Step 1 ⤵️

- Firstly we'll create our github repository and clone or connect it with our local environment so that we can work locally as well. 
- Try to make commits from your local to repository / don't do on github directly because it's not a good practice ❌❌
- This is important step to being comfortable for industry level projects

## Step 2 ⤵️

- If we are going to productionize our Machine learning application means applying **MLOps** concepts to the model like  data ingestion, data transformation, model building, continuous integration, continuous deployment, packaging the model, serving as API, updating the model versions. SO about the whole application, we should define the version, author name etc. For this **setup.py** file comes in handy.
- **setup.py** file is very crucial file if we are packaging our application and deploy it on **pypi** or somewhere else.
- This file includes the **author name**, **organization name**, **repository link**, **required libraries**, **version updates**, **current versions** and many more like these things.
- To know more about **setup.py** file, check this [blog](https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/).

## Step 3 ⤵️

- Now after step 2, we should aware of the general folder template to test and build a machine learning project. One folder we have that is **components** which consists all ML operations like **data ingestion**, **data transformation**, **model monitoring** and **model trainer**. Second folder is **pipelines** which consists **training pipeline** and **prediction pipeline**.
- So for this much files, we don't need to create it everytime, we should automate this step and for this, we'll create **template.py** file which consists a pythonic code which is automatically create the folders and files inside that and leave the already existing file. Have a look at the file in this repository.

## Step 4 ⤵️

- After getting a decent folder structure, another thing we need is to track all our errors and logs of processes stored in a file named **logfile**.
- It is important to store the logs so that we can tract and update the code as we move ahead.
- For this, create two files **logger.py** and **exception.py**, view the file also.

## Step 5 ⤵️

- Now let's ingest the data from database .

