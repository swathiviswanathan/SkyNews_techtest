# Sky Challenge - BDD Test framework - Python

This BDD style automation framework is designed using python "behave".

## Installation

The required python libraries for framework execution are mentioned in `./requirements.txt` file. This is to provide easy dependency installation,

    pip3 install -r requirements.txt

It is advisible to create `virtualenv` in order to maintain independency.

### Drivers for web browsers

To execute scripts on browsers the execution machine should have the driver paths(chrome & firefox) set in system's environmental variables.

If driver paths are not set as part of environmental variable in your machine (you can confirm with `which chromedriver` & `which geckodriver`), please place the relevant drivers inside this repo and mention its "relative" path in `src/behave.ini` file for the framework to pick up appropriate drivers.

*Note: In mac `brew cask install chromedriver` & `brew install geckodriver` will install latest chromedriver version and will take care of setting the environmental variables*

### UserData in behave.ini

Attributes like `browser`, `url`, `path/to/driver/binaries` are parameterised in order to achieve easy maintenance. These are placed in `src/behave.ini` file which can later be altered at runtime if required.

### Iteration

BDD `Examples` are used to run the automated test scripts in iterations. In current implementation, the scenario will be executed 6 times, each time selecting a different news tile, validating the navigation and its contents. Please refer - `src/menuandnews.feature` file.

## Execution

`behave` command must be used to trigger the developed automation test scenario that is placed in `src/menuandnews.feature` file. Please ensure you are navigated into the `src` folder behave executing behave.

Parameters mentioned in `src/behave.ini` can be easily modified at run time like below,

    behave --tags=regression -D browser=Safari

*Note: tag `regression` will execute all validation steps under one scenario.

### Test case tagging

For easy execution, the test scenarios are grouped with tags like `@verify_functionality` (to test individual functionalities), `@functional` (which executes all functional test cases) and `@regression` (tests all validation steps in one scenario). Changing the `--tags` runtime parameter will pick the test scenarios accordingly.

## Reporting

It is recommended to use json result format as it will be lightweight and can later be used for html report generation and Jenkins integration. Use: `behave -f json -o ./results/result.json`.

If required, Allure is another easy way to generate rich html reports locally. `allure-behave` python library is used for this purpose.

To setup, ensure `allure` is installed in your machine to view the reports,

On mac,

    brew install allure

and `allure-behave` python library is required.

    pip install allure-behave

Then, execute behave with allure formatted report,

    behave -f allure_behave.formatter:AllureFormatter -o results/allure

to view the generated report, use the below command with appropriate(relative) folder path.

    allure serve results/allure

### Sample report

Please find below a snap of sample test result,

<img width="1280" alt="SkyNews_Report" src="https://user-images.githubusercontent.com/32310710/59247308-d60f3200-8c16-11e9-823f-2d871b4e46e9.png">

### NOTES

At times a few news contents title after navigated to, doesn't use all the words used at home page when it was displayed as a tile. Because of which the test script might fail.
