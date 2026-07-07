# Expectations
- Our **MAIN** goal for having you do this exercise is to gain an understanding in how you think and solve problems.
- You are welcome to do this exercise in whatever language you want and we expect you to pick a language that best 
  represents your abilities to solve a problem regardless of what the primary language expectation is for the role you're 
  interviewing for.
- You are not judged on whether or not you "complete" the assignment. We understand that the time constraints for doing the
  exercise are significant, and we want to provide a problem that has _enough_ content for someone to think critically 
  about and not just regurgitate a solution they have recently solved.
- Don't get stuck on one thing for too long. Meaning, if you get hung up on one piece of syntax, just add a comment to the 
  code and move on. 
- You are allowed to "google" for help on things, as that is a skill that all engineers are expected to have in their day to 
  day work.
- We do expect you to produce runnable code.

# Starter Templates

We have included a few starter templates available under `/src/main` if you choose to use Scala, Scala w/ Spark, or Java. 
You are welcome to use any IDE of your choice and if you choose to use any of these templates, the prerequisites and 
provided build files are listed below. 

| Language | Prerequisites | Build File | Template Location |   
| -------- | ------------- | ---------- | ----------------- | 
| Scala    | - JDK8 <br /> - SBT |  `build.sbt` | `/src/main/scala/coding_exercise/ScalaDataPipeline.scala` | 
| Scala w/ Spark | - JDK8 <br /> - SBT |  `build.sbt` | `/src/main/scala/coding_exercise/ScalaSparkDataPipeline.scala` | 
| Java | - JDK8  | `pom.xml` | `/src/main/java/coding_exercise/JavaDataPipeline.java` |

# High Level Assignment Goals

1. Read in a plain text file in csv format and standardize its format
2. Execute some validation checks against the data to determine potential quality issues
3. Run analyses on the data and generate a single resulting dataset

## Goal 1: Convert Source Data to Standard Format

### File 1
**Data Granularity:** Data in this file are at the event granularity, that is to say when a medical event actually occurs. So 
if a person has 100 medical events that happen within a single month, then there will be 1 record(row) per event.

[/src/main/resources/file1.csv](src/main/resources/file1.csv) has the following columns
- member_num
- record_id
- fname
- lname
- dob
- claim_pay_amount
- claim_amount
- date_of_service

### Standard Format
Read in the data from `file1.csv` and standardize it into the following schema:

| Field Name       | Data Type |
| ---------------- |-----------|
| source_member_id | String    |
| claim_id         | String    |
| first_name       | String    |
| last_name        | String    |
| birth_date       | Date      |
| claim_amount     | Decimal   |
| service_date     | Date      |
| paid_amount      | Decimal   |


## Goal 2: Run Validation Checks

After the data from `file1.csv` has been standardized, calculate each field’s “fill rate.” A fields fill rate means what 
percentage of the fields values are non-null. So if the file has 100 records and 90 of those have a value for `last_name`, 
then `last_name` has a 90% fill rate. Calculate the fill rate for each field and print it out.

## Goal 3: Generate Result Format
**Data Granularity:** The granularity of this data are expected to be at the per member, per month level, which means that if 
there are 100 medical events in the month of 11/2017 for member 123, there will be a single record that aggregates all 
the records together.

| Field Name          | Data Type       |
| ------------------- | --------------- |
| source_member_id    | String          |
| first_name          | String          |
| last_name           | String          |
| year_month          | String (yyyyMM) |
| total_claims_amount | Decimal         |
| total_paid_amount   | Decimal         |
| total_claim_count   | Int             |

Write these results out to a `.csv` file.