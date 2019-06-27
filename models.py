
database:
  
  inbuilt we have sqlite  to use it need not to change any thng at all
  
  to check our database is  configured properly or not then use this commands 
  
  1.python manage.py shell
  2.from django.db import connection
  3.c=connection.cursor()
  
  if above commands work properly then need then database is ok to use
  
  
  
  =====================================================================================================================

  1. not neccesary to write any sql query in django
  
  
  
  
  ===============================================================================================
  
  
  MODELS:
    1. Charfield we should give max_length= " "
  
  
  
  python manage.py makemigrations =====> it is convert the model class of python into sql table 
  
  by executing above line we will get files like 0001__" ".py 
  
  to see sql code then use this command 
  
  ** python manage.py sqlmigrate appliction_name file_name
  then we can see cmplty sql query
  
  
  
  
  python manage.py migrate   ======> it is execute the that sql table 
  
  by this command multiple tables will be create even though we have only one app  because it willl goto create 
  tables for inbuilt apps also like admin ,auth session ...
  
  
======================================================================================

register model 
admin.site.register(model_name)

========================================================================================
def __str__(self):
  return self.nameof anyfield

===================================================================================================================
admin.py:
  
  to dislay only few columns in admin then we can chnge from here 
  
  
  class EmpAdmin(admin.ModelAdmin):
    list_display=["id","ename" ..]    ==>list_display is keyword 
    
   admin.site.register(emp,empAdmin)
  
  so in admin interface emp table only will above mentioned columns only
  
  
  
  ======================================================================================================












































