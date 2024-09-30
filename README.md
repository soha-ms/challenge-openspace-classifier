# challenge-openspace-classifier
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 🏢 Description

Your company moved to a new office at the Gent Zuiderport. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues. 

This script runs everyday to re-assign everybody to a new seat.
Assign random lead ro each table
![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

## 📦 Repo structure

```
.
├── /utils
│   ├── openspace.py
│   ├── table.py
│   └── utils.py
├── .gitignore
├── main.py
├── output.csv ## TO DO
└── README.md

```
## 🛎️ Usage

To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```
# Creates a list that contains all the colleagues names
names = utils.read_names_from_csv(input_filepath) new_colleagues.csv ## Read names from csv file 

# save the seat assigments to a new file
open_space.store(output_filename) ## TO DO 


Connect with me on [LinkedIn](https://www.linkedin.com/in/soha-mohamad-382b44219/).