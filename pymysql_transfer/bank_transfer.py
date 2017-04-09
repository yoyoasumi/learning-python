# -*- codingL utf8 -*-

import sys
import pymysql


class Transaction(object):
    def __init__(self, connection):
        self.connection = connection

    def transfer(self, src_acctid, dst_acctid, amount):
        try:
            self.check_account(src_acctid)
            self.check_account(dst_acctid)
            self.check_balance(src_acctid)
            self.withdrawal(src_acctid, amount)
            self.deposit(dst_acctid, amount)
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise e

    def check_account(self, acctid):
        print("[ Checking Account %s ...]" % acctid)
        cursor = self.connection.cursor()
        try:
            sql = "select * from account where id=%s" % acctid
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) != 1:
                raise Exception("[!] Account %s does not exist." % acctid)
        finally:
            cursor.close()
            print("Account %s Available." % acctid)

    def check_balance(self, acctid):
        print("[ Checking Balance of Account %s ... ]" % acctid)
        cursor = self.connection.cursor()
        try:
            sql = "select * from account where id=%s and balance>=%s" % (acctid, amount)
            cursor.execute(sql)
            rows = cursor.fetchall()
            if len(rows) != 1:
                raise Exception("[!] Account %s Insufficient Balance." % acctid)
        finally:
            cursor.close()
            print("Account %s has Sufficient Balance." % acctid)

    def withdrawal(self, acctid, amount):
        print("[ Withdrawing from Account %s ... ]" % acctid)
        cursor = self.connection.cursor()
        try:
            sql = "update account set balance=balance-%s where id=%s" % (amount, acctid)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("Withdrawal from Account %s Failed." % acctid)
        finally:
            cursor.close()
            print("Withdrawal Accomplished.")

    def deposit(self, acctid, amount):
        print("[ Depositing into Account %s ... ]" % acctid)
        cursor = self.connection.cursor()
        try:
            sql = "update account set balance=balance+%s where id=%s" % (amount, acctid)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("Deposit into Account %s Failed." % acctid)
        finally:
            cursor.close()
            print("Deposit Accomplished.")


if __name__ == "__main__":
    src_acctid = sys.argv[1]
    dst_acctid = sys.argv[2]
    amount = sys.argv[3]

    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='bank',
        charset='utf8'
    )
    transaction = Transaction(conn)

    try:
        transaction.transfer(src_acctid, dst_acctid, amount)
    except Exception as e:
        print(e)
    finally:
        conn.close()
