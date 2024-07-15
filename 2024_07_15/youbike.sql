SELECT * FROM youbike;


SELECT DISTINCT sarea FROM youbike;

-- 取站點最新資料
SELECT sna AS 站點, total AS 總車輛數, rent_bikes AS 可借, return_bikes AS 可還, mday AS 時間, act AS 狀態
FROM youbike
where (updatetime, sna) IN(
	SELECT MAX (updatetime), sna
		FROM youbike
		where sarea = '大同區'
		GROUP BY sna
);

SELECT MAX (updatetime), sna
FROM youbike
where sarea = '士林區'
GROUP BY sna;