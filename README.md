# BTC Analytics
An application for performing analytics on the bitcoin network.


## Overview
The goal of this project will be to develop a number of components:
* A BTC network listener and transaction parser
* A streaming producer targeted at the AWS Kinesis service
* A streaming analytics consumer, starting with AWS Kinesis Analytics and potentially shifting to Apache Flink
* A client dashboard to allow for graphical analysis


## Components
Below is a description of the various components.
* analytics/btc: code to encapsulate functionality regarding bitcoin
* analytics/utils: miscellaneous functionality for logging, api calls, etc.


## Testing
Below is the way that tests are implemented to validate functionality.

### Analytics
Attempted to keep code clean and minimize customization required for execution. For running the test scripts,
the scripts assume that it will be executed from the base directory of the repository. Thus, when executing the test
scripts, it is assumed that they will be executed as follows:

```
analytics/test/analytics_client.sh
analytics/test/analytics_btc_block.sh
analytics/test/analytics_btc_transaction.sh
```

Note that any customization that might be required for the scripts should be done via the analytics_env.sh file.

