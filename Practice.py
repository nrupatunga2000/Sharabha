

Day 3:

In companies they use sandbox for the development of salesforce applications.
There are 4 types: dev, dev pro, partial copy and full copy 
So application creation is done 
Whenever you login to salesforce in the setup page you find 9 dots at the left. That is called an app launcher. In the app launcher you can access the application you have built.
Whenever there is any admin  things going then first step is to go to setup (wheel icon)
Data - it is information stored. 
Metadata - Skeleton of the data storage.
Example: information inside the table is data whereas the column names in the table is metadata
There are 2 search boxes in the UI: a quick find box and global search box. The search box to the left side is a quick find box where only metadata can be searched, if you search for data you won’t find it there.
Here we are going to create an app for a mobile shop to sell mobile phones with details 
Products
Staff
Customer
New hires 

Building an APP
 We will build an application with the name iTech management 
To build an app quick search→app Manager→ new lightning app(top right corner)
Here you have to fill in the details. App name, developer name is the one which is a backend API name.
Standard way is to make the navigation bar horizontal, the console is keeping it vertical.
when it comes to the part of adding setup always choose the full setup as it includes both the servers and sales cloud features.
Next you will go to the personalization of utility items. This is to create some features like make a call, set some calendar or make a note etc. this will be created in th footer. Here we select notes and move further.
Now we move to navigation items.here we will be adding products, leads, contacts and accounts.
Now we will enter the navigation rules.choose subtabs initially to check the difference. This topic will be covered in security so please ignore it now but keep in your mind that we are system administrators as of now.
Now you are choosing the user profile as system administrator. Without giving the user profile we will not be able to access the application.
Now the app is built and it can be launched using app launcher. But before I launch it I have to test it.
To create or edit the app we have to go to the setup (wheel icon top right corner) then followed by the app manager.


SalesForce Day 4:

We have already created an app, but not yet completely done with it. So now we have to manage it 
Go to object manager which is present directly in the setup→ create → custom object. It is nothing but creating a customer table.
Now we have to enter labels, label plurals etc, which means that you will fill the table names.
Label : candidate
Label plural: candidates
In salesforce there are mandatory fields to be entered just to avoid nameless saves.
What are the options available at the time of object creation?
→ 
Allow Reports
Allow Activities
Track Field History
Allow in Chatter Groups
Enable Licensing

Checkbox all of the above options.
Allow reports:- you can create reports on this table.
Allow activities: it is divided into 2 parts 
→ task:giving a work for someone is a task
→ events: scheduling an interview is called an event.
Track field history: if a candidate does any changes that has to be kept in record, so it is necessary.
Allow chatter groups: chatting within the system. Like whatsapp etc example, @nrupatunga
Object classification:checkbox all of these 
Allow sharing: records can be shared
Bulk APIs access: 1000 records can be shared with someone at the same time as a bulk
Allow streaming APIs: share the details even outside the system.

Development status
Development: only the developer can see this field. Only the person created the field(admin but not all in the team)
Deployed: all people can see the field 
searches
Allow all searches both quick search and global search
Object Creation Options (Available only when custom object is first created)
Add notes and attachment: allow attachments and notes
Launch new custom tabs : allow to create a new tab. A tab is the one like home, leads, contacts etc. 
Checkbox add notes and attachment

So here by following all the processes we created an object.
Tabs are the only entrypoint of an object. It is the only way to create records in an object.
Now in tabs click on the lens which will give you some styles. Select one among the list.
For the next tabs add to profiles, keep everything default on, reason will be explained while explaining the security. Hit next
Now choose the objects where our tab has to be present, so we will choose our application and choose it.
Now go and check in the application in the dropdown. You will find the candidate's object.
It is necessary to find out what type of object it is, so go to object manager and see the API name 
There are 2 types of objects
Custom object: admin has created it 
Standard object: this was already present in the tool by default.
Now we have to create records.we can enter records in many ways that is by XL extraction, entering through external systems or manually.
To create manually first go to the tab candidates and top right corner click on new.
Application←Tabs←objects←fields←data
                                (tables)   (records)
Here now we have to create more fields for the candidate like DOB, qualification, CTC, fixed salary, variable salary, email, phone number, address, city, state, country, skills, languages etc
To create a field first we have to identify the object. Go to setup, object manager, select candidate then go to fields and relationships
Candidate is the field which we created and the others are user fields. It is important to differentiate what is a system field, standard field and custom field.
In SalesForce data types are divided into 3 types
Read only
Relational
Generic 
If you want to enter a few more fields then click on new and start entering the field.
Now keep everything visible for all the security related field properties.

                           





