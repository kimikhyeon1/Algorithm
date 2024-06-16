-- 코드를 작성해주세요
SELECT
    ID,
    (SELECT 
        FISH_NAME 
     FROM 
        FISH_NAME_INFO fn
     WHERE
        fi.FISH_TYPE = fn.FISH_TYPE
    ) FISH_NAME,
    LENGTH
FROM
    FISH_INFO fi
WHERE
    FISH_TYPE IN 
(
    SELECT 
        FISH_TYPE
    FROM FISH_INFO 
    GROUP BY FISH_TYPE 
    HAVING LENGTH = MAX(LENGTH)
)
ORDER BY
    ID 
