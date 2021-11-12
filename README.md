### Features

An application has been made, where you can log in with a Google account, upload an XML file, and make some changes. The application does:
- Downloads the file in the background without making the user wait (TO BE ADDED).
- If the file extension is .xml and the file content matches the pattern, the file is saved in the database.
- If the file extension is not .xml, an 'Extension error' e-mail is sent to the user. If the file content does not fit the pattern, a 'Content error' e-mail is sent.
- A selected word is replaced by a selected word. The actions are sent to the user as an e-mail. (e.g. 1000 nodes' 100 fields word X changed with word Y) (TO BE ADDED)
- When the application starts working, control if there is a change in the XML file. If there is a change in the file, update the database, if there is not do nothing.

- 'sample_CustomersOrders.xml' is used as a sample file and 'sample_CustomersOrders.xsd' is used as a sample template.

- For the mail feature to work, gmail account and password must be entered in the `settings.py` file.
