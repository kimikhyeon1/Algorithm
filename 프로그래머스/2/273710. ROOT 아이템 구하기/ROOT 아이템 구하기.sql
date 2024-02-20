-- 코드를 작성해주세요

SELECT info.ITEM_ID, info.ITEM_NAME 
  FROM ITEM_INFO info 
  JOIN ITEM_TREE tree
    ON info.ITEM_ID = tree.ITEM_ID
 WHERE tree.PARENT_ITEM_ID is NULL;