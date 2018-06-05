from db.base import DbManager
from db.models import BillItem


def get_all_bills():
    return DbManager().open().query(BillItem).all()

def get_bill(bill_id):
    return DbManager().open().query(BillItem).filter(BillItem.id == bill_id).one()

def create_bill(amount, description):
    bill = BillItem()
    bill.amount = amount
    bill.description = description
    DbManager().save(bill)

def delete_bill(bill_id):
    db = DbManager()
    bill = db.open().query(BillItem).filter(BillItem.id == bill_id).one()
    db.delete(bill)

def update_bill(bill_id, amount, description):
    db = DbManager()
    bill = db.open().query(BillItem).filter(BillItem.id == bill_id).one()
    bill.amount = amount
    bill.description = description
    db.save(bill)

