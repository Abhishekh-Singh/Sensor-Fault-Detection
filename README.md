# Sensor Component Failure Prediction

## Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class indicates that the failure was caused by something else.

The Data is provided by Scania, a major Swedish manufacturer, focusing on commercial vehicles—specifically heavy lorries, trucks and buses.

-- Challenge metric  

     Cost-metric of miss-classification:

     Predicted class |      True class       |
                     |    pos    |    neg    |
     -----------------------------------------
      pos            |     -     |  Cost_1   |
     -----------------------------------------
      neg            |  Cost_2   |     -     |
     -----------------------------------------
     Cost_1 = 10 and cost_2 = 500
     
     Total_cost = Cost_1*No_Instances + Cost_2*No_Instances.
     
     Create a model which accurately predicts and minimizes [the cost of] failures?

## Solution Proposed
This project aims to perform a root cause analysis of failures in the Air Pressure Systems (APS) of heavy-duty vehicles. This project aims to classify the causes of failure into two classes:

1. those originating from within the APS and
2. those resulting from external factors.

Through data analysis and feature engineering, we will identify the key contributors to APS failures and categorize them into the appropriate class. The outcome of this project will provide valuable insights and inform future measures to prevent similar failures and ensure the reliable operation of the APS.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.

 

## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## Data Collections

![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)

## Project Archietecture

![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)

## Deployment Archietecture

![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)