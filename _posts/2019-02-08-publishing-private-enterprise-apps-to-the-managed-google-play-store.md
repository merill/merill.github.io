---
id: 1195
title: Publishing private enterprise apps to the managed Google Play Store
date: 2019-02-08 20:27:52 +0000


guid: 'https://merill.net/?p=1195'
permalink: /2019/02/publishing-private-enterprise-apps-to-the-managed-google-play-store/
medium_post:
  - >-
    O:11:"Medium_Post":11:{s:16:"author_image_url";N;s:10:"author_url";N;s:11:"byline_name";N;s:12:"byline_email";N;s:10:"cross_link";N;s:2:"id";N;s:21:"follower_notification";N;s:7:"license";N;s:14:"publication_id";N;s:6:"status";N;s:3:"url";N;}
xyz_lnap:
  - '1'
xyz_twap:
  - '1'
neve_meta_content_width:
  - '70'
categories:
  - Office 365
published: true
---
<!-- wp:paragraph -->
Here's a quick how to guide for publishing a private app to the managed Google Play store using the Custom App Publishing API and then surfacing it to your enterprise users through your EMM/MDM solution.
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
When you use this API your apps are;
<!-- /wp:paragraph -->

<!-- wp:list -->

<ul><li>permanently private, meaning they can't be made public</li><li>not subject to the public Google Play Store policies such as API target levels, application permission restrictions, etc</li><li>going through a streamlined verification process and appear in the managed Google Play Store in as little as five minutes, compared to over two hours via the Play Console </li><li> The only store listing details required to publish an app are its title and default listing language. </li></ul>

<!-- /wp:list -->

<!-- wp:paragraph -->
Before you can run the code below you need to set up a service account that has permissions to publish private apps. You can follow the guide <a href="https://developers.google.com/android/work/play/custom-app-api/get-started">here</a> to set it up.<br>
<!-- /wp:paragraph -->

<!-- wp:list {"ordered":true} -->

<ol><li>Enable the Google Play Custom App Publishing API</li><li>Create a service account</li><li>Obtain private app publishing rights</li><li>Retrieve the developer account id</li></ol>

<!-- /wp:list -->

<!-- wp:paragraph -->
At the end of this step you will have created a service account (eg myappname@turnkey-crowbar-123456.iam.gserviceaccount.com) and retreieved your developer account id (eg 1234567890123456789).
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
Next you need to generate the private key that will be used to authenticate against the API. To do this click on the Create Key button in the Service Account details page and save the json file to your local disk (keep this key very secure).
<!-- /wp:paragraph -->

<!-- wp:image {"id":1196} -->
<figure class="wp-block-image"><img src="https://merill.net/wp-content/uploads/2019/02/GoogleApiJson-1024x686.png" alt=" " class="wp-image-1196"/>

<figcaption>Create private key for service account</figcaption>

</figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
Next fire up your favourite code editor, reference one of the pre-built Google API libraries (or directly use the REST API) to publish the app.
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
Here's how I did it with Visual Studio.
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
Start a new console project and add a nuget reference to Google.Apis.Playcustomapp.v1.
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
Update the devAccountId, apkPath and clientSecretsJson variables in the code below and hit run. If all goes well the response returned is 'Complete'. If you receive a 'Failed' response take a look in the exception message for why it could have failed.
<!-- /wp:paragraph -->

<!-- wp:code -->

	class Program
    {
        static void Main(string[] args)
        {
            try
            {
                new Program().Run().Wait();
            }
            catch (AggregateException ex)
            {
                foreach (var e in ex.InnerExceptions)
                {
                    Console.WriteLine("ERROR: " + e.Message);
                }
            }
            Console.WriteLine("Press any key to continue...");
            Console.ReadKey();
        }

        private async Task Run()
        {
            long devAccountId = 1234567890123456789;
            var apkPath = @"C:\apps\MyPrivateApp.apk";
            var clientSecretsJson = @"C:\secrets\apppublishkey.json";

            var appMetaDda = new CustomApp
            {
                Title = "My Private Company App",
                LanguageCode = "en_AU"
            };

            GoogleCredential credential;
            using (var stream = new FileStream(clientSecretsJson, FileMode.Open, FileAccess.Read))
            {
                credential = GoogleCredential.FromStream(stream)
                    .CreateScoped("https://www.googleapis.com/auth/androidpublisher");
            }
          
            var svc = new Google.Apis.Playcustomapp.v1.PlaycustomappService(new Google.Apis.Services.BaseClientService.Initializer { HttpClientInitializer = credential });
            var request = svc.Accounts.CustomApps.Create(appMetaDda, devAccountId, File.OpenRead(apkPath), "application/octet-stream");
            var response = request.Upload();
            Console.WriteLine("Status = " + response.Status);
        }
    }
	
<!-- /wp:code -->
