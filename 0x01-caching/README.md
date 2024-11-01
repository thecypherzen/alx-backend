# Overview #

## Background Context ##
Redis **Remote Dictionary Service** is ...

In this project, we  look at `Redis` in order to:
- Learn how to use redis for basic operations
- Learn how to use redis as a simple cache


## Reference Materials ##
The following can be used for referencing these areas, curated for optimized understanding:
- [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)
- [Redis commands](https://redis.io/docs/latest/commands/)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)


## Folder Details ###
- **Date Created:** Thur Oct. 24 2024 1:50am
- **Author:** [William Inyam](https.//github.com/thecypherzen/alx-backend-storage/blob/main/0x00-MySQL_Advanced/0x01-NoSQL).
- **Project Timeline:**
- **Released:** Wed Oct 23 - 6am.
  - **1st Deadline** Thur Oct. 24 2024 - 6am.
  - **Duration:** 24hrs
  - **Completed:** .


## Development Environment ##
### Install Redis on Ubuntu 18.04 ###

``` sh
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```


## Files  ###
*This is a high-level view of files in this directory and a short description of what they contain. Each file is task based and a full description of each task, requirement and constraints can be found in each file. The tasks are designed to test understanding of these concepts above....* **enjoy!**

| **SN** | File                         | Description                                         |
|----|----------------------------------------------------|---------------------------------------|
| 1. | [exercise.py](https://github.com/thecypherzen/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py) | A script that creates a class `Cache`. In the `__init__` method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using `flushdb`... |
