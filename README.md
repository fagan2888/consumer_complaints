# Consumer Complaints

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. 

Compute for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Repo directory structure
The top-level directory structure for your repo should look like the following: (So that we can grade your submission, replicate this directory structure at the top-most level of your project repository. Do not place the structure in a subdirectory)

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── complaints.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── complaints.csv
                |── output
                    └── report.csv
