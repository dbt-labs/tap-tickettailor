# ***Archival Notice***
This repository has been archived.

As a result all of its historical issues and PRs have been closed.

Please *do not clone* this repo without understanding the risk in doing so:
- It may have unaddressed security vulnerabilities
- It may have unaddressed bugs

<details>
   <summary>Click for historical readme</summary>

# tap-tickettailor

Author: Claire Carroll (claire@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:
- Generates a catalog of available data in TicketTailor
- Extracts the following resources:
 - Events
 - Issued Tickets
 - Orders

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-tickettailor.git
cd tap-tickettailor
pip install -e .
```

2. Get an API key

https://app.tickettailor.com/box-office/api

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your token and email

4. Run the application to generate a catalog.

```bash
tap-tickettailor -c config.json --discover > catalog.json
```

5. Select the tables you'd like to replicate

Step 4 generates a a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

6. Run it!

```bash
tap-tickettailor -c config.json --catalog catalog.json
```

Copyright &amp;copy; 2020 Fishtown Analytics

