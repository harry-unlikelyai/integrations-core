# CHANGELOG - gearmand

## Unreleased

## 3.0.0 / 2023-08-10

***Changed***:

* Bump the minimum base check version ([#15427](https://github.com/DataDog/integrations-core/pull/15427))

***Added***:

* Update generated config models ([#15212](https://github.com/DataDog/integrations-core/pull/15212))

***Fixed***:

* Fix types for generated config models ([#15334](https://github.com/DataDog/integrations-core/pull/15334))

## 2.3.1 / 2023-07-10 / Agent 7.47.0

***Fixed***:

* Bump Python version from py3.8 to py3.9 ([#14701](https://github.com/DataDog/integrations-core/pull/14701))

## 2.3.0 / 2022-04-05 / Agent 7.36.0

***Added***:

* Add metric_patterns options to filter all metric submission by a list of regexes ([#11695](https://github.com/DataDog/integrations-core/pull/11695))

## 2.2.0 / 2022-02-19 / Agent 7.35.0

***Added***:

* Add `pyproject.toml` file ([#11352](https://github.com/DataDog/integrations-core/pull/11352))

***Fixed***:

* Fix namespace packaging on Python 2 ([#11532](https://github.com/DataDog/integrations-core/pull/11532))

## 2.1.2 / 2022-01-08 / Agent 7.34.0

***Fixed***:

* Add comment to autogenerated model files ([#10945](https://github.com/DataDog/integrations-core/pull/10945))

## 2.1.1 / 2021-11-16 / Agent 7.33.0

***Fixed***:

* Update config example to match implementation and refactor tests ([#10639](https://github.com/DataDog/integrations-core/pull/10639))

## 2.1.0 / 2021-11-13

***Added***:

* Add runtime configuration validation ([#8917](https://github.com/DataDog/integrations-core/pull/8917))

## 2.0.1 / 2021-10-04 / Agent 7.32.0

***Fixed***:

* Add server as generic tag ([#10100](https://github.com/DataDog/integrations-core/pull/10100))

## 2.0.0 / 2021-08-22 / Agent 7.31.0

***Changed***:

* Remove messages for integrations for OK service checks ([#9888](https://github.com/DataDog/integrations-core/pull/9888))

## 1.8.1 / 2021-03-07 / Agent 7.27.0

***Fixed***:

* Bump minimum base package version ([#8443](https://github.com/DataDog/integrations-core/pull/8443))

## 1.8.0 / 2020-10-31 / Agent 7.24.0

***Added***:

* [doc] Add encoding in log config sample ([#7708](https://github.com/DataDog/integrations-core/pull/7708))
* Add log integration ([#7616](https://github.com/DataDog/integrations-core/pull/7616))

## 1.7.0 / 2020-09-21 / Agent 7.23.0

***Added***:

* Add config spec ([#7612](https://github.com/DataDog/integrations-core/pull/7612))

## 1.6.0 / 2020-05-17 / Agent 7.20.0

***Added***:

* Allow optional dependency installation for all checks ([#6589](https://github.com/DataDog/integrations-core/pull/6589))

## 1.5.0 / 2020-04-04 / Agent 7.19.0

***Added***:

* Collect version metadata ([#5927](https://github.com/DataDog/integrations-core/pull/5927))

***Fixed***:

* Update deprecated imports ([#6088](https://github.com/DataDog/integrations-core/pull/6088))

## 1.4.0 / 2020-01-13 / Agent 7.17.0

***Added***:

* Use lazy logging format ([#5377](https://github.com/DataDog/integrations-core/pull/5377))

## 1.3.1 / 2019-10-11 / Agent 6.15.0

***Fixed***:

* Fix misleading gearman.workers metric (#4515) ([#4520](https://github.com/DataDog/integrations-core/pull/4520)) Thanks [orgito](https://github.com/orgito).

## 1.3.0 / 2019-05-14 / Agent 6.12.0

***Added***:

* Adhere to code style ([#3508](https://github.com/DataDog/integrations-core/pull/3508))

## 1.2.0 / 2019-01-04 / Agent 6.9.0

***Added***:

* Support Python 3 ([#2738](https://github.com/DataDog/integrations-core/pull/2738))

## 1.1.1 / 2018-09-04 / Agent 6.5.0

***Fixed***:

* Add data files to the wheel package ([#1727](https://github.com/DataDog/integrations-core/pull/1727))

## 1.1.0 / 2018-03-23

***Added***:

* Add custom tag support to service check.

## 1.0.1 / 2017-07-18

***Fixed***:

* Re-use gearman admin connections, fixes connection leak issue ([#422](https://github.com/DataDog/integrations-core/issues/422), thanks [@sophaskins](https://github)com/sophaskins)

## 1.0.0 / 2017-03-22

***Added***:

* adds gearmand integration.

