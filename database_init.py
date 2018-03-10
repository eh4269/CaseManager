from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime
from database_setup import *

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Delete Categories if exisitng.
session.query(Category).delete()
# Delete Items if exisitng.
session.query(Items).delete()
# Delete Users if exisitng.
session.query(User).delete()

# Create fake users
User1 = User(name="Edward Hernandez",
              email="eh42699@gmail.com",
              picture='http://dummyimage.com/200x200.png/ff4444/ffffff')
session.add(User1)
session.commit()

User2 = User(name="Heather Hampel",
               email="hlh_0119@Yahoo.com",
               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
session.add(User2)
session.commit()

User3 = User(name="Lane Hernandez",
               email="lh4269@gmail.com",
               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
session.add(User3)
session.commit()

User4 = User(name="Landon Hernandez",
               email="lh42699@gmail.com",
               picture='http://dummyimage.com/200x200.png/cc0000/ffffff')
session.add(User4)
session.commit()

# Create fake categories
Category1 = Category(name="Application Fraud",
                      user_id=1)
session.add(Category1)
session.commit()

Category2 = Category(name="Market Manipulation",
                      user_id=1)
session.add(Category2)
session.commit

Category3 = Category(name="Mobile Phone Fraud",
                      user_id=4)
session.add(Category3)
session.commit()

Category4 = Category(name="Bank Account Fraud",
                      user_id=3)
session.add(Category4)
session.commit()

Category5 = Category(name="Payment Fraud",
                      user_id=2)
session.add(Category5)
session.commit()

# Populate a category with items for testing
# Using different users for items also
Item1 = Items(name="ADV-123141234",
               date=datetime.datetime.now(),
               description="OKLAHOMA CITY, Okla. – An armed robbery occurred early this morning at 13500 Plaza Terrace, Fairfield Inn, no injuries have been reported.It was reported that the front desk clerk decided to hide behind the desk till the suspects left.Two armed suspects were involved, both men, the victim says one was wearing a linen scarf the other was wearing an orange hoodie.Officers are still looking  the suspects.",
               picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOClrjq1SQiKRsgFCth9mcxt98AJnRQkDRJvAMjG0vU-n5QzHj",
               category_id=1,
               user_id=1)
session.add(Item1)
session.commit()

Item2 = Items(name="XSA-234234",
               date=datetime.datetime.now(),
               description="Columbus police are investigating the report of an armed robbery at store on Manchester Expressway.According to a police report, officers responded to the Circle K, 2510 Manchester Expressway, at 1:28 a.m. Saturday,  response to an alarm.The report did say what was taken.The report did  give a description of suspects.",
               picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMVJyTShHA8CqB_Y_hST-LSYtC7-MHVd3w0KRM6WIXrpUneqDMEg",
               category_id=4,
               user_id=3)
session.add(Item2)
session.commit()

Item3 = Items(name="ASD-1241243",
               date=datetime.datetime.now(),
               description="An armed robbery in the parking lot of a Raising Cane's store at 4036 Veterans Blvd, Metairie, is being investigated by the Jefferson Parish Sheriff's Office on Sunday afternoon (March 4). One man sustained non-life threatening injuries the incident. JPSO spokesman Jason Rivarde described the injuries  minor.A woman who answered the phone at the restaurant Sunday afternoon offered no further details.No further information was immediately available. ",
               picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp2hgW-U0moB0pG4PhOE72p19iIe_nz-HYT5ixFAcfS2WdCFkWDA",
               category_id=5,
               user_id=2)
session.add(Item3)
session.commit()

Item4 = Items(name="ASD-7894511",
               date=datetime.datetime.now(),
               description="An armed robbery in the parking lot of a Raising Cane's store at 4036 Veterans Blvd, Metairie, is being investigated by the Jefferson Parish Sheriff's Office on Sunday afternoon (March 4). One man sustained non-life threatening injuries the incident. JPSO spokesman Jason Rivarde described the injuries  minor.A woman who answered the phone at the restaurant Sunday afternoon offered no further details.No further information was immediately available. ",
               picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp2hgW-U0moB0pG4PhOE72p19iIe_nz-HYT5ixFAcfS2WdCFkWDA",
               category_id=4,
               user_id=4)
session.add(Item4)
session.commit()

print ("Your database has been populated with fake data!")
