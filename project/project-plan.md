# Project Plan

## Summary

This projects analyzes to what extent the time of day and the air temperature have an influence on car park use in Cologne.

## Rationale

The City of Cologne can use the results to predict what the car park utilisation will be at different times of day, days of the week and temperatures. This allows them to come up with a new, more effective concept for parking in Cologne.

## Datasources

### Datasource1: Weather Data of Cologne
* Offered by: Meteostat Developers https://dev.meteostat.net
* Metadata URL:  https://dev.meteostat.net/bulk/hourly.html
* Data URL: https://bulk.meteostat.net/v2/hourly/D2968.csv.gz
* Data Type: CSV
* Further information: tbd

Hourly data of weather parameters in Cologne. This endpoint provides one GZ compressed CSV file per weather station. The provided data is being aggregated from historical databases, METAR reports and SYNOP data.

Location Cologne:

```json
{
"id": "D2968",
        "name": {
            "en": "Köln-Stammheim"
        },
        "country": "DE",
        "region": "NW",
        "identifiers": {
            "national": "02968",
            "wmo": null,
            "icao": null
        },
        "location": {
            "latitude": 50.9894,
            "longitude": 6.9777,
            "elevation": 43
        }
}
```


### Datasource2: Car park occupancy (Cologne)
* Offered by: Köln via https://offenedaten-koeln.de/dataset/647ed189-ce31-40db-9b9d-353a7768dadf/resource/34681d19-c5c6-4a01-8d10-c8cc4b699dcd
* Metadata URL: https://mobilithek.info/offers/-7694090497647342627
* Data URL: https://www.stadt-koeln.de/externe-dienste/open-data/parking.php
* Data Type: JSON

The car park occupancy data provides you with an overview of the current car park occupancy in Cologne. The update times are approximately 5 to 10 minutes.


## Work Packages

1. Data exploration [#1][i1]
2. Clean data [#2][i2]
3. Combine two datasets [#3][i3]
4. Data analysis [#4][i4]
5. Data pipeline [#5][i5]
6. Testing [#6][i6]
7. Continuous integration [#7][i7]
8. Publish project [#8][i8]

[i1]: https://github.com/jackDS008/2023-amse-template/issues/1
[i2]: https://github.com/jackDS008/2023-amse-template/issues/2
[i3]: https://github.com/jackDS008/2023-amse-template/issues/3
[i4]: https://github.com/jackDS008/2023-amse-template/issues/4
[i5]: https://github.com/jackDS008/2023-amse-template/issues/5
[i6]: https://github.com/jackDS008/2023-amse-template/issues/6
[i7]: https://github.com/jackDS008/2023-amse-template/issues/7
[i8]: https://github.com/jackDS008/2023-amse-template/issues/8
