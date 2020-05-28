This is a system allow customer order car service, driver to get order , and control staff to edit order data <br>
Step to use this project:
1. in commandline run :
    * python manage.py makemigrations
    * python manage.py migrate
    * python manage.py createsuperuser
2. login into your superaccount (admin)
    * Add permission for control
        - app = controlapp
        - Content type =controllstaff
        - Codename = control
    * Add permission for driver
        - app = driverapp
        - Content type = driver
        - Codename = driver
3. In commandline enter python manage.py shell then import
      * setup1 
      * setup2
    <br>to create driver and cardata in csv file 
4. In admin site of the website create a controlstaff matched with a user and add it a permission of control created in 2 
5. In admin site of the website create a driver matched with a user and add it a permission of driver created in 2 
6. to create a customer please go to http://127.0.0.1:8000/ and register a customer account .
7. to enter a control site place please go to http://127.0.0.1:8000/controlstaff/ if you are not a controlstaff it will no allow to make any change and view im=nformation
8. to enter a driver site please go to http://127.0.0.1:8000/driverstaff/ if you are not a driver it will no allow to make any change and view im=nformation
9. In this app , the public customer make a account and create order
10. In this app , the control staff of company is used to confirm the order with customer and edit the order
11. In this app , driver is used to view order assigned to the driver
12. this app is design to minize the data leakage used by hacker to enhance data security
    - get as less data as once
    - no javascript provide if no permission gain to access a page
    - use token of csrf
    - do not use cookie and localstorage
13. this app can be view in mobile with setting of css in base.html

