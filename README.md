### EduPapersAPI
EduPapersAPI is a Django-based RESTful API which functions as the project's backend infrastructure.


There are two main ways to contribute to this project:<br>
1: **Suggest features or functionality in the discussions:**
 - Navigate to the discussions tab at the organization level by following [this link](https://github.com/orgs/EduPapersKe/discussions).
 - In the discussions tab, choose the category of suggestion between "New feature" and "Feature implementation."
 - Create a discussion by tagging any of the organization administrators followed by your suggestion.

2: **Contribute by writing code:**
 - Fork and/or clone the repository, make changes, commit signed-off changes(otherwise the pr can't be merged), create a branch for each change, and open a pull request targeting the development branch. Optionally, you can request a review on your commits from an admin of your choice when creating a pull request.
 - Your changes will be reviewed and the necessary steps taken.
 - Please note that changes made from unapproved suggestions or not-signed commits will not be approved. This is to avoid over-complicating things as well as maintain consistency and prevent feature conflicts.
 - Before contributing to this project, make sure you understand how it works.
  

### How to?
<<<<<<< HEAD
[Take me to the documentation](https://github.com/EduPapersKe/EduPapersAPI/blob/master/contributing.md).<br>
=======
[Take me to the documentation](https://www.postman.com/mwangi-brian/workspace/edupaperske/overview).<br>
>>>>>>> bafeca7fa5166c2fd66f8ccd6570e5dd1aa17f20

Running the project locally

#### Clone the Repository
1: Open your command prompt or terminal.<br>
2: Navigate to your preferred directory and clone the repository using the following command:
  ```Bash
  git clone https://github.com/EduPapersKe/EduPapersAPI.git
  ```
#### Set up Virtual Environment
3: Navigate into the project root directory named EduPapersAPI:
   ```Bash
   cd EduPapersAPI
   ```
4: Create a virtual environment and activate it following the instructions for your operating system (Windows or Linux/macOS).
 - For Windows:
   ```Bash
   python -m venv <virtual-env-name>
   ```
 - For Linux/MacOs:
   ```Bash
   python3 -m venv <virtual-env-name>
   ```
5: Activate the virtual environment with this command:
 - For Windows:
   ```Bash
   <virtual-env-name>\Scripts\activate.bat
   ```
 - For Linux/MacOs:
   ```Bash
   source/<virtual-env-name>/scripts/activate.bat
   ```
6: Install project dependencies using the following command:
 - For Windows:
   ```Bash
   pip install -r requirements.txt
   ```
 - For Linux/MacOs:
   ```Bash
   pip3 install -r requirements.txt
   ```
#### Configure Environment Variables
7: Create a new file in the root directory and name it *```.env```*. **Note:** The ```.env``` file should not be committed to version control. Copy the contents from *```.env.example```* and assign the fields the necessary secrets.
#### Database Migrations
8: Run the following commands to create and apply database migrations:
  ```Bash
   python manage.py makemigrations
  ```
  ```Bash
   python manage.py migrate
  ```
#### Start the Development Server
9: Run the application with this command:
  ```Bash
   python manage.py runserver
  ```

<<<<<<< HEAD
##### With that out of the way, you can proceed to the [docs](https://github.com/EduPapersKe/EduPapersAPI/blob/master/contributing.md).
=======

##### With that out of the way, you can proceed to the [docs](https://www.postman.com/mwangi-brian/workspace/edupaperske/overview).
>>>>>>> bafeca7fa5166c2fd66f8ccd6570e5dd1aa17f20
