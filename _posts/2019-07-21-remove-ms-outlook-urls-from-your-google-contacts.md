---
layout: post
published: false
title: Remove ms-outlook urls from your Google Contacts
---
Microsoft Outlook for mobile is one of the best, if not the best mobile mail client out there. However things can get a bit messy if you use the Save Contacts feature on iOS and also have a third party contact sync app keeping iCloud and GMail contacts in sync. I use the awesome [Contacts Sync for Google](https://apps.apple.com/au/app/contacts-sync-for-google-gmail/id454390333)

If you wind up with 100s of contacts having weird urls like 'ms-outlook://people/' or notes filled with the text 'This contact is read-only. To make changes, tap the link above to edit in Outlook.' then your in a bit of a bind especially if you have a bit of OCD like me.

Have no fear [Google Script](https://script.google.com) is here to rescue us. A simple hack and five minutes later you can enjoy a fully cleaned up contacts list without all the Outlook junk. 

  function myFunction() {
  var outlookJunkNote = "This contact is read-only. To make changes, tap the link above to edit in Outlook."
  var contacts = ContactsApp.getContacts();
  for (var c = 0; c < contacts.length; c++) {
    var cnt = contacts[c];
    
    //Clean outlook:// urls
    var fields = cnt.getUrls();
    for (var i = 0; i < fields.length; i++) {
      if(fields[i].getLabel() == "Outlook"){
        fields[i].deleteUrlField();
      }
    }
    
    //Clean outlook notes
    var notes = cnt.getNotes();
    if(notes.indexOf(outlookJunkNote) !== -1) {
       var regex = new RegExp(outlookJunkNote, 'g');
       var cleanNotes = notes.replace(regex, '');
       cnt.setNotes(cleanNotes);
    }
  }
}

I have published the script over at Google Script so you can simply save it your account and run it to clean up your Google contacts. [Remove Outlook Junk Script](https://script.google.com/a/merill.net/d/17QekwOHQwWAbELmO2xgiHnrRLkzMyaXo-1Fe2L_cBhGitMhsXJvL3asF/edit?usp=sharing)

