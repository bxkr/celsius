# celsius

```diff
@@celsius@@ is an arduino sketch and flask server combination, that creates simple temperature recording system.
```

### api access

```/celsius/get``` [GET] - Get all temperature records.<br />
```/celsius/get?type=last``` [GET] - Get last temperature record.<br />
```/celsius/get?type=day``` [GET] - Get all temperature records for the day.<br />
```/celsius/get?type=week``` [GET] - Get all temperature records for a week.<br />
```/celsius/get?type=month``` [GET] - Get all temperature records for a month.<br />
```/celsius/get?type=year``` [GET] - Get all temperature records for a year.<br />
```/celsius/post``` [POST] {time: timestamp | float, temperature: str} - Post one temperature record to the server from serial reader<br />
