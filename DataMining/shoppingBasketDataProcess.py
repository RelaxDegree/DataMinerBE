# -*- coding:utf-8 -*-
"""
作者：hp
日期：2022年 12月12日
"""
import pandas as pd
import pymysql


def preprocessShoppingtData2(sql = "select * from order_products__train, products   where order_products__train.product_id = products.product_id ORDER BY order_id ASC "):
    conn = pymysql.connect(host="127.0.0.1", user="root", password="", database="association_rules_mining",
                           charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql)
    res = cursor.fetchall()
    # print(res)
    pf = pd.DataFrame(list(res))
    # for item in res[0: 1000]:
    #     print(item)
    print(len(res))
    record = {}
    for item in res[0:1000000]:
        if item["order_id"] not in record.keys():
            record[item["order_id"]] = []
            record[item["order_id"]].append(item["product_name"])
        else:
            record[item["order_id"]].append(item["product_name"])
    for item in record.items():
        print(item)
    cursor.close()
    conn.commit()
    conn.close()
    print('购物篮数据预处理完毕')
    return record


# sql = "select * from order_products__train, products   where order_products__train.product_id = products.product_id ORDER BY order_id ASC "
# sql_conn(sql)


def preprocessShoppingtData1():
    initialData = pd.read_csv(
        "ProcessedData/Market_Basket_Optimisation.csv",
        # "ProcessedData/groceries.csv",
        error_bad_lines=False,  # 加入参数,
        encoding='utf-8',
        sep=',')
    initialData = initialData.values
    print(len(initialData))
    processedData = {}
    for i in range(len(initialData)):
        processedData[i] = initialData[i]
    return processedData

# preprocessShoppingtDataMoreDetailedly()
