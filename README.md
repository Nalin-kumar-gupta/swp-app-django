# GitHub - Nalin-kumar-gupta/swp-app-django

## Smart Walmart Packager

## Table of Contents
-   [Problem Statement](#problem-statement)
-   [Project Overview](#project-overview)
-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Future Aspects](#future-aspects)
-   [Contributing](#contributing)
-   [License](#license)
-   [Contact](#contact)

## Problem Statement
================
The truck loading process is a significant challenge in the logistics industry, resulting in inefficient use of space, weight imbalance, and excessive fuel consumption. This problem statement highlights the need for a space-optimized loading system to address these challenges and improve the overall efficiency of logistics operations.

1. According to the National Highway Traffic Safety Administration (NHTSA), in 2019, there were over 4,900 crashes involving large trucks in the United States, resulting in 5,005 fatalities and 123,000 injuries (NHTSA, 2020).
2. A study by the American Transportation Research Institute (ATRI) found that the trucking industry loses approximately 1.3 billion gallons of fuel annually due to weight imbalance and inefficient loading practices (ATRI, 2018).
3. The Federal Motor Carrier Safety Administration (FMCSA) reports that in 2019, there were over 415,000 police-reported crashes involving large trucks in the United States, resulting in over 4,000 fatalities and 100,000 injuries (FMCSA, 2020).
4. A study by the National Academy of Sciences found that the trucking industry could reduce fuel consumption by up to 20% through the adoption of more efficient loading practices and technologies (National Academy of Sciences, 2015).
5. The International Council on Clean Transportation estimates that the trucking industry could reduce greenhouse gas emissions by up to 40% through the adoption of more efficient loading practices and technologies (International Council on Clean Transportation, 2019).

## Project Overview
================

The Smart Walmart Packager is a cutting-edge solution designed to optimize trailer loading by maximizing package capacity, balancing axle weights, and ensuring a seamless loading experience. This innovative approach aims to significantly increase the efficiency of logistics operations.

### Captured Information

The following truck details are captured when it enters the warehouse:

-   Model name
-   Length
-   Breadth
-   Height
-   Tare weight
-   Gross Vehicle Weight Rating (GVWR)
-   Axle weight ratings
-   Axle group weight ratings
-   Wheel load capacity
-   Destination

### Solution Overview

The application leverages this information to identify relevant packages based on their destination and delivery dates. It then creates an optimized loading design, allocating packages to the trailer and providing real-time visibility into package placement. This proactive approach enables forecasting and planning, allowing logistics teams to stay one step ahead of shipments. By increasing product visibility, the Smart Walmart Packager revolutionizes the logistics industry, providing unparalleled insights into package movement and location.

## Features
================

### Warehouse Management System

The Manager feature provides a comprehensive warehouse management system to track and manage packages and trucks entering and leaving the warehouse. Key functionalities include:

-   Capturing truck dimensions, weight ratings, and loading capacities upon entry
-   Mapping packages to truck destinations and relevant delivery deadlines
-   Sending packages for analysis to the Visualizer server

### 3D Visualization

The Visualizer is a standalone microservice running on a separate server, designed to:

-   Create 3D packing designs and visualizations of packages
-   Increase packing efficiency and product visibility by identifying package locations within the truck
-   Facilitate unloading by knowing the exact location of each package

### Package Allocation

The Allocator feature allocates packages to trucks based on the visualizations created, enabling:

-   Early forecasting and prediction of delivery dates
-   Meeting supply chain demands by staying one step ahead
-   Optimized package allocation for efficient logistics operations

## Installation
================

To get a local copy up and running follow these simple steps.

### Prerequisites

-   Docker
-   Docker Compose

### Installation Steps


1.  Clone the repository:
    ```sh
    git clone https://github.com/Nalin-kumar-gupta/swp-app-django.git
    ```
2.  Change into the project directory:
    ```sh
    cd swp-app-django
    ```
3.  Build the Docker image:
    ```sh
    docker-compose -f local.yml build --no-cache
    ```
4.  Start the Docker container:
    ```sh
    docker-compose -f local.yml up
    ```
5.  View the web application running at `localhost:3000`

## Usage

To use this project, follow these steps:

1.  Start the application using Docker Compose
2.  Access the web application at `localhost:3000`
3.  Follow the on-screen instructions to use the application

## Future Aspects
================

### Warehouse Storage Optimization

The Visualizer microservice can be leveraged to optimize warehouse storage space, increasing package visibility and accessibility. By utilizing the same design principles, the location of packages within the warehouse can be easily identified, and employees can access the service via the warehouse's private network, ensuring data security.

#### Benefits

* Optimized warehouse storage space
* Increased package visibility and accessibility
* Enhanced data security through private network access

### Automation

The design created by the microservice contains package coordinates, which can be fed into robotics programming systems. With senior engineer approval, robots can efficiently place boxes, eliminating concerns about weight balancing and space optimization. This automated process can streamline truck loading, reducing errors and increasing efficiency.

#### Benefits

* Automated truck loading process
* Reduced errors and increased efficiency
* Enhanced weight balancing and space optimization

### Visibility

With the ability to track package locations within the trailer, IoT sensors can be strategically placed to detect potential threats to temperature-sensitive packages. This enables proactive measures to be taken, ensuring timely delivery and meeting critical supply chain demands.

#### Benefits

* Enhanced package visibility and tracking
* Proactive measures to ensure timely delivery
* Meeting critical supply chain demands

### Reverse Engineer

The Visualizer solution can be adapted to accommodate varying business workflows. For instance, if a business brings trucks on demand according to package volume, the Visualizer can reverse engineer the process to determine the optimal truck size needed to fit the desired number of packages, streamlining logistics operations.

#### Benefits

* Adaptability to varying business workflows
* Optimized truck size determination
* Streamlined logistics operations

### Forecasting

The Allocator service can proactively determine which packages will be allocated to which trucks, enabling organizations to stay ahead of supply chain timelines and meet retail market demands. This also provides customers with a clear view of their product's allocation, alleviating concerns about timely delivery.

#### Benefits

* Proactive package allocation and forecasting
* Enhanced supply chain timeline management
* Increased customer satisfaction through transparent allocation

By embracing these future aspects, the Smart Walmart Packager can continue to revolutionize the logistics industry, providing unparalleled efficiency, visibility, and customer satisfaction.

## Contributing
================

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License
================

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
================

Nalin Kumar Gupta - [nalinkrgupta@gmail.com](mailto:nalinkrgupta@gmail.com)

Project Link: [https://github.com/Nalin-kumar-gupta/swp-app-django](https://github.com/Nalin-kumar-gupta/swp-app-django)