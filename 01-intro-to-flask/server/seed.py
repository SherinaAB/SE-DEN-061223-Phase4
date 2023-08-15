#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models


# 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# 8.✅ Create a query to delete all existing records from Production    
   
# 9.✅ Create some seeds for production and commit them to the database. 
p1 = Production(title="", genre="", director="", description="", budget="", image="", ongoing=True)
productions.append(p1)
p2 = Production(title="", genre="", director="", description="", budget="", image="", ongoing=True)
productions.append(p2)
p3 = Production(title="", genre="", director="", description="", budget="", image="", ongoing=False)
productions.append(p3)
p4 = Production(title="Hamilton", genre="Musical", director="Lin-Manuel Miranda", description="", budget="4000000.00", image="", ongoing=False)
productions.append(p4)

db.session.add.all(productions)
db.session.commit()

# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    
    