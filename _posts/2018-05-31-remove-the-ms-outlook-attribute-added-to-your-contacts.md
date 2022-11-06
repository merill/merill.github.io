---
id: 1176
title: Remove the ms-outlook attribute added to your contacts
date: 2018-05-31T20:27:52+00:00


guid: https://merill.net/?p=1176
permalink: /2018/05/remove-the-ms-outlook-attribute-added-to-your-contacts/
medium_post:
  - 'O:11:"Medium_Post":11:{s:16:"author_image_url";s:69:"https://cdn-images-1.medium.com/fit/c/200/200/0*nOSMyIhdQJ9325FH.jpeg";s:10:"author_url";s:26:"https://medium.com/@merill";s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";s:2:"no";s:2:"id";s:12:"a05a2a722663";s:21:"follower_notification";s:3:"yes";s:7:"license";s:19:"all-rights-reserved";s:14:"publication_id";s:12:"99858869fb3c";s:6:"status";s:6:"public";s:3:"url";s:94:"https://medium.com/@merill/remove-the-ms-outlook-attribute-added-to-your-contacts-a05a2a722663";}'
xyz_lnap:
  - "1"
xyz_twap:
  - "1"
categories:
  - Office 365
---
Like me if you had the unfortunate luck of using the Outlook app's feature to sync your Gmail contacts to iOS and then used a sync app like Google Contacts sync you might have ended up with a whole bunch of contacts having an attribute called outlook with a value that says ms-outlook.

The fix is quite easy really. Using the awesome Script editor at https://script.google.com you can run this simple function to get rid of the stuff you don't want.

<pre>
<code>
function myFunction() {
  var contacts = ContactsApp.getContacts();
  for (var c = 0; c < contacts.length; c++) {
    var cnt = contacts[c];
    var fields = cnt.getUrls();
    for (var i = 0; i < fields.length; i++) {
      if(fields[i].getLabel() == "Outlook"){
        fields[i].deleteUrlField();
      }
    }
  }
}
</code>
</pre>