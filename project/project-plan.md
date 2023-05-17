# Project Plan

## Summary

This projects analyzes to what extent the time of day and the air temperature have an influence on parking violations in Bonn.

## Rationale

The City of Bonn can use the results to predict what the parking violations will be at different times of day, days of the week and temperatures. This allows them to come up with a new, more effective concept to prevent parking violations in Bonn.

## Datasources

### Datasource1: Weather Data of Bonn
* Offered by: Meteostat Developers https://dev.meteostat.net
* Metadata URL:  https://dev.meteostat.net/bulk/hourly.html
* Data URL: https://bulk.meteostat.net/v2/hourly/10517.csv.gz
* Data Type: CSV

Hourly data of weather parameters in Bonn. This endpoint provides one GZ compressed CSV file per weather station. The provided data is being aggregated from historical databases, METAR reports and SYNOP data.

Location Bonn:

```json
{
"id": "10517",
        "name": {
            "en": "Bonn-Friesdorf"
        },
        "country": "DE",
        "region": "NW",
        "identifiers": {
            "national": "00599",
            "wmo": "10517",
            "icao": null
        },
        "location": {
            "latitude": 50.7,
            "longitude": 7.15,
            "elevation": 64
        }
}
```


### Datasource2: Warnings and fines for stationary traffic (parking violations) 2022 in Bonn
* Offered by: Bonn via https://opendata.bonn.de
* Metadata URL: https://mobilithek.info/offers/-6571901671376151135
* Data URL: https://opendata.bonn.de/sites/default/files/ParkverstoesseBonn2020_0.csv
* Data Type: CSV

The data set contains the warnings and fines issued for parking violations in the city of Bonn. The list of offences is sorted by day, time, place, offence number, amount of the fine and type of vehicle (car/truck). The explanation of the individual offence numbers is listed in the uniform federal offence catalogue: https://www.kba.de/


## Work Packages

- [ ] 1. Data exploration [#1][i1]
- [ ] 2. Clean data [#2][i2]
- [ ] 3. Combine two datasets [#3][i3]
- [ ] 4. Data analysis [#4][i4]
- [ ] 5. Data pipeline [#5][i5]
- [ ] 6. Testing [#6][i6]
- [ ] 7. Continuous integration [#7][i7]
- [ ] 8. Publish project [#8][i8]

[i1]: https://github.com/jackDS008/2023-amse-template/issues/1
[i2]: https://github.com/jackDS008/2023-amse-template/issues/2
[i3]: https://github.com/jackDS008/2023-amse-template/issues/3
[i4]: https://github.com/jackDS008/2023-amse-template/issues/4
[i5]: https://github.com/jackDS008/2023-amse-template/issues/5
[i6]: https://github.com/jackDS008/2023-amse-template/issues/6
[i7]: https://github.com/jackDS008/2023-amse-template/issues/7
[i8]: https://github.com/jackDS008/2023-amse-template/issues/8
