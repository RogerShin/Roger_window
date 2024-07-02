--- 建立youbike table
CREATE TABLE IF NOT EXISTS youbike (
   	_id Serial Primary Key,
	sna VARCHAR(50) NOT NULL,
	sarea VARCHAR(50),
	ar VARCHAR(100),
	mday TIMESTAMP,
	updateTime TIMESTAMP,
	total SMALLINT,
	rent_bikes SMALLINT,
	return_bikes SMALLINT,
	lat REAL,
	lng REAL,
	act  BOOLEAN
);

--- 刪除youbike table
DROP TABLE youbike;

--- 新增資料
INSERT INTO youbike(sna, sarea, ar, mday, updateTime, total, rent_bikes, return_bikes, lat, lng, act)
VALUES ('臺大明達館北側(員工宿舍)',
		'臺大公館校區',
		'明達館北側前空地',
		'2024-06-24 14:13:20',
		'2024-06-24 14:23:52',
		18,
		18,
		0,
		25.01816,
		121.54469,
		true
	);

--- 查詢資料
SELECT * FROM youbike


--- 查比數
SELECT COUNT(*) FROM youbike
